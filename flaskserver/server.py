"""
@program: flask_learn
@author: Abner
@create: 2021-11-24 09:35
"""
from flask import Flask
from flask import request,render_template

# 创建Flask对象
# def __init__(self,
#              import_name: str,
#              static_url_path: Optional[str] = None,
#               静态资源文件夹
#              static_folder: Union[str, PathLike, None] = "static",
#              static_host: Optional[str] = None,
#              host_matching: bool = False,
#              subdomain_matching: bool = False,
#               模板文件夹，同一目录下的
#              template_folder: Optional[str] = "templates",
#              instance_path: Optional[str] = None,
#              instance_relative_config: bool = False,
#              root_path: Optional[str] = None) -> Any
app = Flask('flaskserver')


# 设置访问资源路径
@app.route('/home', methods=['GET', 'POST'])
def home():
    request_method = request.method
    # 查询参数
    platform = request.args.get("platform")
    # 转换成,获取get请求查询参数
    if platform.lower() == "pc":
        if request_method == 'GET':
            # get请求处理
            return """
            <h2>登录页面</h2>
            <form action='/home?platform=pc' method='post'>
                <input name='username' placeholder='用户名'><br>
                <input name='password' placeholder='密码'><br>
                <button>提交</button>
            </form>
            """
        else:
            # POST请求处理
            username = request.form.get("username")
            password = request.form.get("password")
            # 去除前后空格
            if all((username.strip() == "admin", password.strip() == "123456")):
                return """
                        <h1 style='color:green'>登录成功</h>
                        """
            else:
                return """
                        <h1 style='color:red'>用户名或密码错误</h1><a href='/home'>点击重试</a>
                     """


@app.route('/addbank',methods=['GET','POST'])
def addBank():
    # 获取数据
    data={
        'title':'绑定',
        'mesage':''
    }

    request_method=request.method

    if request_method=='POST':
        card_name=request.form.get('cardId')
        pwd=request.form.get('pwd')
        # 若不为空
        if all((card_name,pwd)):
            # 打印日志
            app.logger.info('cardID:%s,password:%s'%(card_name,pwd))
            data['mesage']="绑定成功"
            success=render_template('success.html')
            return success

    res=render_template('add_bank.html',**data)
    # 静态资源页面
    # print(res)
    # debug下可以客户端调试
    # raise Exception("无意异常")
    return res






# 启动服务
host = "localhost"
port = 5000
"""
:param options: the options to be forwarded to the underlying Werkzeug
            server. See :func:`werkzeug.serving.run_simple` for more
            information.
            
threaded: bool = False,
 processes: int = 1,
"""
# 开启多线程,多进程和多线程不能同时设置
app.run(host, port,debug=True,threaded=True)
