"""
@program: flask_learn
@author: Abner
@create: 2021-11-25 22:01
"""
import pymysql

config={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"Abner",
    "database":"pysql"
}
db=pymysql.connect(**config)

with db.cursor(pymysql.cursors.DictCursor) as cursor:
    # 执行业务逻辑
    sql="select * from userinfo"
    res=cursor.execute(sql)
    print(res)
    cursor.scroll(2,mode='relative')
    data=cursor.fetchone()
    print(data)
    cursor.close()
db.close()

