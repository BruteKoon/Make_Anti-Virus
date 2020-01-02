#-*- coding:utf-8 -*-
import sys
import os
import hashlib
import zlib

def DecodeKMD(fname):
        try :
                fp = open(fname, 'rb')
                buf = fp.read()
                fp.close()

                buf2 = buf[:32] #암호화 내용 분리
                fmd5 = buf[-32:] # MD5 분리

                f = buf2
                for i in range(3):
                        md5 = hashlib.md5()
                        md5.update(f)
                        f = md5.hexdigest()

                if f != fmd5:
                        raise SystemError

                buf3 = ''
                for c in buf2[4:] : #0XFF로 xor (복호화)
                        buf3 += chr(ord(c) ^ 0XFF)

                buf4 = zlib.decompress(buf3) # 압축해
                return buf4
        except:
                pass

        return None
