#!/usr/bin/env python
# coding:utf-8
# manning  2015-1-27
import os
import random

'''
参数配置
'''

DOWNLOAD_MODE = 2
'''
下载模式
静态模式    0
动态模式    1
动静模式    2
'''

DOWNLOAD_RATE = 50
'''
动静模式下，动静分配比率
0为全静态
100为全动态
'''

FETCH_TIME_INTERVAL = 5
'''
抓取时间间隔
'''

FETCH_TIME = 3600*8
'''
抓取时间
'''

IGNORE_EXT = ('js','css','png','jpg','gif','bmp','svg','exif',\
            'jpeg','exe','doc','docx','ppt','pptx','pdf','ico',\
            'wmv','avi','swf','apk','xml','xls','thmx')
'''
不期待文件后缀
'''


SPIDER_PROXY = False
'''
爬虫代理
'''

SPIDER_PROXY_DIC = {}
'''
爬虫代理ip字典
'''
def set_proxy_dic():
    if SPIDER_PROXY == True:
        #设置爬虫代理ip字典
        pass


THREAD_NUM = 10
'''
线程数量
'''



KEY_WORD = 'bjut'
IGNORE_KEY_WORD = ['blog','bbs']
CUSTOM_KEY = ['home.php','forum.php']
'''
爬虫过滤关键字 字典  PS：列表形式
'''
def set_key_word(key):
    klist = key.split(',')
    return klist


START_URLS = '/home/work/wanderSpider/data/starturls.txt'
'''
爬虫起始urls
'''
def clean_url(url):
    character_list = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    while url[-1] not in character_list:
        url = url[:-1]
    return url

def set_start_urls(key):
    if os.path.isfile(str(key)):
        t = open(key).readlines()
        temp_urls_list = []
        for i in t:
            if '\r\n' in i:
                if 'http://' not in i:
                    temp_urls_list.append('http://' + i[:-2])
                else:
                    temp_urls_list.append(i[:-2])
            elif '\n' in i:
                if 'http://' not in i:
                    temp_urls_list.append('http://' + i[:-1])
                else:
                    temp_urls_list.append(i[:-1])
            else:
                temp_urls_list.append(i)
        return temp_urls_list

    elif str(type(key)) == "<type 'list'>":
        return key

    elif str(type(key)) == "<type 'str'>":
        if 'http://' in key:
            temp_urls_list = []
            temp_urls_list.append(key)
            return temp_urls_list
        elif len(key) < 11:
            temp_urls_list = []
            for i in open('./data/allurl.txt').readlines():
                t = ''
                if key in i:
                    if 'http://' in i:
                        url = clean_url(i)
                        temp_urls_list.append(url)
                    else:
                        t = 'http://' + i[:-2]
                        url = clean_url(t)
                        temp_urls_list.append(url)
            return temp_urls_list
    else:
        return []
#START_URLS = set_start_urls(START_URLS)


USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

HEADERS = {'User-Agent':random.choice(USER_AGENTS)}

def random_header():
    return {'User-Agent':random.choice(USER_AGENTS)}

DEPTH = 1000