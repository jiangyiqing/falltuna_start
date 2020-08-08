# -*- coding: utf-8 -*-
from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class Article(BaseModel):
    id: int
    owner_id: int
    tags: str
    content_url: str

    class Config:
        orm_mode = True


class FtUser(UserBase):
    id: int
    is_active = bool
    articles: List[Article] = []

    class Config:
        orm_mode = True
