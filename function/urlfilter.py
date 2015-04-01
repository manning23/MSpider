#!/usr/bin/env python
# coding:utf-8
# manning  2015-1-27
import time
import os
import urlparse
import hashlib
import sys
sys.path.append("..")

from config.config import *
reload(sys) 
sys.setdefaultencoding("utf-8") 

SIMILAR_SET = set()
REPEAT_SET = set()

'''
2015.3.30
分清楚爬虫 什么是聚焦 什么是过滤
聚焦：  如果keyword在url则返回True 否则返回False

过滤：  如果keyword在url则返回False 否则返回True
'''


def format(url):
    '''
    策略是构建一个三元组
    第一项为url的netloc
    第二项为path中每项的拆分长度
    第三项为query的每个参数名称(参数按照字母顺序排序，避免由于顺序不同而导致的重复问题)
    '''
    if urlparse.urlparse(url)[2] == '':
        url = url+'/'

    url_structure = urlparse.urlparse(url)
    netloc = url_structure[1]
    path = url_structure[2]
    query = url_structure[4]
    
    temp = (netloc,tuple([len(i) for i in path.split('/')]),tuple(sorted([i.split('=')[0] for i in query.split('&')])))
    #print temp
    return temp


def check_netloc_is_ip(netloc):
    '''
    如果url的netloc为ip形式
    return True
    否则
    return False
    '''
    flag =0
    t = netloc.split('.')
    for i in t:
        try:
            int(i)
            flag += 1
        except Exception, e:
            break
    if flag == 4:
        return True
    
    return False

def url_domain_control(url,keyword):
    '''
    URL域名控制  聚焦

    True url符合域名判断
    False url不符合域名判断

    1，keyword可以是list或者str
    2，如果url的netloc为ip形式，return True

    '''
    t = format(url)
    if check_netloc_is_ip(t[0]):
        return True

    elif str(type(keyword)) == "<type 'list'>":
        for i in keyword:
            if i.lower() in t[0].lower():
                return True

    elif str(type(keyword)) == "<type 'str'>":
        if keyword.lower() in t[0].lower():
            return True
    return False

def url_domain_control_ignore(url,keyword):
    '''
    URL域名控制  过滤

    True 忽略关键字不在url中
    False 忽略关键字在url中

    例如：
    忽略blog，如果域名的netloc内有blog，则返回false
    '''
    t = format(url)
    for i in keyword:
        if i in t[0].lower():
            return False
    return True

def url_similar_control(url):
    '''
    URL相似性控制
    
    True url未重复
    False url重复
    '''
    t = format(url)
    if t not in SIMILAR_SET:
        SIMILAR_SET.add(t)
        return True
    return False


def url_format_control(url):
    '''
    URL格式控制  过滤

    True url符合格式判断
    False url不符合格式判断
    '''

    if '}' not in url and '404' not in url and url[0].lower() == 'h' and '/////' not in url and len(format(url)[1]) < 6:
        if len(format(url)[2]) > 0:
            for i in format(url)[2]:
                if len(i) > 20:
                    return False
        if 'viewthread' in url or 'forumdisplay' in url:
            return False
        return True
    return False

def url_custom_control(url):
    '''
    URL自定义关键字控制  过滤
    True 
    False
    '''
    for i in CUSTOM_KEY:
        if i in url:
            return False
    return True

def url_custom_focus_control(url,focuskey):
    '''
    URL自定义关键字控制  聚焦
    True 符合聚焦策略
    False
    '''
    if len(focuskey) == 0:
        return True
    for i in focuskey:
        if i in url:
            return True
    return False

def url_repeat_control(url):
    '''
    URL重复控制

    True url未重复
    False url重复
    '''
    if url not in REPEAT_SET:
        REPEAT_SET.add(url)
        return True
    return False

def url_filter_similarity(url,keyword,ignore_keyword,focuskey):
    if url_format_control(url) and url_similar_control(url) \
                and url_domain_control(url,keyword) and url_domain_control_ignore(url,IGNORE_KEY_WORD) \
                    and url_custom_control(url) and url_custom_focus_control(url,focuskey):
        return True
    else:
        return False
def url_filter_no_similarity(url,keyword,ignore_keyword,focuskey):
    if url_format_control(url) and url_repeat_control(url) \
                and url_domain_control(url,keyword) and url_domain_control_ignore(url,IGNORE_KEY_WORD) \
                    and url_custom_control(url) and url_custom_focus_control(url,focuskey):
        return True
    else:
        return False


if __name__ == "__main__": 
    print url_format_control("http://www.1hai.cn")