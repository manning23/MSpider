#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17
"""
MSpider 日志记录
"""
import logging
import sys

def init_spider_log(spider_global_variable):

    '''
    logs msg定义如下
    Function: init_spider_log, Info: xxx
    '''

    spider_logger = logging.getLogger('MSpiderLogs')
    spider_logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")

    console_handler.setFormatter(formatter)

    spider_logger.addHandler(console_handler)

    spider_global_variable.spider_logger = spider_logger
    spider_logger.info("Welcome to Mspider !!!")
    spider_logger.info("---------------------------")
