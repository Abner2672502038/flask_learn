"""
@program: flask_learn
@author: Abner
@create: 2021-11-22 22:49
@descriptions: 使用WSGI 创建静态资源服务器
"""

import os
from wsgiref.simple_server import make_server


"""
服务协议
SERVER_PROTOCOL   HTTP/1.1 
服务软件
SERVER_SOFTWARE   WSGIServer/0.2
请求方法
REQUEST_METHOD   GET
资源路径
PATH_INFO   /
请求参数
QUERY_STRING   
客户端地址
REMOTE_ADDR   127.0.0.1
资源类型
CONTENT_TYPE   text/plain
HTTP_HOST   127.0.0.1:8000
多线程和多进程的
wsgi.multithread   True
wsgi.multiprocess   False
"""
def app(env,make_response):

    # 查看env中的数据
    # for k,v in env.items():
    #     print(k,' ',v)

    #设置响应头
    # make_response('200 OK',[('Content-Type','text/html;charset=utf-8')])
    # 返回数据
    # return ['<h4>hello,wsgl,访问静态资源服务器</h4>'.encode("utf-8")]

    # 访问静态资源
    headers=[]
    body=[]
    static_path=env.get('PATH_INFO')
    # 静态资源目录
    static_dir='static_resourse'
    print(static_path)
    # 资源路径查找
    if static_path=='/favicon.ico':
        res_path=os.path.join(static_dir,'image/music-icon.png')
        headers.append(('Content-type','images/*'))
    elif static_path=='/':
        res_path=os.path.join(static_dir,'home/index.html')
        headers.append(('Content-type','text/html;charset=utf-8'))
    else:
        # css/js/image/mp4
        # 分割路径 /js/.... /css/.. /mp4/...
        res_path=os.path.join(static_dir,static_path[1:])
        if res_path.endswith('.html'):
            headers.append(('Content-type','text/html;charset=utf-8'))
        elif any((res_path.endswith('.jpg'),res_path.endswith('.png'),res_path.endswith('.gif'))):
            headers.append(('Content-type','images/*'))
        else:
            # css,js
            headers.append(('Content-Type','text/*;charset=utf-8'))

#     判断资源是否存在
    status_code=200
    if not os.path.exists(res_path):
        status_code=404
        # headers.append(('Content-Type','text/html;charset=utf-8'))
        body.append('<h3 style="color:red">404,访问资源不存在</h3>'.encode("utf-8"))
    else:
        # 打开文件
        with open(res_path,'rb') as file:
            body.append(file.read())

    make_response('%s OK' % status_code,headers)

    return body

host='127.0.0.1'
port=8000
# 生成web应用服务进程
httpd=make_server(host,port,app)
print("running http://%s:%s" % (host,port))
# 启动服务，监听客户端连接
httpd.serve_forever()