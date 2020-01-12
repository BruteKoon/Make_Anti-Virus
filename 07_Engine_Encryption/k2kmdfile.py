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
    kmd_data = 'KAVM'

    #현재 날짜와 시간을 구한다.
    ret_date = k2timelib.get_now_date()
    ret_time = k2timelib.get_now_time()

    #날짜와 시간 값을 2바이트로 변경한다
    val_date = struct.pack('<H', ret_date)
    val_time = struct.pack('<H', ret_time)

    reserved_buf = val_date + val_time + (chr(0) * 28)

    #날짜와 시간 값이 포함된 예약 영역을 만들어 추가한다.
    kmd_data += reserved_buf

    random.seed()

    while 1:
        tmp_kmd_data = '' #임시 본문 데이터
        
        #rc4 알고리즘에 사용할 128bit 랜덤키 생성
        key = ''

        for i in range(16):
            key += chr(random.randint(0, 0xff))

        #생성된 rc4 키를 암호화 한다.
        e_key = k2rsa.crypt(key, rsa_pr) #개인키로 암호화
        if len(e_key) != 32:
            continue

        #암호화된 rc4키를 복호화 한다.
        d_key = k2rsa.crypt(e_key, rsa_pu) #공개키로 복호화

        #생성된  rc4키가 문제없음을 확인한다.
        if key == d_key and len(key) == len(d_key):
            #개인키로 암호화된 rc4 키를 임시 버퍼에 추가한다.
            tmp_kmd_data += e_key

            #생성된 pyc 파일 압축하기
            buf1 = open(pyc_name, 'rb').read()
            buf2 = zlib.compress(buf1)

            e_rc4 = k2rc4.RC4() #rc4 알고리즘 사용
            e_rc4.set_key(key) #rc4 알고리즘에 키 적용

            #압축된 pyc 파일 이미지를 rc4로 암호화한다.
            buf3 = e_rc4.crypt(buf2)

            e_rc4 = k2rc4.RC4()
            e_rc4.set_key(key)

            #암호화한 압축된 pyc 파일 이미지 복호화하여 결과가 같은지 확인한다.
            if e_rc4.crypt(buf3) != buf2:
                continue

            #개인키로 암호화한 압축된 파일 이미지를 임시 버퍼에 추가한다.
            tmp_kmd_data += buf3

            #헤더와 본문에 대해 md5를 3번 연속 구한다.
            md5 = hashlib.md5()
            md5hash = kmd_data + tmp_kmd_data

            for i in range(3):
                md5.update(md5hash)
                md5hash = md5.hexdigest()

            m = md5hash.decode('hex')

            e_md5 = k2rsa.crypt(m, rsa_pr) #md5 결과를 개인키로 암호화
            if len(e_md5) != 32: #오류 시 다시 생성
                continue

            d_md5 = k2rsa.crypt(e_md5.rsa_pu) #md5 결과를 공개키로 복호화

            if m == d_md5:
                kmd_data += tmp_kmd_data + e_md5
                break

    #kmd file 이름을 만든다.
    ext = fname.find('.')
    kmd_name = fname[0:ext] + '.kmd'

    try :
        if kmd_data:
            #kmd 파일을 생성한다.
            open(kmd_name, 'wb').write(kmd_data)

            #pyc 파일은 삭제한다.
            os.remove(pyc_name)

            if debug:
                print ' success : %-13s -> %s' %(fname, kmd_name)
            return True
        else:
            raise IOError
    except:
        if debug:
            print ' Fail : %s' %fname
        return False


