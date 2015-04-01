#!/usr/bin/env python
# coding:utf-8
# manning  2015-1-27
import lxml.html
import urlparse
import time
import sys
sys.path.append("..")

from fetch import fetcher
from config.config import *
from node import UrlNode,HtmlNode

def timestamp():
    return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

def crawler(html_node):
    link_list = []
    html = html_node.html
    url = html_node.url
    if html == '':
        return []
    else:
        #获取页面内的links
        try:
            tmp = lxml.html.document_fromstring(html)
            tmp.make_links_absolute(url)
            links = tmp.iterlinks()
            link_list = list(set([i[2] for i in links]))
            
        except Exception, e:
            pass

            
        #过滤不期待页面后缀
        try:
            temp_list = []
            for i in link_list:
                if urlparse.urlparse(i)[2].split('.')[-1].lower() not in IGNORE_EXT:
                    temp_list.append(i)
                link_list = temp_list
        except Exception, e:
            print str(e)

        tmp_url_node = []
        for i in link_list:
            tmp_url_node.append(UrlNode(urlparse.urlunparse((urlparse.urlparse(i)[0],urlparse.urlparse(i)[1],urlparse.urlparse(i)[2],urlparse.urlparse(i)[3],urlparse.urlparse(i)[4],'')),url,len(html),timestamp(),'',html_node.depth))
        return tmp_url_node

if __name__ == '__main__':
    pass