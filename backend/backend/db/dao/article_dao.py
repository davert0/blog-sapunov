from typing import List, Optional

from fastapi import Depends
from sqlalchemy import delete, select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.dependencies import get_db_session
from backend.db.models.article import Article


class ArticleDAO:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_article_model(self, name: str, text: str) -> Article:
        article = Article(name=name, text=text)
        self.session.add(article)
        return article
    

    async def delete_article_model(self, name: str) -> None:
        await self.session.execute(
            delete(Article).where(Article.name==name)
        )
    
    async def get_all_articles(self, limit: int, offset: int) -> List[Article]:

        raw_articles = await self.session.execute(
            select(Article)
            .options(selectinload(Article.tags))
            .limit(limit)
            .offset(offset),
        )

        return list(raw_articles.scalars().fetchall())

    async def filter(
        self,
        name: Optional[str] = None,
    ) -> List[Article]:
        query = select(Article)
        if name:
            query = query.where(Article.name == name)
        rows = await self.session.execute(query)
        return list(rows.scalars().fetchall())
