# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#: 数据库连接的URL
from app.core.config import SQLALCHEMY_DATABASE_URL
from sqlalchemy.ext.declarative import declarative_base
# from app.core.config import SQLALCHEMY_DATABASE_URL
from sqlalchemy import Boolean, Column, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import relationship

#: 创建连接数据库的engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
#: Session Local 数据库连接的session -> "每次和数据库的对话" 每次对话调用这个
SessionLocal = sessionmaker(bind=engine, autoflush=False)

db = SessionLocal()
#:Base 类, declarative_base()的结果, 一个模版of class 会在model.py里用到
DBBase = declarative_base()

#:Base 类, declarative_base()的结果, 一个模版of class 会在model.py里用到
DBBase = declarative_base()


class FtUser(DBBase):
    __tablename__ = "ftusers"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(32))
    is_active = Column(Boolean, default=False)
    #: 定义FtUser的ftarticle和Articles的关系. 关联其他table的field
    ftarticle = relationship("Articles", back_populates="author")


class Articles(DBBase):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60), index=True)
    content_url = Column(String(256), unique=True)
    tags = Column(String(128))
    #:关系, 把文章的author_id和用户的id联系
    author_id = Column(Integer, ForeignKey("ftusers.id"))
    author = relationship("FtUser", back_populates="ftarticle")
