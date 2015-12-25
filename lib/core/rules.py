#!/usr/bin/env python
# coding:utf-8
# manning  2015-1-27
import time
import re
import urlparse
import sys
sys.path.append(sys.path[0].split('MSpider')[0] + "MSpider/lib")

import logging
spider_logger = logging.getLogger('MSpiderLogs')

class UrlRuleClass(object):

    """docstring for UrlRule"""

    def __init__(self, SpiderGlobalVariable):
        super(UrlRuleClass, self).__init__()
        self.url_repeat_set = set()
        self.url = ''
        self.spiderglobal = SpiderGlobalVariable

    def check_repeat(self,url):
        if url not in self.url_repeat_set:
            self.url_repeat_set.add(url)
            return True
        return False


    def focus_domain(self,url):
        if len(self.spiderglobal.focus_domain) == 0:
            return True
        t = urlparse.urlparse(url)[1]
        for i in self.spiderglobal.focus_domain:
            if i in t:
                return True
        return False

    def filter_domain(self,url):
        t = urlparse.urlparse(url)[1]
        for i in self.spiderglobal.filter_domain:
            if i in t:
                return False
        return True

    def focus_keyword(self,url):
        if len(self.spiderglobal.focus_keyword) == 0:
            return True
        for i in self.spiderglobal.focus_keyword:
            if i in url:
                return True
        return False

    def filter_keyword(self,url):
        if len(self.spiderglobal.filter_keyword) == 0:
            return True
        for i in self.spiderglobal.filter_keyword:
            if i in url:
                return False
        return True

    def check_filter_and_focus(self,url):
        if self.focus_domain(url) and self.filter_domain(url) and self.focus_keyword(url) and self.filter_keyword(url):
            return True
        return False

    def check_url(self, url):
        if self.check_repeat(url) and self.check_filter_and_focus(url):
            return True
        else:
            return False
