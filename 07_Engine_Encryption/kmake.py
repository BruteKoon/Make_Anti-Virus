# -*- coding:utf-8 -*-

import os
import sys
import k2kmdfile

if __name__ = '__main__':

    #인자 값 체크
    if len(sys.argv) != 2:
        print 'Usage : kmake.py [python source]'
        exit()
    k2kmdfile.make(sys.argv[1], True)
