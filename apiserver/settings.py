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


class Product():
    ENV = 'production'  # 默认运行环境 production
    SECRET_KEY = '1ewwarhfrtwhtn@'

