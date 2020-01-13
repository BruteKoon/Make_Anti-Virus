# -*- coding:utf-8 -*-

import sys
import k2rsa

if __name__ == '__main__':
    pu_fname = 'key.pkr'
    pr_fname = 'key.skr'

    if len(sys.argv) == 3:
        pu_fname = sys.argv[1]
        pr_fname = sys.argv[2]
    elif len(sys.argv) != 1:
        print 'Usage : mkkey.py [pu] [pk] '
        exit(0)


    k2rsa.create_key(pu_fname, pr_fname, True)
