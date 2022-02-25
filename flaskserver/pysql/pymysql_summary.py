"""
@program: flask_learn
@author: Abner
@create: 2021-11-25 21:15
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
cursor=db.cursor()
# sql="insert into userinfo(username,password) values ('abner','1234')"
sql="insert into userinfo(username,password) values (%s,%s)"
cursor.execute(sql,('linda','4567'))
db.commit()
cursor.close()
db.close()


