"""
@program: flask_learn
@author: Abner
@create: 2021-11-24 15:46
"""
import hashlib

import pymysql
from pymysql.cursors import DictCursor

config = {

    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "Abner",
    "database": "pysql",
    "cursorclass": DictCursor
}


class DB:
    def __init__(self):
        self.db = pymysql.connect(**config)

    def __enter__(self):
        return self.db.cursor()

    # 出异常时
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.db.rollback()
        else:
            self.db.commit()

    def close(self):
        if self.db:
            self.db.close()
            self.db = None


class BaseDao:
    def __init__(self):
        self.db = DB()

    def findAll(self, table, where=None, *whereArgs):


        sql="select * from %s" % table
        if where:
            sql+=where

        with self.db as cursor:
            cursor.execute(sql,whereArgs)
            data=list(cursor.fetchall())

        return data

    def save(self,table,**data):
        sql="insert into %s(%s) values (%s)"
        col_name=','.join([k for k in data])
        col_placeholders=','.join(['%%(%s)s' % key for key in data])
        # print(col_placeholders)
        with self.db as c:
            # str=sql %(table,col_name,col_placeholders)
            # print(str)
            # print(data)
            c.execute(sql %(table,col_name,col_placeholders),data)
            if c.rowcount>0:
                return True
        return False

    def update(self,table,id,**data):
        sql="update %s set %s where id=%s"
        col_name=','.join(['%s=%%(%s)s'% (key,key) for key in data])
        with self.db as c:
            c.execute(sql % (table,col_name,id),data)
            if c.rowcount>0:
                return True
        return False





if __name__ == '__main__':
    dao=BaseDao()
    pwd=hashlib.md5(('1234').encode('utf-8')).hexdigest()
    # user=dao.findAll('userinfo'," where username=%s and password=%s",'frank',pwd)
    # user=dict(username='dl',password='12345')
    # user['password']=hashlib.md5((user['password']).encode('utf-8')).hexdigest()
    # flag=dao.save('userinfo',**user)
    # print(flag)
    user=dao.findAll('userinfo')
    print(user)




