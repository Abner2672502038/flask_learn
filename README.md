### 一.pycharm上传项目 
问题1：invalid authentication data 404 not found  
解决方案：使用token登录  
share project on github
### 二.WSGI创建web服务器
##### 1. 使用虚拟环境创建项目  
  所谓虚拟环境，就是我们创建项目时，不使用操作系统中安装的Python，而是在项目所在目录下创建一个目录，通常叫venv，然后把系统中安装的Python以及项目依赖包都拷贝到这个venv目录中，本项目以后就使用这个venv。
总结起来就是一句话：每个项目都有自己独立的环境依赖，外部环境变化不会对其造成影响  
  首先是全局安装virtualenv这个包，安装很简单，随便打开一个cmd或者powershell窗口，然后运行pip install virtualenv就可以了。
安装成功之后，需要在cmd中验证一下，运行virtualenv --version即可。
之后，就是进入你的项目目录，运行virtualenv venv命令即可。venv就是虚拟环境的目录，是可以改的，但是我们一般都使用venv。  
##### 2. httpd=>d:daemon 守护进程  
##### 3.使用WSGI创建静态资源服务器  
```
def app(env,make_response):

     查看env中的数据
     for k,v in env.items():
         print(k,' ',v)

    设置响应头
     make_response('200 OK',[('Content-Type','text/html;charset=utf-8')])
     返回数据
     return ['<h4>hello,wsgl,访问静态资源服务器</h4>'.encode("utf-8")]
生成web应用服务进程  
httpd=make_server(host,port,app)  
启动服务，监听客户端连接  
httpd.serve_forever()  
```  
### 三. Flask框架应用
####3.1 安装环境  
(apiserver)> pip install flask -i https://mirrors.aliyun.com/pypi/simple
####3.2 第一个Flask项目
创建服务脚本server.py  
```
from flask import Flask
from flask import request
# 创建Flask对象-httpd WEB服务对象
app=Flask(__name__) #__name__可以是任意的小写字母，表示Flask应用对象的名称

#声明web服务的请求资源(指定资源访问的路由)
#Restful风格指定资源动作，GET:查询，POST:增加、表单 DELETE:删除 PUT:更新 PATCH:批量更新
@app.route('/path',method=['GET','POST','PUT','DELETE','PATCH'])
def path():
    #request是请求对象（HttpRequest）,包含请求路径，请求方法，请求头，表单数据，文件等
    #获取请求中查询参数 QUERY_STRING
    name=request.args.get('username')
    password=request.args.get('password')
    return """
    <h2>用户登录信息</h2>
    <h3>用户名：%s</h3>
    <h3>密码：%s</h3>
    """%(name,password)

#启动flask的web服务器
app.run(host='0.0.0.0',port=5000)
```
注:   
**zip拉链函数:处理请求参数**   
>>a=['Cotent_Type','Request_Method','Connection']  
>>b=['text/html','GET','keep-alive']  
>>list(zip(a,b))  
[('Cotent_Type', 'text/html'), ('Request_Method', 'GET'), ('Connection', 'keep-alive')] 
**请求码**  
2--: 客户端与服务器通信建立  
3--：重定向  
4--：客户端请求错误  
5--：服务器请求异常  
**git的配置和github**    
cd ~/.ssh  
ssh-keygen -t rsa -C 'xxx@xxx.com' 生成key  
将key加入到github  
#### 3.3 路径的反向解析

