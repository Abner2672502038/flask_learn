# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/2 12:52
@Author : 薛定谔的余项
@Description : 
"""

from mainapp.dao import BaseDao


class CardDao(BaseDao):
    def list(self):
        sql="select c.id,c.number,c.money,u.username, b.bankname " \
            "from card c ,userinfo u,bank b " \
            "where c.user_id=u.id and c.bank_id=b.id"

        with self.db as  c:
            c.execute(sql)
            data=list(c.fetchall())

        return data

if __name__ == '__main__':
    dao=CardDao()
    print(dao.list())


