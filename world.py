# -*- coding: utf-8 -*-

import os
import abstract

def initWorld():
    print('============')
    print('initWorld')
    # 获取paper文件夹下面所有的文件名
    filelist = os.listdir('./paper')
    # print filelist[0]
    for file in filelist:
        abstract.getAbs(os.path.abspath('./paper/' + file))


