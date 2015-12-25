#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17
"""
MSpider 全局调度
"""

import random
import time
import sys
sys.path.append(sys.path[0].split('MSpider')[0] + "MSpider/lib")

from crawl import crawl
from structure.UrlData import UrlNode
from common.common import is_netloc

def exit_condition(SpiderGlobalVariable):
    # 调度退出机制函数
    if time.time() -SpiderGlobalVariable.start_time < SpiderGlobalVariable.time:
        if SpiderGlobalVariable.exit_flag_count < SpiderGlobalVariable.threads:
            if SpiderGlobalVariable.total_count < SpiderGlobalVariable.count:
                return True
    return False


def init_urlnode(start_urls_list,UrlRule):
    nodelist = []
    for i in start_urls_list:
        if UrlRule.check_url(i):
            tmpnode = UrlNode(i, '', -1)
            nodelist.append(tmpnode)
    return nodelist


def spider_scheduling(SpiderGlobalVariable,UrlRule):
    '''
    SpiderGlobalVariable
    '''
    for i in init_urlnode(SpiderGlobalVariable.start_url,UrlRule):
        SpiderGlobalVariable.global_urlnode_queue.put((0,i))

    while exit_condition(SpiderGlobalVariable):
        if SpiderGlobalVariable.htmlnode_queue.qsize() > 0:
            html_node = SpiderGlobalVariable.htmlnode_queue.get()
            linklist = crawl(html_node.url, html_node.html)
            for i in linklist:
                url = i[1]
                method = i[0]
                data = i[2]
                depth = html_node.depth
                referer = html_node.url
                i = UrlNode(url, referer, depth, method, data)

                if i.depth <= SpiderGlobalVariable.depth and UrlRule.check_url(i.check_url):
                    if is_netloc(i.url):
                        SpiderGlobalVariable.global_urlnode_queue.put((0,i))
                    else:
                        SpiderGlobalVariable.global_urlnode_queue.put((random.randint(1,5),i))

                else:
                    SpiderGlobalVariable.refuse_count += 1
