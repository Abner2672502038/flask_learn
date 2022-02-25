"""
@program: flask_learn
@author: Abner
@create: 2021-11-25 21:32
"""
import pymysql


user=input("username:")
pwd=input("password:")
# username:' or 1=1 -- (--后面有空格)
# password:12
config={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"Abner",
    "database":"pysql"
}

db=pymysql.connect(**config)
# 结果为字典类型，可以看到列名
cursor=db.cursor(cursor=pymysql.cursors.DictCursor)

# sql注入
# sql="select * from userinfo where username='%s' and password='%s' "%(user,pwd)
# select * from userinfo where username='' or 1=1 -- ' and password='12'

# 解决方法就是将变量或者实参直接写到execute中即可
sql="select * from userinfo where username=%s and password=%s"

res=cursor.execute(sql,(user,pwd))
if res:
    print("登录成功")
else:
    print("登录失败")
print(res)

print(cursor.fetchone())

