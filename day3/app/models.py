# -*- coding: utf-8 -*-
from sqlalchemy import Boolean, Column, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import relationship

from database import DBBase


class FtUser(DBBase):
    __tablename__ = "ftusers"
    #:?
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(32))
    is_active = Column(Boolean, default=False)
    #: 定义FtUser的ftarticle和Articles的关系. 关联其他table的field
    ftarticle = relationship("Articles", back_populates="author")
    #: 为了学习Migration, 新加一个Column
    avatar = Column(String(200))
    nick = Column(String(30))


class Articles(DBBase):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60), index=True)
    content_url = Column(String(256), unique=True)
    tags = Column(String(128))
    #:关系, 把文章的author_id和用户的id联系
    author_id = Column(Integer, ForeignKey("ftusers.id"))
    author = relationship("FtUser", back_populates="ftarticle")