```
from flask import url_for
from flask import Blueprint

blue=Blueprint('card',__name__)

@blue.route('/add/<bankname>')
def add(bankname):
   ...

@blue.route('/select')
def select():
    return """
    <a href='%s'>点击进入开户界面</a>
    """ % url_for("card.add",bankname="ICBC")
```
url_for("蓝图名.函数名",**kargs):反向解析获取蓝图下的路由注册的路径   
url_for("函数名")：反向解析获取flask的路由注册的路径
>1.TypeError: ‘builtin_function_or_method‘ object is not subscriptable解决办法  
python报“TypeError: ‘builtin_function_or_method’ object is not subscriptable” 这个错，大概率是因为括号用错了（比如应该用圆括号，用成了方括号），或者缺少括号，应检查括号是否使用有误  
>2.Flask框架报错 ValueError: urls must start with a leading slash  
ValueError: url必须以斜杠开头  
>3.usage: manage.py [-?] {test,shell,db,runserver} ... positional arguments错误  
在pycharm运行flask程序时会出现usage: manage.py [-?] {test,shell,db,runserver} … positional arguments错误；  
这里是因为在正常运行的时候，命令行为python manage.py runserver，pycharm是不会帮我们添加runserver。  
#### 3.4 请求对象
```
from flask import request
@blue.route('/user', methods=['GET', 'POST'])
def user():
    print('url',request.url)
    print('base_url',request.base_url)
    print('host_url',request.host_url)
    print('path',request.path)
    # 渲染界面
    return render_template('user_list.html',request=request)
<ul>
        <li>url: {{ request.url }}</li>
        <li>base_url: {{ request.base_url }}</li>
        <li>host_url: {{ request.host_url }}</li>
        <li>path: {{ request.path }}</li>
        <li>method: {{ request.method }}</li>
        <li>heads: {{request.headers}}</li>
        <li>客户端IP: {{request.remote_addr}}</li>
        <li>Cookie:  {{ request.cookies }}</li>

    </ul>
```
请求对象本质上是封装客户端发送的请求数据，在flask中由Werkzeug库(实现python的WSGI库的接口)封装的，包含请求路径(url,base_url,host_url,path),请求方法(大写)，请求参数(查询参数，表单参数)，请求头,Cookies,客户端IP,上传的数据  
 #### 3.5 响应对象response
 在服务端，业务处理完成后，生成响应的数据并封装成响应对象，并传给Python的WSGI,由WSGI向客户端传送数据流  
    1.直接返回文本或响应码
    flask的处理函数如果直接返回文本或附带一个响应状态码，则会自动封装成一个Response对象，且数据类型为 text/html;charset=utf-8  
  ```
@blue.route('/publish', methods=['POST'])
def publishBank():
    # return "预发布银行公告成功",200
  ```
如果返回是一个html文本数据，可以使用render_template()函数，将写好的html模板经过渲染之后生成的html返回
**单元测试类的编写**  
```
from unittest import TestCase
import requests
#声明单元测试类
class TestBank(TestCase):
    # 声明单元测试方法，方法名以test_开头
    def test_publish(self):
        url="http://localhost:5000/publish"
        resp=requests.post(url)
        self.assertEqual(resp.status_code,200)
        # 查看响应数据的类型Content-Type
        print(resp.text)
        # 打印响应数据的类型
        print(resp.headers.get('Content-Type'))

```
*Requirement already satisfied 解决方法*  
对于这样的问题，只需指定安装路径即可 pip install --target=F:\WorkSpace\python\flask_learn\venv\Lib\site-packages  requests,这是由于使用venv，与python环境中冲突导致  
    2.使用make_response(data,code)生成response对象
    通过生成response对象，设置响应头
  ```
    @blue.route('/publish', methods=['POST'])
    def publishBank():
        data='{"id":101,"name":"李华"}'
        code=200
        response=make_response(data,code)
        response.headers['Content-type']='application/json;charset=utf-8'
        return response
  ```
   3.jsonify快速生成json响应对象
   此函数返回一个response对象，只不过response对象的headers已经设置属性Content-Type为application/json
  ```
    @blue.route('/publish', methods=['POST'])
    def publishBank():
        data='{"id":101,"name":"李华"}'
        code=200
        return jsonify(data,code)
  ```

   4.使用Response对象生成响应对象
    
  ```
    @blue.route('/publish', methods=['POST'])
    def publishBank():
        data='{"id":101,"name":"李华"}'
        code=200
        return Response(response=data,status=code,content_type='application/json;charset=utf-8')
  ```
   5.redirect响应对象  
   在一个请求中，由于业务处理的要求，处理业务之后进入新页面，该界面已声明路由，则需要重定向的方式进入到下一页  
   【注意】重定向也是响应对象，必须返回，相当于浏览器或客户端再次发送新的请求
  ```
    @blue.route('/add',methods=['GET','POST'])
    def applicationaCard():
        if request.method=='POST':
            bank_name=request.form.get('bank')
            username=request.form.get('username')
            phone=request.form.get('phone')
    
    
            return redirect(url_for('bank.showCard'))
    
        return render_template('card/add.html')
    
    @blue.route('/list',methods=['GET'])
    def showCard():
        return render_template('card/list.html')
  ```
