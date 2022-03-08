"""
@program: flask_learn
@author: Abner
@create: 2021-11-24 15:50
"""
from mainapp import app
from mainapp.views import user
from flask_script import Manager
from mainapp.views import bank
from mainapp.views import card
from flask import url_for, render_template
# 解决跨域请求
from flask_cors import CORS

@app.route("/")
def index():
    # return """
    # <ul>
    #     <li><a href='%s'>银行开户</a></li>
    #     <li><a href='%s'>银行管理</a></li>
    #     <li><a href='%s'>用户管理</a></li>
    # </ul>
    # """% (url_for('card.addCard',cardname="Industrial and Commercial Bank of China"),url_for('bank.bank'),url_for('user.user'))
    data={
        "menus":["财务管理","课程管理","人力管理","工程管理","人力管理"]
    }
    return render_template("index.html",**data)

if __name__ == '__main__':
    CORS().__init__(app)
    # 把blueprint注册到app
    app.register_blueprint(user.blue)
    app.register_blueprint(bank.blue)
    app.register_blueprint(card.blue)
    manager=Manager(app)
    manager.run()
