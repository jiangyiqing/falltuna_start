# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session
import models
import schemas

#: Read


def get_ftuser(db: Session, user_id: int):
    ftuser = db.query(models.FtUser).filter(
        models.User.id == user_id).one_or_none()
    return ftuser
#: Read


def create_ftuser(db: Session, user: schemas.UserCreate):
    fake_pwd = user.password
    db_user = models.FtUser(email=user.email, hashed_password=fake_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
