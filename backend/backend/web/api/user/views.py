from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from backend.web.api.user.schema import Token, UserDTO
from backend.db.dao.user_dao import UserDAO
from backend.db.models.user import User
from backend.services.user_services import (
    authenticate_user,
    create_access_token,
    get_current_active_user,
)


ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_dao: Annotated[UserDAO, Depends()],
):
    user = await authenticate_user(user_dao, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserDTO)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user
