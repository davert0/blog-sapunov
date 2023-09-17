import asyncio
from backend.db.dao.article_dao import ArticleDAO
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from backend.settings import settings


async def create_articles():
    engine = create_async_engine(
        str(settings.db_url),
    )
    async_session = async_sessionmaker(engine, expire_on_commit=True)
    async with async_session.begin() as session:
        dao = ArticleDAO(session)
        for i in range(3):
            await dao.create_article_model(
                f"test-{i}", '"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."'
            )
        await dao.session.commit()

async def async_main() -> None:

    try:
        await create_articles()
    except IntegrityError as e:
        print(e)




asyncio.run(async_main())