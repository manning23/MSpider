#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17
'''
MSpider 爬虫工作线程
            2015.5.20
            调整输出样式，参考了@lijiejie的一些代码

            2015.3.28
            抓取模型
            0，广度优先（缺省）
            1，深度优先
            2，随机优先

            2015.3.27
            加入数据队列，单起一个线程写入数据库
            数据库类型为sqlite
            预计支持mysql、sql server等

            2015。3.26
            添加深度控制

            2015.3.8
            server退出机制
            1，超过爬取时间
            2，爬取线程不存在(可能爬完)
            3，深度超越
            4，抓取个数超越

            线程退出机制
            如果此线程5分钟内没有工作，线程退出

'''
import time
import sys
sys.path.append(sys.path[0].split('MSpider')[0] + "MSpider/lib")
from console import getTerminalSize
from fetch import fetch
from common.common import timestamp
from structure.HtmlData import HtmlNode

import logging
spider_logger = logging.getLogger('MSpiderLogs')

def spider(SpiderGlobalVariable):
    if SpiderGlobalVariable.spider_use_gevent:
        import gevent
    while True:
        if SpiderGlobalVariable.spider_urlnode_queue.qsize() > 0:
            _,node = SpiderGlobalVariable.spider_urlnode_queue.get()
            html = fetch(node.url, SpiderGlobalVariable.spider_model, SpiderGlobalVariable.fetch_time_interval, SpiderGlobalVariable.random_agent)
            if len(html) < 10:
                pass
            html_node = HtmlNode(node.url, html, timestamp(), node.depth)
            SpiderGlobalVariable.htmlnode_queue.put(html_node)
            SpiderGlobalVariable.total_count += 1

            if SpiderGlobalVariable.print_all:
                msg = "[Url] %s  Depth: %s  Found: %s Remaining: %s  Html: %s"% (node.url, str(node.depth), str(SpiderGlobalVariable.total_count), str(SpiderGlobalVariable.spider_urlnode_queue.qsize()), str(len(html)))
                spider_logger.info(msg)

            else:
                msg = "[Url] %s  Depth: %s  Found: %s Remaining: %s  Html: %s" % (node.url, str(node.depth), str(SpiderGlobalVariable.total_count), str(SpiderGlobalVariable.spider_urlnode_queue.qsize()), str(len(html)))
                console_width = getTerminalSize()[0] - 0
                if len(msg) - console_width > 0:
                    msg = msg[:console_width]
                    sys.stdout.write('\r' + msg)
                    sys.stdout.flush()
                else:
                    sys.stdout.write('\r' + msg + ' ' * (console_width - len(msg)))
                    sys.stdout.flush()
            if SpiderGlobalVariable.spider_use_gevent:
                gevent.sleep(0)
        else:
            if SpiderGlobalVariable.spider_use_gevent:
                gevent.sleep(0)
            else:
                time.sleep(5)
    SpiderGlobalVariable.exit_flag_count += 1
