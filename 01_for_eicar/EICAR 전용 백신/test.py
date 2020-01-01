#-*- coding:utf-8 -*-
import os

fp = open('./eicar.txt', 'rb')
fbuf = fp.read()
fp.close()
#Signature 비교
#바이러스인 경우
if fbuf[0:3] == 'X5O':
    print "virus"
    
    #삭제를 통한 치료
    os.remove('./eicar.txt')
#바이러스 아닌 경우    
else :
    print "No virus"


