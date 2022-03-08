# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/2 19:38
@Author : 薛定谔的余项
@Description : 
"""

from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()


class Userinfo(db.Model):
    id=db.Column(type_=db.Integer,primary_key=True,autoincrement=True,nullable=False)
    username=db.Column(db.String(10),nullable=False)
    password=db.Column(db.String(100),nullable=False)
    number=db.Column(db.String(18))

    def __str__(self):
        return "%s %s"%(self.username,self.number)


class Bank(db.Model):
    id=db.Column(db.Integer,nullable=False,primary_key=True,autoincrement=True)
    bankname=db.Column(db.String(50))
    address=db.Column(db.String(200),nullable=False)

    def __str__(self):
        return "%s  %s"%(self.bankname,self.address)



class Card(db.Model):
    id=db.Column(db.Integer,nullable=False,primary_key=True,autoincrement=True)
    number=db.Column(db.String(20),unique=True,)
    money=db.Column(db.Float,default=0,server_default='0')
    passwd=db.Column(db.String(100))

    # 模型关系,添加外键约束。设置关系
    user_id = db.Column(db.Integer,db.ForeignKey("userinfo.id"))
    # user=db.relationship(Userinfo)
    # 反向引用
    # 不使用懒加载时，使用连接查询left outer join
    user=db.relationship(Userinfo,backref=db.backref("cards",lazy=False))
    bank_id = db.Column(db.Integer,db.ForeignKey("bank.id"))
    # bank=db.relationship(Bank)
    bank=db.relationship(Bank,backref="cards")
    # # 定义装饰器
    # @property
    # def username(self):
    #     return Userinfo.query.filter(Userinfo.id==self.user_id).all()[0].username
    #
    # @property
    # def bankname(self):
    #     return Bank.query.filter(Bank.id==self.bank_id).all()[0].bankname



