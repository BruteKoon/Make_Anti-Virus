#-*- coding:utf-8 -*-
import os
import hashlib


#바이러스 db에 존재하는지 확인
def SearchVDB(vdb, fmd5):
        for t in vdb :
                if t[0] == fmd5:
                        return True, t[1]
        return False, ''



#md5를 이용하여 악성코드 검사
def ScanMD5(vdb, vsize, fname):
        ret = False
        vname = ''

        size = os.path.getsize(fname)
        if vsize.count(size):
                fp = open(fname, 'rb')
                buf = fp.read()
                fp.close()

                m = hashlib.md5()
                m.update(buf)
                fmd5 = m.hexdigest()

                ret, vname = SearchVDB(vdb,fmd5)

        return ret, vname
