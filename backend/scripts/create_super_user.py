import asyncio
import getpass
import re
from backend.db.dao.user_dao import UserDAO
from sqlalchemy.exc import IntegrityError
from backend.services.user_services import get_password_hash
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from backend.settings import settings

async def get_username():
    username = await asyncio.get_running_loop().run_in_executor(None, input, "Введите имя пользователя: ")
    return username

async def get_email():
    while True:
        email = await asyncio.get_running_loop().run_in_executor(None, input, "Введите адрес электронной почты: ")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Некорректный адрес электронной почты. Попробуйте еще раз.")
        else:
            return email

async def get_password():
    while True:
        password = await asyncio.get_running_loop().run_in_executor(None, getpass.getpass, "Введите пароль: ")
        if len(password) < 8:
            print("Пароль должен быть не менее 8 символов.")
        else:
            confirm_password = await asyncio.get_running_loop().run_in_executor(None, getpass.getpass, "Повторите пароль: ")
            if password == confirm_password:
                return password
            else:
                print("Пароли не совпадают. Попробуйте еще раз.")

async def create_super_user(username: str, email: str, hashed_password: str):
    engine = create_async_engine(
        str(settings.db_url),
    )
    async_session = async_sessionmaker(engine, expire_on_commit=True)
    async with async_session.begin() as session:
        dao = UserDAO(session)
        await dao.create_user_model(username, email, hashed_password, is_admin=True)
        await dao.session.commit()

async def async_main() -> None:
    username = await get_username()
    email = await get_email()
    password = await get_password()
    hashed_password = get_password_hash(password)
    try:
        await create_super_user(username, email, hashed_password)
        print("Суперпользователь успешно создан")
    except IntegrityError as e:
        print("Не удалось создать суперпользователя")
        print(e)




asyncio.run(async_main())