运行实时服务器：
```code
cd app
uvicorn main:app --reload
```
运行Test可以直接在test.http里发送request
今天要学会的是
## 使用FastAPI
### 处理请求
接收并处理GET请求
接收POST请求 (JSON以及表单)
接收上传的媒体文件, 并保存在服务器上
### 响应请求
返回Json数据给前端请求
媒体文件下载
## 使用Postman或REST Client VScode插件测试API

参考文档:
[FastAPI](https://fastapi.tiangolo.com/zh/)

