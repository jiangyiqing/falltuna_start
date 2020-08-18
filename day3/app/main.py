# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud
import models
import schemas
from fastapi import FastAPI, Body, Form, UploadFile, File, Response, Depends
from typing import Optional
from fastapi.responses import FileResponse
import uvicorn
import sys
print(sys.path)

import logging

fastapi_logger = logging.getLogger()
fh = logging.FileHandler("main_log.log")
fh.setLevel(logging.ERROR)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
fastapi_logger.addHandler(fh)

#: 这句话是创建数据库
models.DBBase.metadata.create_all(bind=engine)

app = FastAPI()


#:数据库的dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


async def com_param(q: Optional[str] = None, skip2: int = 0):
    return{"q": q, "skip2": skip2}


@app.get("/")
async def root():
    '''
    GET请求, 输入网址发送请求
    返回: JSON, {"message": "Hi cons"}
    '''
    return {"message": "Hi cons"}


@app.get("/treq/{item_name}")
async def treqf(item_name: str):
    '''
    GET Path Param
    '''
    print('item_name', item_name)
    '''
    返回 JSON
    '''
    return {"value": item_name}


@app.get("/qreq/")
async def qreqf(skip: int = 0, limit: int = 10, p: dict = Depends(com_param)):
    '''
    GET Query Param
    从上面的fake_items_db中返回第skip个开始到limit个项, 用于查询数据等
    '''
    print(jyq)
    return {
        "fake_items": fake_items_db[skip: skip + limit],
        "commons": p
    }


@app.post("/tpostreq")
async def tpostreq(req=Body(...)):
    '''
    POST Test Json
    '''
    print(req)
    return {"data": req}


@app.post("/tpostreqc")
async def tpostreqc(
        name=Body(...),
        classNo=Body(...),
        age=Body(...)
):
    '''
    POST Test Json, 按照变量名称获取值
    ＊ 此方法更严谨 (对传来的请求要求高)
    可以Optional (泤乎不行)
    返回: Json
    '''
    return {"data": name}


@app.post("/form", tags=["form"])
async def get_form(name: str = Form(...), age: int = Form(...)):
    '''
    POST Form(表单), 用在用户名/密码这里
    '''
    print(name, age)
    return {"data": age}


@app.post("/image/")
async def upload_image(file: UploadFile = File(...)):
    '''
    upload_image:
        file.file: <class 'tempfile.SpooledTemporaryFile'>
        需要用.read()转成bytes,
        file.content_type: 类型
        file.filename: 名
    因为可以辨别文件名和类型, 推荐此
    '''
    print("file_name", file.filename)
    print("file_type", file.content_type)
    output = open("img.png", "wb")
    output.write(file.file)
    output.close()


@app.post("/img/")
async def file_image(file: bytes = File(...)):
    '''
    file:
        bytes, 没有名字和类型
    '''
    output = open("img.png", "wb")
    output.write(file)
    output.close()


@app.get("/getimg")
async def getimg():
    return FileResponse("image.png", media_type="image/png")


'''
下面是正式服务用的API
'''


@app.post("/create-user/")
async def create_user(user: schemas.UserCreate = Body(...), db: Session = Depends(get_db)):
    ftuser = crud.create_ftuser(db, user)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
