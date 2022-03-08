# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/6 19:02
@Author : 薛定谔的余项
@Description : sqlalchemy中原生sql查询
"""
from unittest import TestCase
from mainapp import app,db
from models import Userinfo,Bank,Card
from utils import encrypt

class TestRaw(TestCase):

    def test_rawsql(self):
        sql1="select * from userinfo limit 5 "
        sql2="insert into userinfo(username,password,number) values(:username,:pwd,:number)"
        with app.app_context():
            res=db.session.execute(sql1)
            print("res类型是：",type(res)) # <class 'sqlalchemy.engine.cursor.CursorResult'>
            print("res.cursor类型",type(res.cursor)) # <class 'pymysql.cursors.Cursor'>
            print(res.fetchall())
            print("------------------添加------------------")
            cursor=db.session.execute(sql2,params={"username":"杨过","pwd":encrypt.md5("476958"),"number":12435465783})
            db.session.commit()
            print(cursor.lastrowid)
            # for item in res.cursor:
            #     print("item类型：",type(item)) # <class 'tuple'>
            #     print(item)

    def test_user_bank(self):
        # 查询用户名、手机号、银行名、银行名、银行地址、银行卡及存款
        sql=" select u.username,b.bankname,b.address,c.number,c.money from userinfo as u join card as c on u.id=c.user_id join bank as b on b.id=c.bank_id order by c.money desc"
        app.app_context().push()
        cursor=db.session.execute(sql)
        print(cursor.fetchall())

    # 连接查询可用多个filter的sqlalchemy的查询替代
    def test_user_bank_sqlalchemy(self):
        app.app_context().push()
        res=db.session.query(Userinfo.username,Userinfo.number,Bank.bankname,Bank.bankname,Card.number,Card.money)\
            .filter(Userinfo.id==Card.user_id)\
            .filter(Card.bank_id==Bank.id)
        for r in res:
            print(r)




