import k2rc4

if __name__ == '__main__':
    rc4 = k2rc4.RC4()
    rc4.set_key('PASSWORD1234')
    t1 = rc4.crypt('hello')
    print t1


    rc4 = k2rc4.RC4()
    rc4.set_key('PASSWORD1234')
    t2 = rc4.crypt(t1)
    print t2
