from datetime import timedelta
from typing import Any, AsyncGenerator
from backend.db.dao.user_dao import UserDAO
from backend.services.user_services import create_access_token, get_password_hash

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy import true
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from backend.db.dependencies import get_db_session
from backend.db.utils import create_database, drop_database
from backend.settings import settings
from backend.web.application import get_app


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    """
    Backend for anyio pytest plugin.

    :return: backend name.
    """
    return "asyncio"


@pytest.fixture(scope="session")
async def _engine() -> AsyncGenerator[AsyncEngine, None]:
    """
    Create engine and databases.

    :yield: new engine.
    """
    from backend.db.meta import meta  # noqa: WPS433
    from backend.db.models import load_all_models  # noqa: WPS433

    load_all_models()

    await create_database()

    engine = create_async_engine(str(settings.db_url))
    async with engine.begin() as conn:
        await conn.run_sync(meta.create_all)

    try:
        yield engine
    finally:
        await engine.dispose()
        await drop_database()


@pytest.fixture
async def dbsession(
    _engine: AsyncEngine,
) -> AsyncGenerator[AsyncSession, None]:
    """
    Get session to database.

    Fixture that returns a SQLAlchemy session with a SAVEPOINT, and the rollback to it
    after the test completes.

    :param _engine: current engine.
    :yields: async session.
    """
    connection = await _engine.connect()
    trans = await connection.begin()

    session_maker = async_sessionmaker(
        connection,
        expire_on_commit=False,
    )
    session = session_maker()

    try:
        yield session
    finally:
        await session.close()
        await trans.rollback()
        await connection.close()


@pytest.fixture
def fastapi_app(
    dbsession: AsyncSession,
) -> FastAPI:
    """
    Fixture for creating FastAPI app.

    :return: fastapi app with mocked dependencies.
    """
    application = get_app()
    application.dependency_overrides[get_db_session] = lambda: dbsession
    return application  # noqa: WPS331


@pytest.fixture
async def client(
    fastapi_app: FastAPI,
    anyio_backend: Any,
) -> AsyncGenerator[AsyncClient, None]:
    """
    Fixture that creates client for requesting server.

    :param fastapi_app: the application.
    :yield: client for the app.
    """
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
async def authed_client(dbsession: AsyncSession, client: AsyncClient):
    dao = UserDAO(dbsession)
    username =  "admin@email.com"
    password = get_password_hash("123qwe123")
    user = await dao.create_user_model("admin", username, password)
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    client.headers = {"Authorization": f"Bearer {access_token}"}
    yield client

@pytest.fixture
async def admin_client(dbsession: AsyncSession, client: AsyncClient):
    dao = UserDAO(dbsession)
    username =  "admin@email.com"
    password = get_password_hash("123qwe123")
    user = await dao.create_user_model("admin", username, password, True)
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    client.headers = {"Authorization": f"Bearer {access_token}"}
    yield client