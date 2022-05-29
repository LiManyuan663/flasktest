# -*- coding: utf-8 -*-
# @Time    : 2022/5/15 19:20
# @Author  : Manyuan Li
# @Email   : 1551531616@qq.com
# @File    : txt2json.py
# @Software: PyCharm
import os
import json

# 对case的处理
def processCase():
    path= 'case/'
    title=['title','case','result']
    files = os.listdir('case/')
    for file in files:
        if file.endswith('txt'):
            with open(path+file, 'r', encoding='utf-8') as f:
                js={}
                for i in range(3):
                    content=f.readline()
                    js[title[i]]=content
                    print(content)
                f.close()
            with open(path+file,'w',encoding='utf-8') as f:
                json.dump(js, f)

# 对document的处理
def processDoc():
    path = 'document/'
    title=['title1','title2','title3','content']
    files = os.listdir(path)
    for file in files:
        if file.endswith('txt'):
            with open(path+file,'r',encoding='utf-8') as f:
                js = {}
                for i in range(3):
                    content = f.readline()
                    js[title[i]] = content
                    print(content)
                js[title[3]] = "".join(f.readlines())
            with open(path + file, 'w', encoding='utf-8') as f:
                json.dump(js, f)

# for file in files:
#     with open(path + file, 'r', encoding='utf-8') as f:
#         content = json.load(f)
#         print(content)

processDoc()