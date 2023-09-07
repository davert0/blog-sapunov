from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserDTO(BaseModel):
    id: int
    username: str
    email: str
    disabled: bool
    is_admin: bool
    
    class Config:
        orm_mode = True

class UserInDBDTO(UserDTO):
    hashed_password: str

