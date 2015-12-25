#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17
"""
MSpider 任务初始化
"""
import urlparse

def get_focus_info(url):
    if url.startswith('http'):
        netloc = urlparse.urlparse(url)[1]
        info = '.'.join(netloc.split('.')[1:])
        return info
    else:
        return url


def focus_domain(spider_global_variable):
    if len(spider_global_variable.focus_domain) == 0 and len(spider_global_variable.start_url) > 0:
        for i in spider_global_variable.start_url:
            spider_global_variable.focus_domain.append(get_focus_info(i))
