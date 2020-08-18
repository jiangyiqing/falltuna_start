# -*- coding: utf-8 -*-
# from sqlalchemy.orm import Session
from app.models.database import *
#: Read

# db = SessionLocal()


def get_ftuser(user_id: int):
    user_id = int(user_id)
    ftuser = db.query(FtUser).filter(FtUser.id == user_id).one_or_none()
    return ftuser


def create_ftuser(user):
    fake_pwd = user.password
    db_user = FtUser(email=user.email, hashed_password=fake_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
