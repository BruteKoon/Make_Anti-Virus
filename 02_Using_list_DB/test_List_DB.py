#-*- coding:utf-8 -*-
import sys
import os
import hashlib

#바이러스 DB
VirusDB = {
    '117599303ed472727a2cbe1343ad6989:EICAR TEST',
    'ef5a19cc8eed8de1621f6a0591e374e4:Dummy TEST'

}

#프로그램 동작 중 실제로 사용하는 DB용 리스트
vdb= []

#VirusDB --> vdb로 작업 진행
def MakeVirusDB():
    for pattern in VirusDB:
        t = []
        v = pattern.split(':')
        t.append(v[0])
        t.append(v[1])
        vdb.append(t)


#vdb에서 md5 비교
def SearchDB(fmd5):
    for t in vdb :
        if t[0] == fmd5:
            return True, t[1]
        else:
            return False, ''

if __name__ == '__main__':
    MakeVirusDB()

    if len(sys.argv) != 2:
        print 'Usage : test_List_DB.py [file]'
        exit(0)

    fname = sys.argv[1]
    fp = open(fname, 'rb')
    fbuf = fp.read()
    fp.close()


    m = hashlib.md5()
    m.update(fbuf)
    fmd5 = m.hexdigest()

    ret, vname = SearchDB(fmd5)
# vdb에 존재하는 MD5 비교
    if ret == True:
        print 'virus'
        print '%s : %s' %(fname, vname)
        os.remove(fname)
    else:
        print 'No virus'
        print '%s : ok' %(fname)
