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
**请求码**  
2--: 客户端与服务器通信建立  
3--：重定向  
4--：客户端请求错误  
5--：服务器请求异常  
**git的配置和github**    
cd ~/.ssh  
ssh-keygen -t rsa -C 'xxx@xxx.com' 生成key  
将key加入到github  




