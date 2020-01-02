#-*- coding:utf-8 -*-
import os

#치료를 목적으로 주어진 파일을 삭제한다.
def CureDelete(fname):
        return os.remove(fname)
