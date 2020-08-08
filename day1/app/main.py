# -*- coding: utf-8 -*-
from typing import Optional
from fastapi import FastAPI, Body, Form, UploadFile, File, Response
from fastapi.responses import FileResponse
import uvicorn


#:在这里建立了API
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


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
async def qreqf(skip: int = 0, limit: int = 10):
    '''
    GET Query Param
    从上面的fake_items_db中返回第skip个开始到limit个项, 用于查询数据等
    '''
    return fake_items_db[skip: skip + limit]


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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
