"""
@program: flask_learn
@author: Abner
@create: 2021-11-25 22:50
"""
from mainapp.dao import BaseDao


class BankDao(BaseDao):
    def findAll(self, table, where=None, *whereArgs):
        return super().findAll(table, where, *whereArgs)







if __name__ == '__main__':
    bankDao = BankDao()
    # res = bankDao.findAll("bank")
    # print(res)
    res=bankDao.list("bank")
    print(res)
