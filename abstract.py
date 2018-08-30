# -*- coding: utf-8 -*-

import os

from textrank4zh import TextRank4Keyword, TextRank4Sentence


def getAbs(woldFile):
    print('woldFile path:  ' + woldFile)
    with open(woldFile, 'r') as f:
        text = f.read()
        # print (sequence)
        tr4w = TextRank4Keyword()
        tr4w.analyze(text=text, lower=True,
                     window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=text, lower=True, source='all_filters')
        print('摘要：')
        # item = tr4s[0]
        # print(item.index, item.weight, item.sentence)
        # for item in tr4s.get_key_sentences(num=1):
        #     print(item.index, item.weight)
        #     print(item.sentence)

        item = tr4s.get_key_sentences(num=1)
        print(item.index, item.weight)
        print(item.sentence)
