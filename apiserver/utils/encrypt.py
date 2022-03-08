# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/4 15:28
@Author : 薛定谔的余项
@Description : 
"""
import hashlib


def md5(txt):
        # return hashlib.md5(txt.encode("utf-8")).hexdigest()
    hash_=hashlib.md5()
    hash_.update(txt.encode("utf-8"))
    return hash_.hexdigest()
