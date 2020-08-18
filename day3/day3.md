# Day3
Migration
假设table里面要增加一个Column(如昵称、头像)
然而models改了, MySQL的table却没改
所以, Migration就是把models里的数据库修改, 自动同步到MySQL的table里去
比如我加了2个Column (Avatar, Nick)
## Alembic
进入项目目录
`alembic init alembic`
> alembic
同级目录会有: `alembic.ini`
把`sqlalchemy.url`改成 `database.py`的路径
每次升级都会在versions里面
### migration
> alembic revision -m "description:"
创建升级脚本, 版本
> alembic upgrade head
升级数据库, 把版本号写进去
### auto generation
在auto migration时会读env.py
在env.py里加上
```
#: 导入DBBase
from models import DBBase
target_metadata = DBBase.metadata
```
改变类型, 不改变名称, 也让migration自动处理:
在context.configure里加入
```
        compare_type = True,
        compare_server_default = True
```
参见: https://alembic.sqlalchemy.org/en/latest/autogenerate.html
接下来, 运行
```
alembic revision --autogenerate -m "description:"
alembic upgrade head
```
## logging
(setup logger)
在main.py里加上
```
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
```
参见: https://medium.com/@PhilippeGirard5/fastapi-logging-f6237b84ea64