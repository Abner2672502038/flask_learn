# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/4 14:41
@Author : 薛定谔的余项
@Description : 
"""
from unittest import TestCase
from mainapp import app
from models import db, Userinfo,Bank,Card
from utils import encrypt

class TestOrm(TestCase):

    # C 增加
    def test_create(self):
        # 添加应用环境
        app.app_context().push()

        user=Userinfo()
        user.username="python"
        user.password=encrypt.md5("1111")
        user.number="622424199807"
        db.session.add(user)
        # 提交事务
        db.session.commit()

    # U 更新
    def test_update(self):
        app.app_context().push()

        user=Userinfo.query.get(1)
        print(user)
        user.number="1234567890"
        db.session.commit()

    # D 删除
    def test_delete(self):
        app.app_context().push()

        db.session.delete(Userinfo.query.get(7))
        db.session.commit()

    def test_read(self):
        app.app_context().push()
        bank=Bank.query.filter(Bank.bankname=="甘肃银行").all()
        print(bank)

        print("----------------------拿到查询结果一个-----------------------------")
        filter= Userinfo.query.filter(Userinfo.username=='rose',Userinfo.password==encrypt.md5('1234'))
        try:
            user=filter.one()
            print(user)
        except:
            print("密码或用户名错误")

        print("----------------------查询username中包含f的用户-----------------------------")
        # for u in Userinfo.query.filter(Userinfo.username.contains("f")):
        #     print(u)

        for u in Userinfo.query.filter(Userinfo.username.like("%f%")):
            print(u)

        print("----------------------查询username中包含以l结尾的用户-----------------------------")

        for u in Userinfo.query.filter(Userinfo.username.endswith("l")):
            print(u)

        print("----------------------查询Bank中id大于等于10，bankname包含业字的银行-----------------------------")
        for b in Bank.query.filter(db.or_(Bank.id.__ge__(10),Bank.bankname.contains("业"))):
            print(b)

        print("----------------------查询Bank中id大于等于10，bankname不包含业字的银行-----------------------------")
        for b in Bank.query.filter(db.or_(Bank.id.__ge__(10),db.not_(Bank.bankname.contains("业")))):
            print(b)

        print("----------------------查询Card中，money大于5000的用户-----------------------------")
        for c in Card.query.filter(Card.money.__ge__(":m")).params(m=5000):
            print(c.username,c.bankname)

    def test_models_session(self):
        app.app_context().push()
        #  模型查询Userinfo.query的类型是<class 'flask_sqlalchemy.BaseQuery'>是一个对象
        users=Userinfo.query.all()
        # 结果集 list[<class 'models.Userinfo'>]
        print(type(users[0]))

        # session查询query中有查询条件，session查询的结果集为list[()], NamedTuple
        user2=db.session.query(Userinfo.username,Userinfo.number).all()
        print(type(user2[0]))

    def pages(self, query_set, page_size, page=1):

        total = query_set.count()
        total_page = total // page_size + (1 if total % page_size > 0 else 0)
        print("------------------第 %s 页/共%s页--------------------"% (page,total_page))
        return query_set.offset((page - 1) * page_size).limit(page_size).all()


    #   分页查询
    def test_page(self):

        app.app_context().push()
        # 总共的记录数
        # tcnt= db.session.query(Userinfo).count()
        # page_size=4
        # total_page=tcnt//page_size + (1 if tcnt % page_size>0 else 0)
        # page=3
        # users=db.session.query(Userinfo.username,Userinfo.number).offset((page-1)*page_size).limit(page_size).all()
        users=self.pages(db.session.query(Userinfo),page_size=3,page=2)
        for u in users:
            print(u.username,u.number)


    def   test_aggregation_work(self):
        app.app_context().push()

        query_set=db.session.query(Card.bank_id,\
                                   db.func.min(Card.money).label("min_money"),
                                   db.func.max(Card.money).label("max_money"),
                                   db.func.sum(Card.money).label("wealth")).group_by(Card.bank_id).order_by(db.Column("wealth").desc()).all()

        # query_list=[(Bank.query.get(bank_id),wealth)for bank_id,wealth in query_set]
        print("--------------每个银行的存款的总数，每个银行的存款的最大值和最小值------------------")
        for c in query_set:
            print(Bank.query.get(c.bank_id).bankname,c.wealth,c.min_money,c.max_money)
            for u_id,money in db.session.query(Card.user_id,Card.money).filter(Card.bank_id==c.bank_id,db.or_(Card.money==c.min_money,Card.money==c.max_money)):
                print(Userinfo.query.get(u_id).username,money)



































