#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17
'''
MSpider的通用函数
'''

import sys
import time
import urlparse

def get_absolute_path():
    '''
    获取MSpider的绝对路径
    '''
    path = sys.path[0]
    path = path.split('MSpider')[0] + "MSpider/"
    return path

#sys.path[0].split('MSpider')[0] + "MSpider/"

def is_netloc(url):
    '''
    判断当前url是否为纯域名形式
    urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
    ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',params='', query='', fragment='')
    '''
    parse_result = urlparse.urlparse(url)
    if len(parse_result[1]) > 0 and len(parse_result[2]) <= 1 and len(parse_result[4]) == 0:
        return True
    else:
        return False

def get_netloc(url):
    '''
    获取当前url的域名字段
    '''
    return urlparse.urlparse(url)[1]

def is_ipv4_address(ip_str):
    '''
    判断是否是合法的ipv4地址
    '''
    if len(ip_str.split('.')) != 4:
        return False

    for i in ip_str.split('.'):
        try:
            int(i)
            if int(i) > 255:
                return False
        except Exception as e:
            return False
    if ip_str.startswith('192.'):
        return False
    if ip_str.startswith('10.'):
        return False
    return True

def timestamp():
    return  str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
