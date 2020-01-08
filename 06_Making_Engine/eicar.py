# -*- coding:utf-8 -*-

import os
import hashlib

class KavMain:
    
    # 플러그인 엔진 초기화
    def init(self, plugin_path):
        return 0

    # 플러그인 엔진 종료
    def uninit(self):
        return 0

    # ==> init/uninit 여기서는 별다른 역할 x

    # 악성코드 검사
    def scan(self, filehandle, filename):
        try:
            mm = filehandle
            size = os.path.getsize(filename)
            if size == 86:
                m = hashlib.md5()
                m.update(mm[:86])
                fmd5 = m.hexdigest()

                if fmd5 == '117599303ed472727a2cbe1343ad6989':
                    return True, 'EICAR-TEST-FILE', 0
        except IOError:
            pass
        return False, '', -1

    # 악성코드 치료
    def disinfect(self, filename, malware_id):
        try:
            if malware_id == 0:
                os.remove(filename)
                return True
        except IOError:
            pass
        return False

    # 바이러스 목록
    def listvirus(self) :
        vlist = list()
        vlist.append('EICAR-Test-File')
        return vlist
    
    # 엔진 정보
    def getinfo(self):
        info = dict()

        info['author'] = 'Koon'
        info['version'] = '1.0'
        info['title'] = 'EICAR Scan Engine'
        info['kmd_name'] = 'eicar'

        return info

