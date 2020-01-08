# -*- coding:utf-8 -*-

class KavMain:
    # 플러그인 엔진을 초기화한다.
    def init(self, plugins_path):
        #진단/치료하는 악성 코드 , 패턴
        self.virus_name = "Duumy-Test-File"
        self.dummy_pattern = "Dummy Engine Test File"
        return 0
    
    # 플러그인 엔진을 종료한다.
    def uninit(self):
        # 메모리 해제
        del self.virus_name
        del self.dummy_pattern
        return 0

    # 악성코드를 검사한다.
    def scan(self, filehandle, filename):
        try:
            #파일을 통해 악성코드 패턴 읽기
            fp = open(filename)
            buf = fp.read(len(self.dummy_pattern))
            fp.close()i

            # 악성코드 패턴 비교
            if buf == self.dummy_pattern :
                return True, self.virus_name, 0

        except IOError:
            pass
        
        return False, '', -1


    # 악성코드를 치료한다.
    def disinfected(self, filename, malware_id):
        try:
            if malware_id == 0:
                os.remove(filename)
                return True

        except IOError:
            pass
        return False


    # 플러그인 엔진이 진단/치료 가능한 악성코드의 리스트를 알려준다.
    def listvirus(self):
        vlist = list()
        
        #진단하는 악성코드 이름 등록
        vlist.append(self.virus_name)
        return vlist


    # 플러그인 엔진의 주요 정보(만든 사람...)를 알려준다.
    def getinfo(self):
        info = dict()        
        info['author'] = 'Koon'
        info['version'] = '1.0'
        info['title'] = 'Dummy Scan Engine'
        info['kmd_name'] = 'dummy'

        return info
