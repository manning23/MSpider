#!/usr/bin/env python
# coding:utf-8
# manning  2014-11-9

import hashlib 
import urlparse

def my_split(s):
    tmp_list = []
    for i in s.split('/'):
        for j in i.split('-'):
            for m in j.split('_'):
                tmp_list.append(m)
            
    return tmp_list

def similarity(url,hash_size):
    '''
    URL相似度判断
    主要取三个值
    1，netloc的hash值
    2，path字符串拆解成列表的列表长度
    3，path中字符串的长度
    '''
    tmp = urlparse.urlparse(url)
    scheme = tmp[0]; netloc = tmp[1]; path = tmp[2][1:]; query  = tmp[4]
    if len(path.split('/')[-1].split('.')) > 1:
        tail = path.split('/')[-1].split('.')[-1]
    elif len(path.split('/')) == 1 :
        tail = path
    else:
        tail = '1'
    tail = tail.lower()
    path_length = len(path.split('/')) -1
    path_value = 0
    path_list = path.split('/')[:-1] + [tail]
    for i in range(path_length + 1):
        if path_length - i == 0:
            path_value += hash(path_list[path_length - i])%(hash_size-1)
        else:
            path_value += len(path_list[path_length - i])*(10**(i+1))
    netloc_value = hash(hashlib.new("md5", netloc).hexdigest())%(hash_size-1)
    url_value = hash(hashlib.new("md5", str(path_value + netloc_value)).hexdigest())%(hash_size-1)
    return url_value

if __name__ == '__main__':
    size = 1000000000
    l = [
        'http://auto.sohu.com/7/0903/70/column213117075.shtml',
        'http://auto.sohu.com/7/0903/95/column212969565.shtml',
        'http://auto.sohu.com/7/0903/96/column212969687.shtml',
        'http://auto.sohu.com/7/1103/61/column216206148.shtml',
        'http://auto.sohu.com/s2007/0155/s254359851/index1.shtml',
        'http://auto.sohu.com/s2007/5730/s249066842/index2.shtml',
        'http://auto.sohu.com/s2007/5730/s249067138/index3.shtml',
        'http://auto.sohu.com/s2007/5730/s249067983/index4.shtml']
    for i in l:
        print i + '\t\t' + str(similarity(i,size))
            