#### 3.6 请求异常
   在请求处理过程中，验证某一数据出现的错误，可以中断请求。如果请求异常不是请求数据而引起，或者说请求资源不存在，服务器内部异常，此时可以捕获异常  
   ##### 3.6.1 abort()中断
   ```
    @blue.route('/add',methods=['GET','POST'])
    def applicationaCard():
        if request.method=='POST':
            bank_name=request.form.get('bank')
            username=request.form.get('username')
            phone=request.form.get('phone')
            if phone=='18846756637':
                # abort(404)
                # abort(Response('<h3 style="color:red">当前手机号不能被登录</h3>',401))
                raise Exception('')
            return redirect(url_for('bank.showCard'))
    
        return render_template('card/add.html')
   ```
   abort()两种写法：  
    ·abort(status_code)  
    ·abort(Response)  
   ##### 3.6.2 捕获请求异常
   通过相关状态码，获取请求异常，并指定处理函数来响应异常
  ```
    @app.errorhandler(404)
    def notFound(error):
        print(error)
        return render_template('404.html')
    
    @app.errorhandler(Exception)
    def servererror(error):
        return render_template('500.html')

  ```
建议处理异常函数与app对象在同一个脚本中  
如果业务处理中抛出相关异常，则可以指定异常类捕获
### 四、Cookies和Session技术
#### 4.1 Cookie存储技术
1.Cookie数据存储技术,存储在客户端（浏览器），浏览器会为每个站点（host）创建存储空间，Cookie的数据存储以key=value存储，但是每个Key都有生命周期。  
2.一个完整的Cookie信息含：名称、内容、域名、路径（/），有效时间（创建时间，到期时间），查看chrome下的cookie信息：chrome://settings/siteData  
##### 4.1.1 向客户端写入Cookie
使用response对象的set_cookie()方法可以向客户端添加Cookie  
```
# werkzug.wrappers.base_response.BaseResponse
 def set_cookie(
        self,
        key,
        value="",
        max_age=None,
        expires=None,
        path="/",
        domain=None,
        secure=False,
        httponly=False,
        samesite=None,
    ): 

@blue.route('/login',methods=['GET','POST'])
def login():
    response=make_response('登录成功')
    response.set_cookie('username','Abner',max_age=3600,domain='127.0.0.1')
    return response


```
注：localhost和127.0.0.1在存储cookie中不同
##### 4.1.2 从请求对象中获取Cookie
```
@blue.route('/find',methods=['GET'])
def find():
    response=Response('查找成功',200)
    username=request.cookies.get('username')
    print('username=%s'%username)
    # response.delete_cookie('username',domain='127.0.0.1')
    return response
```
#### 4.2 会话Session
1. 会话技术，一般是指客户端与服务端建立的连接，针对Http来说，会话连接称为Session。  
2. 在Http/1.0 版本上，会话是一次性的，请求与响应的一次完整过程基于Session。Http/1.1时，会话是长链接，多个请求和响应共享一个会话。是否为长链接，可以查看响应、请求头的Connection，如果值为keep-alive表示是长链接。因为Session是多个请求的共享资源,所以session存数据时，多个请求可以访问  
3. session的使用场景：用户登录，退出，验证用户，城市定位  
```
@blue.route('/login',methods=['GET','POST'])
def login():
    # response=make_response('登录成功')
    # response.set_cookie('username','Abner',max_age=3600,domain='127.0.0.1')
    # return response
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if not all((username,password)):
            message='用户名或密码不能为空'
        else:
            # 数据与数据库对比
            dao=UserDao()
            # print(username,password)
            user=dao.login(username,password)
            # print(user)
            if not user:
                message="暂无 %s 用户，用户名或密码错误" % username
            else:
                # session = Session()
                session['login_user']=user
                session['test']='session depends on cookies'
                # 重定向到主页
                return redirect('/',302)

    context=locals()
    return render_template('user/user_login.html',**context)
```
locals():将函数内部的变量生成字典对象  
**数据库操作中问题**  
1. %%(%s)s :此种方式，相当于起别名，后面跟key-value字典格式，而且字典的value要与前面对应  
**注:python中对%转义为何是%%，%和\转义有什么区别吗？**  
%占位后，后面得有与之匹配的解释符连接 单独%是不用转义的，如：  
 print('growth rate: %d %%' % 7) >>>growth rate: 7 %   
 print('%') >>>%  
 print('\\%') >>>\\%   
 print('%%') >>>%%
