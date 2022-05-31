# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 文本语义相似度计算和文本匹配搜索
"""
import sys
import os
import json
import random

sys.path.append('..')
from similarities import Similarity

# 1.Compute cosine similarity between two sentences.
sentences = ['花呗的绑定的卡怎么改']
corpus = [
    '花呗更改绑定银行卡',
    '我什么时候开通了花呗',
    '俄罗斯警告乌克兰反对欧盟协议',
    '暴风雨掩埋了东北部；新泽西16英寸的降雪',
    '中央情报局局长访问以色列叙利亚会谈',
    '人在巴基斯坦基地的炸弹袭击中丧生',
]
documents = []
case = []
# dpath = './data/document' # 运行当前脚本
dpath = 'examples/data/document'  # 运行app.py
# cpath = './data/case'
cpath = 'examples/data/case'
dfiles = os.listdir(dpath)
cfiles = os.listdir(cpath)
for file in dfiles:
    with open(dpath + '/' + file, 'r', encoding='utf-8') as f:
        content = json.load(f)
        documents.append(content)

for file in cfiles:
    with open(cpath + '/' + file, 'r', encoding='utf-8') as f:
        content = json.load(f)
        case.append(content)


def selectSim(input):
    print("开始加载模型了")
    model = Similarity(model_name_or_path="shibing624/text2vec-base-chinese")
    list1 = []
    for item in documents:
        list1.append(item['content'])
    model.add_corpus(list1)
    print("开始寻找文书")
    res1 = model.most_similar(queries=input, topn=5)
    # print(res)
    result = {}
    result1 = []
    for q_id, c in res1.items():
        print('query:', input[q_id])
        print("search top 3:")
        for corpus_id, s in c.items():
            # print(f'\t{model.corpus[corpus_id]}: {s:.4f}')
            print(corpus_id)
            result1.append({'text': documents[corpus_id], 'rate': ('%.2f' % s)})

    result['document'] = result1

    model.corpus = {}
    model.corpus_ids_map = {}
    model.corpus_embeddings = []
    list2 = []
    for item in case:
        list2.append(item['case'])
    model.add_corpus(list2)
    print("开始寻找案例")
    res2 = model.most_similar(queries=input, topn=10)
    # print(res)
    result2 = []
    for q_id, c in res2.items():
        # print('query:', input[q_id])
        # print("search top 10:")
        for corpus_id, s in c.items():
            # print(f'\t{case[corpus_id]}: {s:.4f}')
            print(corpus_id)
            result2.append({'text': case[corpus_id], 'rate': ('%.2f' % s)})

    result['case'] = result2
    print("匹配结束")
    return result


def selectSim2(input):
    print("虚假的筛选")
    result = {}
    # 5个文书
    result1 = []
    result2 = []
    ran1 = random.sample(range(0, 13), 5)
    print(ran1)
    rate1 = sorted(random.sample(range(30, 60), 5))
    rate1.reverse()
    print(rate1)
    # print(type(rate1))
    for i in range(5):
        result1.append({'rate': rate1[i], 'text':documents[ran1[i]]})
    result['document'] = result1
    # 10个案例
    ran2 = random.sample(range(0,26),10)
    rate2 = sorted(random.sample(range(30,60),10))
    rate2.reverse()
    for i in range(10):
        result2.append(({'rate':rate2[i],'text':case[ran2[i]]}))
    result['case'] = result2
    print(result)
    return result


if __name__ == '__main__':
    selectSim2(sentences)
