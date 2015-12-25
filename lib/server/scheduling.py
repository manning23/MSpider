#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17
"""
MSpider global_scheduling
"""
import time
import logging
spider_logger = logging.getLogger('MSpiderLogs')

def global_scheduling(spider_global_variable):
    while True:
        if spider_global_variable.global_urlnode_queue.qsize() > 0:
            node = spider_global_variable.global_urlnode_queue.get()
            spider_global_variable.spider_urlnode_queue.put(node)

        '''
            In this function, you can put something interesting code in this,
        The global_scheduling function can get all the url_node, the url_node
        structure in the UrlData.py.
        '''
