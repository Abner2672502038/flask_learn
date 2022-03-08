"""
@program: flask_learn
@author: Abner
@create: 2021-11-24 15:45
"""
import math
from datetime import datetime

from flask import Flask, render_template

import settings

app=Flask(__name__,static_folder='static',static_url_path='/s')
# 配置session的秘钥
# app.secret_key='1234566frtwhtn@'
# 从指定的服务中加载Flask服务的配置
app.config.from_object(settings.Dev)


# 使用flask_session插件
from flask_session import Session
session=Session()
session.init_app(app)


# 初始化数据库sqlalchemy
from  models import db
db.init_app(app)


# 自定义日期过滤器
@app.template_filter("dateformat")
def dateformat_filter(value,*args):
    # print(value,type(value)) type(value):datetime
    return value.strftime(*args)

# 金钱过滤器
@app.template_filter("moneyformat")
def money_filter(value,method='common',precision=0):
    # precision:保留几位小数
    # 普通金额的格式化
    value=round(value,precision)
    if method=='common':
        if isinstance(value,int):
            pre_v=str(value)
            end_v=''
        else:
            pre_v,end_v=str(value).split(".")
            end_v='.'+end_v
        #  反转
        pre_v=pre_v[::-1]
        vs=[pre_v[i*3:i*3+3] for i in range(math.ceil(len(pre_v)/3))]
        return ','.join(vs)[::-1]+end_v
    # currency 货币单位
    cur=''
    if value/10000<1:
        cur='元'
    elif value/10*10000<1:
        cur='万元'
        value=round(value/1000,2)
    elif value/100*10000<1:
        cur='十万'
        value=round(value/(10*10000),2)
    elif value / 1000 * 10000 < 1:
        cur = '百万万'
        value = round(value / (100* 10000), 2)
    elif value/10000*10000<1:
        cur='千万'
        value = round(value / (1000* 10000), 2)
    else:
        cur='亿'
        value = round(value / (10000* 10000), 2)
    return str(value)+cur








@app.errorhandler(404)
def notFound(error):
    print(error)
    return render_template('404.html')

@app.errorhandler(Exception)
def servererror(error):
    return render_template('500.html')
