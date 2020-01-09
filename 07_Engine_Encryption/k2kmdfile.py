# -*- coding:utf-8 -*-

import hashlib
import os
import py_compile
import random
import struct
import shutil
import sys
import zlib
import k2rc4
import k2rsa
import k2timelib


#rsa 개인키를 이용해서 주어진 파일을 암호화하ㅕㅇ kmd 파일을 새성
def make(src_fname, debug=False):
    fname = src_fname

    #암호화 대상 파일을 컴파일 또는 복사해서 준비
    if fname.split('.')[1] == 'py':
        py_compile.compile(fname)
        pyc_name = fname+'c'
    else:
        pyc_name = fname.split('.')[0] + '.pyc'
        shutil.copy(fname, pyc_name)


    #simple rsa를 사용하기 위해 공개키 개인키 로딩

    #공개키 로딩
    rsa_pu = k2rsa.read_key('key.pkr')
    #개인키 로딩
    rsa_pr = k2rsa.read_key('key.skr')

    if not (rsa_pr and rsa_pu):
        if debug:
            print 'ERROR : Cannot find the key file!'
        return False

    #kmd 파일 생성

