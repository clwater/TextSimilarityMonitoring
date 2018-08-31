# -*- coding: utf-8 -*-

from gensim import corpora, models, similarities
from collections import defaultdict
import logging
import main

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


dictionary = None
texts = None
cacheName = []


def getAbs():
    print('getAbs')
    documents = []
    with open('./cache/absCache', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            baseLine = line.split('|||')
            cacheName.append(baseLine[0])
            documents.append(baseLine[1])
    return documents


def buildDictionary():
    print('buildDictionary')
    print('==================================')
    documents = getAbs()
    # 1.分词，去除停用词
    stoplist = set('for a of the and to in'.split())
    global texts
    texts = [[word for word in document.lower().split() if word not in stoplist] for document in
             documents]
    # 2.计算词频
    frequency = defaultdict(int)  # 构建一个字典对象
    # 遍历分词后的结果集，计算每个词出现的频率
    for text in texts:
        for token in text:
            frequency[token] += 1
    # 选择频率大于1的词
    texts = [[token for token in text if frequency[token] > 1] for text in texts]

    # 3.创建字典（单词与编号之间的映射）
    global dictionary
    dictionary = corpora.Dictionary(texts)

    print('buildDictionary success')


def getDictionary():
    return dictionary


def checkText(new_doc):
    # 将文档分词并使用doc2bow方法对每个不同单词的词频进行了统计，并将单词转换为其编号，然后以稀疏向量的形式返回结果
    new_vec = dictionary.doc2bow(new_doc.lower().split())

    # 建立语料库
    # 将每一篇文档转换为向量
    corpus = [dictionary.doc2bow(text) for text in texts]

    # 初始化模型
    # 初始化一个tfidf模型,可以用它来转换向量（词袋整数计数）表示方法为新的表示方法（Tfidf 实数权重）
    tfidf = models.TfidfModel(corpus)

    # 将整个语料库转为tfidf表示方法
    corpus_tfidf = tfidf[corpus]

    # 创建索引
    index = similarities.MatrixSimilarity(corpus_tfidf)

    # 相似度计算
    new_vec_tfidf = tfidf[new_vec]  # 将要比较文档转换为tfidf表示方法

    # 计算要比较的文档与语料库中每篇文档的相似度
    sims = index[new_vec_tfidf]

    simsD = {}
    index = 0
    simValue = main.getsimValue()
    while index < len(sims):
        if sims[index] >= simValue:
            simsD.setdefault(cacheName[index], sims[index])
        index = index + 1

    print(simsD)
    sortlist = sorted(dict2list(simsD), key=lambda x: x[1], reverse=True)

    print(sortlist)

    return sortlist


def dict2list(dic: dict):
    ''' 将字典转化为列表 '''
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst
