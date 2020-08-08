# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#: 数据库连接的URL
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://jyq:qq20040915@localhost/blogs'

#: 创建连接数据库的engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
#: Session Local 数据库连接的session -> "每次和数据库的对话" 每次对话调用这个
SessionLocal = sessionmaker(bind=engine, autoflush=False)

#:Base 类, declarative_base()的结果, 一个模版of class 会在model.py里用到
DBBase = declarative_base()
