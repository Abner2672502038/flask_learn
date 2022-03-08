# _*_ coding: utf-8 _*_
"""
@Time : 2022/2/22 9:15
@Author : 薛定谔的余项
@Description : 
"""
from redis import Redis
class Dev():
    ENV='developement' # 默认运行环境 production
    SECRET_KEY='1234566frtwhtn@'
    # session中配置redis
    SESSION_TYPE='redis'
    SESSION_REDIS=Redis(host='127.0.0.1',port=6379,db=8)
    # 不可用
    # STATIC_FOLDER='static'
    # STATIC_URL_PATH='/s'

    # sqlalchemy的配置 mysql+pymysql://user:password@ip:port/库
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:Abner@127.0.0.1:3306/pysql"
    SQLALCHEMY_TRACK_MODIFICATIONS=True # 可扩展
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True  # 回收资源时自动提交事务
    SQLALCHEMY_ECHO=True # 显示调试SQL



class Product():
    ENV = 'production'  # 默认运行环境 production
    SECRET_KEY = '1ewwarhfrtwhtn@'

