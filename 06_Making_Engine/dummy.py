# -*- coding:utf-8 -*-

class KavMain:
    #플러그인 엔진을 초기화한다.
    def init(self, plugins_path):
        #진단/치료하는 악성 코드 , 패턴
        self.virus_name = "Duumy-Test-File"
        self.dummy_pattern = "Dummy Engine Test File"
        return 0
    
    #플러그인 엔진을 종료한다.
    def uninit(self):
        # 메모리 해제
        del self.virus_name
        del self.dummy_pattern
        return 0

    #악성코드를 검사한다.
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


    #악성코드를 치료한다.
    def disinfected(self):
        pass


    #플러그인 엔진이 진단/치료 가능한 악성코드의 리스트를 알려준다.
    def viruslist(self):
        pass


    #플러그인 엔진의 주요 정보를 알려준다.
    def getinfo(self):
        pass
