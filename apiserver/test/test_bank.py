# _*_ coding: utf-8 _*_
"""
@Time : 2022/2/11 16:17
@Author : 薛定谔的余项
@Description : 
"""
from unittest import TestCase
import requests


# 声明单元测试类
class TestBank(TestCase):

    # 声明单元测试方法，方法名以test_开头
    def test_publish(self):
        url = "http://localhost:5000/publish"
        resp = requests.post(url)
        self.assertEqual(resp.status_code, 200)
        # 查看响应数据的类型Content-Type
        print(resp.text)
        # 打印响应数据的类型
        print(resp.headers.get('Content-Type'))
