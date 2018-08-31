# -*- coding: utf-8 -*-

import world, cosine, abstract, serverMain

simValue = 0.3


def setsimValue(value):
    global simValue
    simValue = value


def getsimValue():
    return simValue


def checkText(text):
    absText = abstract.getAbs(text)

    sims = cosine.checkText(absText)
    return sims


def main():
    print('Service Start')

    init()
    server()


def init():
    print('initWorld')
    world.initWorld()


def server():
    print('WebService Start')
    serverMain.initServer()


if __name__ == '__main__':
    main()
