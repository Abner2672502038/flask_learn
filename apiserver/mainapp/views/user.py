"""
@program: flask_learn
@author: Abner
@create: 2021-11-24 20:06
"""
# 使用blueprint插件拆分视图函数
import hashlib
from datetime import datetime

from flask import Blueprint
from flask import request, Response, session
from flask_session import Session
from flask import render_template, make_response, redirect

from mainapp.dao.user_dao import UserDao

blue = Blueprint('user', __name__, url_prefix='/user')

'''
登录控制器
'''


@blue.route('/login', methods=['GET', 'POST'])
def login():
    # response=make_response('登录成功')
    # response.set_cookie('username','Abner',max_age=3600,domain='127.0.0.1')
    # return response
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not all((username, password)):
            message = '用户名或密码不能为空'
        else:
            # 数据与数据库对比
            dao = UserDao()
            # print(username,password)
            user = dao.login(username, password)
            # print(user)
            if not user:
                message = "暂无 %s 用户，用户名或密码错误" % username
            else:
                # session = Session()
                session['login_user'] = user
                session['test'] = 'session depends on cookies'
                # 重定向到主页
                return redirect('/', 302)

    context = locals()
    return render_template('user/user_login.html', **context)


'''
登出操作
'''


@blue.route("/logout", methods=['GET'])
def logout():
    # session=Session()
    del session['login_user']
    return redirect('/user/login')


@blue.route('/find', methods=['GET'])
def find():
    response = Response('查找成功', 200)
    username = request.cookies.get('username')
    print('username=%s' % username)
    # response.delete_cookie('username',domain='127.0.0.1')
    return response


@blue.route('/user', methods=['GET', 'POST'])
def user():
    # session=Session()
    # 验证用户是否登录成功
    if not session.get('login_user'):
        return "当前没有登录，请先<a href='/user/login'>登录</a>"
    print('url', request.url)
    print('base_url', request.base_url)
    print('host_url', request.host_url)
    print('path', request.path)
    # 渲染界面
    # 从session中获取当前用户
    # print(session)
    name = session.get('login_user').get('username')
    return render_template('user_list.html', request=request, nick_name=name)


@blue.route('/deluser', methods=['GET'])
def del_user():
    del_id = request.args.get('id')
    return "<h3>delete user id=%s" % del_id

@blue.route('/listuser',methods=['GET'])
def listUser():

    data={
        "message":"hello,template",
        "age":20,
        "time":datetime.now(),
        "list":["财务总监","技术总监","销售总监","财务总监","董事长"],
        "file":1122433,
        "money":18999345623.456345
    }
    return render_template("user/list.html",**data)


@blue.route("/list",methods=['GET'])
def list():
    del session["menus"]
    if not session.get("menus"):
        session['menus']=[
            {"title":'用户管理','url':"/user/list"},
            {"title":"银行管理",'url':'/bank/list2'},
            {"title":'银行卡管理','url':'/card/list2'}
        ]

    # dao=UserDao()
    from  models import Userinfo
    print("-------------------------------------------")
    for item in Userinfo.query.all():
        print(item.id)
    data={
        # "users":dao.list(),
        "users":Userinfo.query.all(),
        "session":session
    }
    return render_template("user/list2.html",**data)

# flask_session插件
# pip install flask_session -i http://mirrors.aliyun.com/pypi/simple
# pip install redis
