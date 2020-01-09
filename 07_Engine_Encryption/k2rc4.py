# -*- coding:utf-8 -*-

class RC4:

    # 멤버 변수 초기화
    def __init__(self):
        self.__S = []
        self.__T = []
        self.__Key = []
        self.__K_i = 0
        self.__K_j = 0

    #암호를 설정한다.
    # password - rc4 암호문
    def set_key(self, password):
        for i in range(len(password)):
            self.__Key.append(ord(password[i]))
            self.__init_rc4()

    # 주어진 데이터를 암/복호화한다.
    # arg = 암복호활 데이터/ return = 암/복호화 결과 데이터
    def crypt(self, data):
        t_str = []

        for i in range(len(data)):
            t_str.append(ord(data[i]))

        for i in range(len(t_str)):
            t_str[i] ^= self.__gen_k()

        ret_s = ''
        for i in range(len(t_str)):
            ret_s += chr(t_str[i])

        return ret_s

    # rc4 테이블 초기화
    def __init_rc4(self):
        # S 초기화
        for i in range(256):
            self.__S.append(i)
            self.__T.append(self.__Key[i % len(self.__Key)])

        j = 0
        for i in range(256):
            j = (j + self.__S[i] + self.__T[i]) % 256
            self.__swap(i,j)


    # 주어진 두 인덱스 데이터 교환
    def __swap(self, i, j):
        temp = self.__S[i]
        self.__S[i] = self.__S[j]
        self.__S[j] = temp


    # 암/복호화에 필요한 스트림을 생성
    def __gen_k(self):
        i = self.__K_i
        j = self.__K_j

        i = (i+1) % 256
        j = (j+ self.__S[i]) % 256
        self.__swap(i,j)
        t = (self.__S[i] + self.__S[j]) % 256

        self.__K_i = i
        self.__K_j = j

        return self.__S[t]

