import uuid

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from backend.db.dao.article_dao import ArticleDAO




@pytest.mark.anyio
async def test_creation_no_auth(
    fastapi_app: FastAPI,
    client: AsyncClient,
) -> None:
    url = fastapi_app.url_path_for("create_article_model")
    test_name = uuid.uuid4().hex
    response = await client.put(
        url,
        json={"name": test_name, "text": "test"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.anyio
async def test_creation_no_admin(
    fastapi_app: FastAPI,
    authed_client: AsyncClient,
) -> None:
    url = fastapi_app.url_path_for("create_article_model")
    test_name = uuid.uuid4().hex
    response = await authed_client.put(
        url,
        json={"name": test_name, "text": "test"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN




@pytest.mark.anyio
async def test_creation_admin(
    fastapi_app: FastAPI,
    admin_client: AsyncClient,
) -> None:
    url = fastapi_app.url_path_for("create_article_model")
    test_name = uuid.uuid4().hex
    response = await admin_client.put(
        url,
        json={"name": test_name, "text": "test"},
    )
    assert response.status_code == status.HTTP_200_OK




@pytest.mark.anyio
async def test_getting(
    fastapi_app: FastAPI,
    client: AsyncClient,
    dbsession: AsyncSession,
) -> None:
    """Tests dummy instance retrieval."""
    dao = ArticleDAO(dbsession)
    test_name = uuid.uuid4().hex
    await dao.create_article_model(name=test_name, text="test")
    url = fastapi_app.url_path_for("get_article_models")
    response = await client.get(url)
    articles = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(articles) == 1
    assert articles[0]["name"] == test_name
