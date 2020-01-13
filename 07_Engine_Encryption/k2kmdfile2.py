# -*- coding:utf-8 -*-

import struct
import hashlib
import zlib
import k2rc4
import k2rsa
import k2timelib


# 주어진 버퍼에 대해 n회 반복해서 MD5 해시 결과를 리턴
def ntimes_md5(buf, ntims):
    md5 = hashlib.md5()
    md5hash = buf
    for i in range(ntimes):
        md5.update(md5hash)
        md5hash = md5.hexdigest()
    return md5hash

# KMD 오류 메시지 정의
class KMDFormatError(Exception):
    def __init(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

# KMD 관련 상수
class KMDConstants:
    KMD_SIGNATURE = 'KAVM'

    KMD_DATE_OFFSET = 4
    KMD_DATE_LENGTH = 2
    KMD_TIME_OFFSET = 6
    KMD_TIME_LENGTH = 2

    KMD_RESERVED_OFFSET = 8
    KMD_RESERVED_LENGTH = 28

    KMD_RC4_KEY_OFFSET = 36
    KMD_RC4_KEY_LENGTH = 32
    KMD_MD5_OFFSET = -32

# KMD 클래스
class KMD(KMDConstants):

    # 클래스 초기화
    def __init__(self, fname, pu):
        self.filename = fname
        self.date = None
        self.time = None
        self.body = None

        self.__kmd_data = None
        self.__rsa_pu = pu
        self.__rc4_key = None

        if self.filename:
            self.__decrypt(self.filename)

    #kmd 파일을 복호화
    def __decrypt(self, fname, debug=False):
        with open(fname, 'rb') as fp:
            if fp.read(4) == self.KMD_SIGNATURE:
                self.__kmd_data = self.KMD_SIGNATRURE + fp.read()
            else:
                raise KMDFormatError('KMD Header magic not found.')

        tmp = self.__kmd_data[self.KMD_DATE_OFFSET:self.KMD_DATE_OFFSET + self.KMD_DATE_LENGTH]
        self.date = k2timelib.convert_date(struct.unpack('<H', tmp)[0])


        tmp = self.__kmd_data[self.KMD_TIME_OFFSET:self.KMD_TIME_OFFSET + self.KMD_TIME_LENGTH]
        self.time = k2timelib.convert_time(struct.unpack('<H', tmp)[0])

        e_md5hash = self.__get_md5()

        md5hash = ntimes_md5(self.__kmd_data[:self.KMD_MD5_OFFSET], 3)
        if e_md5hash != md5hash.decode('hex'):
            raise KMDFormatError('Invalid KMD MD5 hash')

        
        self.__rc4_key = self.__get_rc4_key()

        e_kmd_data = self.__get_body()
        if debug:
            print lne(e_kmd_data)

        self.body = zlib.decompress(e_kmd_data)
        if debug:
            print len(self.body)

    # kmd 파일의 rc4 키를 얻는다.
    def __get_rc4_key(self):
        e_key = self.__kmd_data[self.KMD_RC4_KEY_OFFSET:self.KMD_RC4_KEY_OFFSET + self.KMD_RC4_KEY_LENGTH]
        return k2rsa.crypt(e_key, self.__rsa_pu)

    # kmd 파일의 body를 얻음
    def __get_body(self):
        e_kmd_data = self.__kmd_data[self.KMD_RC4_KEY_OFFSET + self.KMD_RC4_KEY_LENGTH:self.KMD_MD5_OFFSET]
        r = k2rc4.RC4()
        r.set_key(self.__rc4_key)
        return r.crypt(e_kmd_data)


    #kmd 파일의 md5 얻기
    def __get_md5(self):
        e_md5 = self.__kmd_data[self.KMD_MD5_OFFSET:]
        return k2rsa.crypt(e_md5, self.__rsa_pu)



