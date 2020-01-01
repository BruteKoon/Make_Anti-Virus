#-*- coding:utf-8 -*-
import os

fp = open('./eicar.txt', 'rb')
fbuf = fp.read()
fp.close()
#Signature 비교
if fbuf[0:3] == 'X5O':
    print "virus"
    os.remove('./eicar.txt')
else :
    print "No virus"


