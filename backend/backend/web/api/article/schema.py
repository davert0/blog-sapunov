from pydantic import BaseModel
from typing import List


class TagDTO(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ArticlelDTO(BaseModel):

    id: int
    name: str
    text: str
    tags: List[TagDTO]

    class Config:
        orm_mode = True



class ArticlelInputDTO(BaseModel):
    name: str
    text: str

