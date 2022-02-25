# _*_ coding: utf-8 _*_
"""
@Time : 2022/2/10 16:52
@Author : 薛定谔的余项
@Description : 
"""
from flask import Blueprint
# 导入url_for模块
from flask import url_for

# 定义蓝图
blue = Blueprint("card", __name__)


@blue.route("/addCard/<cardname>")
def addCard(cardname):
    return """%s，开户成功</br>
    <a href='%s'>返回首页</a>
    """ % (cardname, url_for('index'))


@blue.route("/selectBank")
def select_bank():
    bankName = "Agriculture Bank of China"
    return '''
    选择银行成功，3秒后跳转到<a href="%s">开户界面</a>
    ''' % url_for('card.addCard', cardname=bankName)
