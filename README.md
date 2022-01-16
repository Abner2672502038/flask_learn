### pycharm上传项目 
问题1：invalid authentication data 404 not found  
解决方案：使用token登录  
share project on github
### Flask框架学习
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

