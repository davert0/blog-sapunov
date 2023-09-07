from backend.services.user_services import get_password_hash
import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status


from backend.db.dao.user_dao import UserDAO


@pytest.fixture
def admin_user(dbsession: AsyncSession):
    dao = UserDAO(dbsession)
    user = UserDAO.create_user_model("admin", "admin@email.com", "123qwe123", True)
    return user


@pytest.mark.anyio
async def test_creation(
    fastapi_app: FastAPI,
    client: AsyncClient,
    dbsession: AsyncSession,
) -> None:
    dao = UserDAO(dbsession)
    user = await dao.create_user_model("admin", "admin@email.com", get_password_hash("123qwe123"), True)
    url = fastapi_app.url_path_for("login_for_access_token")
    form_data = {
        "username": "admin@email.com",
        "password": "123qwe123"
    }
    response = await client.post(url, data=form_data)
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

# @pytest.mark.anyio
# async def test_getting(
#     fastapi_app: FastAPI,
#     client: AsyncClient,
#     dbsession: AsyncSession,
# ) -> None:
#     """Tests dummy instance retrieval."""
#     dao = ArticleDAO(dbsession)
#     test_name = uuid.uuid4().hex
#     await dao.create_article_model(name=test_name, text="test")
#     url = fastapi_app.url_path_for("get_article_models")
#     response = await client.get(url)
#     articles = response.json()

#     assert response.status_code == status.HTTP_200_OK
#     assert len(articles) == 1
#     assert articles[0]["name"] == test_name
