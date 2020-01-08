# -*- coding:utf-8 -*-

import os
import hashlib

class KavMain:
    
    # 플러그인 엔진 초기화
    def init(self, plugin_path):
        pass

    # 플러그인 엔진 종료
    def uninit(self):
        pass

    # 악성코드 검사
    def scan(self, filehandle, filename):
        pass

    # 악성코드 치료
    def disinfect(self, filename, malware_id):
        pass

    # 바이러스 목록
    def listvirus(self) :
        pass
    
    # 엔진 정보
    def getinfo(self):
        pass
