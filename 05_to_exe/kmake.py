#-*- coding:utf-8 -*-
import sys
import os
import hashlib
import zlib

def main() :
        if len(sys.argv) != 2:
                print 'Usage : kmake.py [file]'
                return

        fname = sys.argv[1] #암호화 파일 대상
        tname = fname

        fp = open(tname, 'rb') #대상 파일 읽기
        buf = fp.read()
        fp.close()

        buf2 = zlib.compress(buf) #파일 압축

        buf3 = ''

        #xor 암호화
        for c in buf2 :
                buf3 += chr(ord(c) ^ 0xFF)

        buf4 = 'KAVM' + buf3 #헤더 생성
        

        f = buf4
        for i in range(3) : # 지금까지의 한것을 md5로 변환
                md5 = hashlib.md5()
                md5.update(f)
                f = md5.hexdigest()

        buf4 += f

        kmd_name = fname.split('.')[0] + '.kmd'
        fp = open(kmd_name, 'wb')
        fp.write(buf4)
        fp.close()

        print '%s -> %s' % (fname, kmd_name)

if __name__ == '__main__':
        main()
