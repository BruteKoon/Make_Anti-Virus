#-*- coding:utf-8 -*-
import sys
import os
import hashlib
import zlib
import StringIO
import scanmod #모듈화를 통해 추가된 부분 (바이러스 검사용 모듈)
import curemod #모듈화를 통해 추가된 부분 (치료용 모듈)

#바이러스 DB ==> 암호화된 virus.kmd에 존재
VirusDB = []

#프로그램 동작 중 실제로 사용하는 DB용 리스트
vdb= []
vsize = []

sdb = [] #특정 위치 검색 용 db

#.kmd 파일을 복호화
def DecodeKMD(fname):
        try :
                fp = open(fname, 'rb')
                buf = fp.read()
                fp.close()

                buf2 = buf[:-32] #암호화 내용 분리
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


#virus.db 파일에서 악성코드 패턴을 읽음
def LoadVirusDB() :
	buf = DecodeKMD('virus.kmd')
	fp = StringIO.StringIO(buf)
	
	while True:
		line = fp.readline()
		if not line : break
		
		line = line.strip()
		VirusDB.append(line) #악성코드 패턴을 VirusDB 리스트에 추가
	fp.close()
	
#VirusDB --> vdb로 작업 진행
def MakeVirusDB():
    for pattern in VirusDB:
        t = []
        v = pattern.split(':')

        scan_func = v[0]
        cure_func = v[1]

        if scan_func == 'ScanMD5':
                t.append(v[3])
                t.append(v[4])
                vdb.append(t)

                size = int(v[2])
                if(vsize.count(size)) == 0:
                   vsize.append(size)
        elif scan_func == 'ScanStr':
                t.append(int(v[2]))
                t.append(v[3])
                t.append(v[4])
                sdb.append(t)


#vdb에서 md5 비교
def SearchDB(fmd5):
    for t in vdb :
        if t[0] == fmd5:
            return True, t[1]
        else:
            return False, ''

#Main 
if __name__ == '__main__':
    LoadVirusDB()
    MakeVirusDB()

    if len(sys.argv) != 2:
        print 'Usage : antivirus.py [file]'
        exit(0)
        
    fname = sys.argv[1]

    ret, vname = scanmod.ScanVirus(vdb, vsize, sdb, fname)

    if ret == True:
        print 'virus'
        print '%s : %s' %(fname, vname)
        curemod.CureDelete(fname)
    else:
            print 'No virus'
            print '%s : ok' %(fname)

