#-*- coding:utf-8 -*-
import os
import hashlib

fp = open('./eicar.txt', 'rb')
fbuf = fp.read()
fp.close()


m = hashlib.md5()
m.update(fbuf)
fmd5 = m.hexdigest()

#EICAR TEST 파일 MD5 비교
if fmd5 == '117599303ed472727a2cbe1343ad6989':
    print 'virus'
    os.remove('eicar.txt')
else:
    print 'No virus'
