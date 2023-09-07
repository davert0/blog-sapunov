from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.dependencies import get_db_session
from backend.db.models.user import User


class UserDAO:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_user_model(
        self, username: str, email: str, password: str, is_admin: bool = False
    ) -> User:

        user = User(
            username=username,
            email=email,
            password=password,
            is_admin=is_admin,
            disabled=False,
        )
        self.session.add(user)

        return user
    

    async def get_user(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        raw_user = await self.session.execute(query)
        return raw_user.scalar_one_or_none()
