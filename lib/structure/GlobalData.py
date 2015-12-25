#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17
"""
MSpider 全局变量
"""

import Queue
import urlparse
import time

class MSpiderGlobalVariable(object):
    def __init__(self, variable_dict):
        self.variable_dict = variable_dict

        self.start_url = ["http://www.baidu.com"]
        self.focus_keyword = []
        self.filter_keyword = []
        self.focus_domain = []
        self.filter_domain = []

        self.threads = 10
        self.spider_use_gevent = False
        self.depth = 10
        self.count = 1000
        self.time = 24 * 3600
        self.referer = ''
        self.cookies = ''
        self.spider_model = 0
        self.spider_policy = 0

        self.random_agent = False
        self.print_all = True
        self.spider_use_gevent = False

        self.ignore_ext = []
        self.spider_proxy = True
        self.spider_proxy_ip_pool = []
        self.download_rate = 50
        self.fetch_time_interval = 5

        '''
        全局控制参数
        '''

        self.exit_flag_count = 0
        self.global_urlnode_queue = Queue.Queue()
        self.global_unfocus_urlnode_queue = Queue.Queue()
        self.spider_urlnode_queue = None
        self.htmlnode_queue = Queue.Queue()
        self.store_queue = Queue.Queue()
        self.parse_variable_dict()
        self.set_urlnode_queue()

        self.spider_logger = None

        '''
        爬虫任务参数
        '''
        self.total_count = 0
        self.refuse_count = 0

        self.start_time = time.time()
        self.end_time = None
        self.start_ctime = time.ctime()
        self.end_ctime = None
        self.maintain_time = None

        self.task_name = None



    def set_urlnode_queue(self):
        if self.spider_policy == 1:
            self.spider_urlnode_queue = Queue.LifoQueue()
        elif self.spider_policy == 2:
            self.spider_urlnode_queue = Queue.PriorityQueue()
        else:
            self.spider_urlnode_queue = Queue.Queue()

    def parse_variable_dict(self):
        self.start_url = self.variable_dict['start_url']
        self.focus_keyword = self.variable_dict['focus_keyword']
        self.filter_keyword = self.variable_dict['filter_keyword']
        self.focus_domain = self.variable_dict['focus_domain']
        self.filter_domain = self.variable_dict['filter_domain']
        self.threads = self.variable_dict['threads']
        self.depth = self.variable_dict['depth']
        self.count = self.variable_dict['count']
        self.time = self.variable_dict['time']
        self.referer = self.variable_dict['referer']
        self.cookies = self.variable_dict['cookies']
        self.spider_model = self.variable_dict['spider_model']
        self.spider_policy = self.variable_dict['spider_policy']
        self.random_agent = self.variable_dict['random_agent']
        self.print_all = self.variable_dict['print_all']
