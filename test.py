# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 20:28
# @Author  : Manyuan Li
# @Email   : 1551531616@qq.com
# @File    : test.py
# @Software: PyCharm
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]