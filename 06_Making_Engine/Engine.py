# -*- coding:utf-8 -*-

class Main:
    #플러그인 엔진을 초기화한다.
    def init(self):
        pass

    
    #플러그인 엔진을 종료한다.
    def uninit(self):
        pass


    #악성코드를 검사한다.
    def scan(self):
        pass


    #악성코드를 치료한다.
    def disinfected(self):
        pass


    #플러그인 엔진이 진단/치료 가능한 악성코드의 리스트를 알려준다.
    def viruslist(self):
        pass


    #플러그인 엔진의 주요 정보를 알려준다.
    def getinfo(self):
        pass
