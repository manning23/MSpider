#!/usr/bin/env python
# coding:utf-8
# manning  2015-1-27
import time
import os
import urlparse
import requests
import signal
import sys
import random
sys.path.append("..")

from splinter import Browser
from config.config import *

reload(sys) 
sys.setdefaultencoding("utf-8") 



def fetcher(url,DOWNLOAD_MODE):
    '''
    页面下载模块
    '''
    time.sleep(FETCH_TIME_INTERVAL)         #抓取时间间隔

    if DOWNLOAD_MODE == 0:
        #静态模式
        try:
            response = requests.get(url,timeout = 15 ,headers = random_header())
            if response.status_code == 200:
                return response.content
            else:
                return ""
        except Exception, e:
            #差记录日志
            return ""
            
            

    elif DOWNLOAD_MODE == 1:
        #动态模式
        try:
            browser = Browser('phantomjs')
            browser.visit(url)
            html = browser.html
            browser.quit()  
            return html
        except Exception, e:
            #差记录日志s
            return ""

    elif DOWNLOAD_MODE == 2:
        #动静模式
        try:
            if random.randint(1,99) > DOWNLOAD_RATE:
                response = requests.get(url,timeout = 15,headers = HEADERS)
                if response.status_code == 200:
                    return response.content
                else:
                    return ""
            else:
                try:
                    browser = Browser('phantomjs')
                    browser.visit(url)
                    html = browser.html
                    browser.quit()  
                    return html
                except Exception, e:
                    #差记录日志s
                    return ""
        except Exception, e:
            #差记录日志s
            return ""
    else:
        return ""

if __name__ == "__main__": 
    pass