#!/usr/bin/env python
# coding:utf-8
# manning  2014-11-7

import requests
import time
import urlparse
from splinter import Browser
from MyDataNode import DataNode

def check_type(s):
    s = s.lower()
    if s == 'static':
        return 0
    elif s == 'dynamic':
        return 1
    else:
        return 2

def fetcher(node,mytype = "static"):
    url = node.url
    mytype = check_type(mytype)

    if mytype == 0:
        try:
            response = requests.get(url,timeout = 15)
            if response.status_code == 200:
                node.set_html(response.content)
        except Exception, e:
            #差记录日志
            pass
        return
        
    elif mytype == 1:
        try:
            browser = Browser('phantomjs')
            browser.visit(url)
            node.set_html(browser.html)
            browser.quit()  
        except Exception, e:
            #差记录日志s
            print e
            pass
        return
    else:
        return

if __name__ == '__main__':
    t = DataNode("http://www.sohu.com/")
    fetcher(t)
    print 'static:\t'+str(len(t.html))
    print "----------"
    fetcher(t,"dynamic")
    print 'dynamic:\t'+str(len(t.html))
