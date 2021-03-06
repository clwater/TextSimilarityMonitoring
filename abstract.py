# -*- coding: utf-8 -*-

import os

from textrank4zh import TextRank4Keyword, TextRank4Sentence


def getAbs(text):
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=text, lower=True,
                 window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')
    absText = ''
    for item in tr4s.get_key_sentences(num=1):
        absText = item.sentence
    return absText


def getAbsFile(woldFile):
    try:
        with open(woldFile, 'r') as f:
            text = f.read()
            absText = getAbs(text)
            with open('./cache/absCache', 'a') as f:
                f.write(woldFile + ' ||| ' + absText + '\n')
            print(woldFile + 'build abstract success')
    except:
        print(woldFile + 'build abstract error')
