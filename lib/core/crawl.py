#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17
'''
About how to crawl the <a href=""> in the html
'''
import lxml.html
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import urlparse
import chardet
import urllib2
try:
    import re2 as re
except ImportError:
    import re

import random
import time
from fetch import fetch

import logging
spider_logger = logging.getLogger('MSpiderLogs')


def get_url_by_lxml(url,html):
    try:
        if '.js' in urlparse.urlparse(url)[2]:
            return []
        tmp = lxml.html.document_fromstring(urllib2.unquote(html))
        tmp.make_links_absolute(url)
        links = tmp.iterlinks()

        links = [i[2] for i in links]
        return links
    except Exception as e:
        msg = 'Function: get_url_by_lxml, Info: ' + str(e)
        spider_logger.error(msg)
        return []

def check_suffix(url):
    ignore_ext = ['wma', 'png', 'jpeg', 'jpg']
    suffix = urlparse.urlparse(url)[2].split('.')[-1].lower()
    if suffix in ignore_ext:
        return False
    else:
        return True

def check_keyword(domian):
    i = domian
    if i.startswith('javascript:'):
        return False
    if i.startswith('about:'):
        return False
    return True

def modify_url(url):
    i = url
    if '/' not in i and '?' not in i:
        i = i + '/'
    i = 'http://' + i
    return i


def crawl(url,html):
    if len(html) < 10:
        return []
    link_set = set()
    _ = [link_set.add(i) for i in get_url_by_lxml(url,html) if check_keyword(i)]
    get_link_list = [i for i in list(link_set) if check_suffix(i)]

    links = []

    for i in get_link_list:
        data = modify_url_to_structure(i)
        links.append(data)

    return links


def modify_url_to_structure(url):
    method = 'get'
    return (method,url,'')
