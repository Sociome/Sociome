from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

# This is the main model of post that user will pass 
class PostBase(BaseModel):
    content: str #the main content of the post 
    published: bool =True #the post will be published or not default is set to true
    image: Optional[str]

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    user_id: int
    fullname: str
    username: str
    bio: str
    github_link: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    post_id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    fullname: str
    username: str
    bio: str
    github_link: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)