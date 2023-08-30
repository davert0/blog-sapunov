from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from backend.db.dao.article_dao import ArticleDAO
from backend.db.models.article import Article
from backend.web.api.article.schema import ArticlelDTO, ArticlelInputDTO

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


@router.put("/")
async def create_article_model(
    new_article_object: ArticlelInputDTO,
    article_dao: ArticleDAO = Depends(),
) -> None:
    """
    Creates dummy model in the database.

    :param new_dummy_object: new dummy model item.
    :param dummy_dao: DAO for dummy models.
    """
    await article_dao.create_article_model(**new_article_object.dict())
