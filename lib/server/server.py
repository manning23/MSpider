#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17

import time
import sys
sys.path.append(sys.path[0].split('MSpider')[0] + "MSpider")
import threading
import logging
from lib.core.rules import UrlRuleClass
from lib.core.scheduling import spider_scheduling
from lib.core.spider import spider
from lib.structure.GlobalData import MSpiderGlobalVariable
from scheduling import global_scheduling

spider_logger = logging.getLogger('MSpiderLogs')

def global_server(spider_global_variable):
    # 初始化全局变量
    url_rule = UrlRuleClass(spider_global_variable)

    threads_list = []
    spider_threads = []

    threads_list.append(threading.Thread(target=spider_scheduling, args=(spider_global_variable, url_rule,)))
    threads_list.append(threading.Thread(target=global_scheduling, args=(spider_global_variable,)))

    for t in threads_list:
        t.setDaemon(True)
        t.start()

    if spider_global_variable.spider_use_gevent:
        import gevent
        from gevent import monkey
        monkey.patch_all(thread=False)
        for i in xrange(spider_global_variable.threads):
            spider_threads.append(gevent.spawn(spider, spider_global_variable))
        gevent.joinall(spider_threads)
    else:
        for i in xrange(spider_global_variable.threads):
            spider_threads.append(threading.Thread(target=spider, args=(spider_global_variable,)))
        for t in spider_threads:
            t.setDaemon(True)
            t.start()


    time.sleep(120)
    while True:
        if spider_global_variable.spider_urlnode_queue.qsize() == 0:
            spider_logger.critical('MSpider wait to exit!!')
            time.sleep(120)
            if spider_global_variable.spider_urlnode_queue.qsize() == 0:
                pass
            else:
                continue
            spider_global_variable.end_ctime = time.ctime()
            time.sleep(120)
            spider_logger.critical('MSpider exit!!')
            sys.exit(0)
        else:
            time.sleep(10)
