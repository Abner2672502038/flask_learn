# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/7 12:47
@Author : 薛定谔的余项
@Description : 
"""
from unittest import TestCase
from mainapp import app,db
from models import Userinfo,Card,Bank

class TestRelationship(TestCase):
    def test_models(self):
        app.app_context().push()
        # 直接查询，不用filter()
        app.logger.info("----------------------日志测试----------------------")
        for card in Card.query.all():
            print(card.user.username,card.user.number,card.bank.bankname,card.number,card.money)

    # 反向引用
    def test_backref(self):
        app.app_context().push()
        user=Userinfo.query.get(1)
        print(user.username)
        for card in user.cards:
            print(card.number,card.money,card.bank.bankname)



