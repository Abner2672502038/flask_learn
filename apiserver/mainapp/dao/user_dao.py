# _*_ coding: utf-8 _*_
"""
@Time : 2022/2/21 13:55
@Author : 薛定谔的余项
@Description : 
"""
import hashlib

from mainapp.dao import BaseDao


class UserDao(BaseDao):
    # 登录
    def login(self,username,pwd):
        password=hashlib.md5(pwd.encode('utf-8')).hexdigest()
        res=super().findAll('userinfo'," where username=%s and password=%s",username,password)
        if res:
            return res[0]
        return None

    def save(self,**data):
        # 验证外部数据的完整性
        data['password'] = hashlib.md5((data['password']).encode('utf-8')).hexdigest()
        return super().save('userinfo',**data)

    def update(self,**data):
        if not data['id']:
            return False
        id=data.pop('id')
        if  data.get('password'):
            data['password']= hashlib.md5((data['password']).encode('utf-8')).hexdigest()
        return super().update('userinfo',id,**data)


if __name__ == '__main__':
    dao=UserDao()
    user=dao.login('frank','1234')
    print(user)
    # user=dict(id=6,number=6224246666)
    # flag=dao.update(**user)
    # print(flag)





