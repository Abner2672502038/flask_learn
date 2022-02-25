"""
@program: flask_learn
@author: Abner
@create: 2021-11-25 20:15
"""
import pymysql


# 获取db对象
db=pymysql.connect(host='localhost',port=3306,user='root', password='Abner',database='pysql')

# 获取cursor对象
cursor=db.cursor()

# 执行sql
cursor.execute('SELECT * FROM pysql.userinfo')

# 获取全部数据
data=cursor.fetchall()

print(list(data))

# 关闭流
cursor.close()
db.close()


