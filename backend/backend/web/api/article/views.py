from typing import Annotated, List
from backend.db.models.user import User
from backend.services.user_services import get_current_active_user

from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends

from backend.db.dao.article_dao import ArticleDAO
from backend.db.models.article import Article
from backend.web.api.article.schema import ArticlelDTO, ArticlelInputDTO, ArticlelInputDeleteDTO

router = APIRouter()


@router.get("/", response_model=List[ArticlelDTO])
async def get_article_models(
    limit: int = 10,
    offset: int = 0,
    article_dao: ArticleDAO = Depends(),
) -> List[Article]:
    """
    Retrieve all dummy objects from the database.

    :param limit: limit of dummy objects, defaults to 10.
    :param offset: offset of dummy objects, defaults to 0.
    :param dummy_dao: DAO for dummy models.
    :return: list of dummy objects from database.
    """
    return await article_dao.get_all_articles(limit=limit, offset=offset)


@router.post("/", response_model=ArticlelDTO)
async def create_article_model(
    new_article_object: ArticlelInputDTO,
    article_dao: Annotated[ArticleDAO, Depends()],
    current_user: Annotated[User, Depends(get_current_active_user)]
) -> Article:
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient privilege",
        )
    article = await article_dao.create_article_model(**new_article_object.dict())
    return article


@router.delete("/")
async def delete_article_model(
    article_object: ArticlelInputDeleteDTO,
    article_dao: Annotated[ArticleDAO, Depends()],
    current_user: Annotated[User, Depends(get_current_active_user)]
) -> None:
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient privilege",
        )

    await article_dao.delete_article_model(**article_object.dict())
