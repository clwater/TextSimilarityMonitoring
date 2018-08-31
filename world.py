# -*- coding: utf-8 -*-

import os
import abstract, cosine

def cleanAbsCache():
    print('clean abstract cache')
    with open('./cache/absCache', 'w') as f:
        f.write('')


def initWorld():
    print('============')

    cleanAbsCache()

    print('initWorld')
    # 获取paper文件夹下面所有的文件名
    filelist = os.listdir('./paper')
    # print filelist[0]
    for file in filelist:
        abstract.getAbsFile(os.path.abspath('./paper/' + file))

    cosine.buildDictionary()

