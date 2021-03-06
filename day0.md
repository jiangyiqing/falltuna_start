## 为什么需要后台服务?
用户发请求需要结果, 后台服务处理用户请求, 返回结果. 所以需要后台服务.
## 后台服务能做什么?

你所见页面, 来自于后台服务返回的数据
- 如打开网页发送请求, 去哪个网站, 具体哪个页面, 根据你发送的请求, 后台服务器将数据返回给浏览器, 得到如你所见的网页
## 怎么工作?
后台服务器与用户互动. 
对用户而言, 分2步:
- 1:告诉服务器你想要什么(request),
`如询问“明天天气如何”, 用户发送请求, {city=..., date=...}`
- 2你收到服务器的回复(response)
`用户收到来自后台服务的返回结果: 上海明天是晴天.`
对服务器而言, 3步: 
  - 1服务器处理请求(收),
`(明天)(上海)天气如何 参数: {城市=上海, 日期=明天}`
  - 2处理请求(处理),
`根据(明天),(上海)查找天气数据, 得到结果{晴天}`
  - 3把结果返回用户(发)
`把数据结果发回用户,{晴天}`
## 后台服务需要有什么功能?
- 至少包括3部分
  - 获取用户请求, 转化成数据
  - 处理用户的请求, 存储/查找
  - 把处理结果返回给用户
### 请求数据
* 请求的类型:
    - 查询/下载数据 (查询条件)
    - 填写表单 (接收表单数据)
    - 上传图片/视频/音频 (接收文件)

### 处理数据
* 处理的功能:
    - 存储表单数据
    - 存储文件
    - 根据查询请求查找数据/文件
    - 向其他服务器发送请求, 获得数据

### 响应请求
* 响应的方式:
    - 把数据发给用户
    - 把媒体文件发给用户
## Fast API 是什么?

[FastAPI](https://fastapi.tiangolo.com/zh/)是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 3.6+ 并基于标准的 Python 类型提示。
## 关于本教程
本教程是一个快速入门教程, 帮助初学者使用FastAPI搭建后台服务.
## 配置环境
见[prereq.md](./prereq.md)
## 每日目标
* Day1
1. 最基本的服务, 接收请求, 查询, 提交表单, 上传媒体文件
2. 响应用户的请求, 返回数据/媒体文件
* Day2
1. 向其他网站发送请求
2. 使用数据库
* Day3
1. 优化项目结构
2. 追踪、修正bug, log系统
* Day4
1. 部署系统
2. 版本管理
3. 服务器上、Docker的设置
* Day5~Day7 Vue JS的前端开发(预定)
* Day8开始: 