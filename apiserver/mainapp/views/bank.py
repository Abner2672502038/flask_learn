"""
@program: flask_learn
@author: Abner
@create: 2021-11-24 20:07
"""
from flask import Blueprint, request, render_template, redirect, url_for, abort
from mainapp.dao.bank_dao import BankDao
from flask import jsonify
from flask import make_response
from flask import Response

blue = Blueprint(name='bank', import_name=__name__,url_prefix='/bank')

@blue.route('/add',methods=['GET','POST'])
def applicationaCard():
    if request.method=='POST':
        bank_name=request.form.get('bank')
        username=request.form.get('username')
        phone=request.form.get('phone')
        if phone=='18846756637':
            # abort(404)
            # abort(Response('<h3 style="color:red">当前手机号不能被登录</h3>',401))
            raise Exception('出现异常',500)
        return redirect(url_for('bank.showCard'))

    return render_template('card/add.html')

@blue.route('/list',methods=['GET'])
def showCard():
    return render_template('card/list.html')

@blue.route('/list2',methods=["GET"])
def list2():
    # dao=BankDao()
    from models import Bank
    data={
        # "banks":dao.findAll("bank")
        "banks":Bank.query.all()
    }
    return render_template("bank/list.html",**data)

@blue.route('/publish', methods=['POST'])
def publishBank():
    data='{"id":101,"name":"李华"}'
    code=200
    return Response(response=data,status=code,content_type='application/json;charset=utf-8')
    # return jsonify(data,code)
    # response=make_response(data,code)
    # response.headers['Content-type']='application/json;charset=utf-8'
    # return response


    # return "预发布银行公告成功",200

@blue.route('/bank', methods=['GET', 'POST'])
def bank():
    bankdao = BankDao()
    # 获取数据
    data = bankdao.findAll("bank")
    # flask自带的json工具
    return jsonify({
        "status": 200,
        "message": "ok",
        "data": data
    })
