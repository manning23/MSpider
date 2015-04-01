#!/usr/bin/env python
# coding:utf-8
# manning  2014-11-13

import hashlib
import sys
reload(sys) 
sys.setdefaultencoding("utf-8") 

def bloomfilter(url,size):
    v0 = hash(hashlib.md5(url).hexdigest())%(size - 1)
    v1 = hash(hashlib.sha1(url).hexdigest())%(size - 1)
    v2 = hash(hashlib.sha224(url).hexdigest())%(size - 1)
    v3 = hash(hashlib.sha256(url).hexdigest())%(size - 1)
    v4 = hash(hashlib.sha384(url).hexdigest())%(size - 1)
    v5 = hash(hashlib.sha512(url).hexdigest())%(size - 1)
    return [v0,v1,v2,v3,v4,v5]


if __name__ == '__main__':
    t = bloomfilter('http://www.baidu.com',100000000)
    print t