```
>>>demo="%(name)s"%{'name':'abner',"password":'1234'}
>>>demo
'abner'
```
```
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
```
#### 4.3 Flask-Session插件
session解决的是每个客户端中将数据共享在多个请求中，即为每个客户端创建session会话连接。问题是如何判断session是哪个客户端的。Http协议中已经考虑该问题，解决方案是在Cookie中存储一个session_id，当请求发送给服务器时，cookie信息也会带到服务器，服务器以此session_id确定当前的请求是属于哪个session会话的  
**Flask中，默认情况下，session数据存储在内存中（客户端Cookie）。通过flask-session插件，解决将session中数据存储在数据库，文件，或者缓存（redis中）**  
首先安装flask-session插件
```
   pip install flask-session
   pip install redis -i https://mirrors.aliyun.com/pypi/simple
```
配置Flask中的session信息，在settings.py脚本中
```
from redis import Redis
class Dev():
    ENV='developement' # 默认运行环境 production
    SECRET_KEY='1234566frtwhtn@'
    # session中配置redis
    SESSION_TYPE='redis'
    SESSION_REDIS=Redis(host='127.0.0.1',port=6379,db=8)
```
在创建flask脚本中
```
import settings

app=Flask(__name__)
# 配置session的秘钥
# app.secret_key='1234566frtwhtn@'
# 从指定的服务中加载Flask服务的配置
app.config.from_object(settings.Dev)

# 使用flask_session插件
from flask_session import Session
session=Session()
session.init_app(app)
```
session的使用跟之前一样，<font color=red>从flask库中导入session对象即可 </font>
### 四、模板技术与静态资源
#### 4.1 template模板
Flask使用了Jinja2模板技术，支持变量、循环和分支以及自定义标签，支持点"."语法 如：  
*  对象.属性
*  列表.索引下标
*  字典.key  
模板的html文件存放在templates文件夹下，内部可以使用jinja2模板语法，但是html文件必须在view视图函数中通过render_template(".html")渲染  
#### 4.2 静态资源
flask默认情况下静态资源在static目录中，访问路径也是/static,可以创建Flask对象时，指定static_folder和static_url_path两个参数。  
static_folder:静态资源存放的目录  
static_url_path:静态资源的访问路径，若指定为'/s' 针对static目录下的css下的my.css样式，完整的url访问路径：https://127.0.0.1:5000/s/css/my.css  
```
from flask import Flask
app=Flask(__name__,static_folder='static',static_url_path='/s')
```
