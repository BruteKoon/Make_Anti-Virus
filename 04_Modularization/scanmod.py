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

#특정 위치 검색법을 이용하여 악성코드 검사
#특정 위치 검색법은 특정 위치에 바이트 값을 통하여 악성 코드 검사
def ScanStr(fp, offset, mal_str):
        size = len(mal_str) #악성코드 진단 문자열 길이

        #특정 위치에 악성코드 진단 문자열이 존재하는지 체크
        fp.seek(offset)
        buf = fp.read(size)

        if buf == mal_str:
                return True
        else:
                return False

