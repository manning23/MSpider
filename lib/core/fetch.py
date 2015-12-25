#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17
'''
About how to get html.
'''

import requests
import urlparse
import time
import random
import urllib2
from splinter import Browser

import sys
sys.path.append(sys.path[0].split('MSpider')[0] + "MSpider/lib")

import logging
spider_logger = logging.getLogger('MSpiderLogs')


def html_pretreatment(html):
    html = html.lower()
    html = urllib2.unquote(html)
    return html


def fetch(url, spider_model=0, fetch_time_interval=1, set_random_agent=True, set_referer=False, set_cookies=False):
    try:
        spider_model = spider_model
        fetch_time_interval = fetch_time_interval
        random_agent = random_agent
    except Exception, e:
        spider_model = 0
        fetch_time_interval = 1
        random_agent = False

    myheaders = dict()
    if random_agent:
        myheaders['Agent'] = random_http_header()
    else:
        myheaders['Agent'] = 'MSpider'

    if set_referer:
        myheaders['Referer'] = set_referer

    if set_cookies:
        myheaders['Cookie'] = set_cookies

    returnhtml = ''

    if spider_model == 0:
        # Static Model
        try:
            response = requests.get(url, timeout=15, headers=myheaders, allow_redirects=False)
            if response.status_code == 200:
                returnhtml = response.content
            else:
                return ""
        except Exception, e:
            msg = 'Function: fetch_0, Info: ' + str(e)
            spider_logger.error(msg)
            return ""
    elif spider_model == 1:
        # Dynamic Model
        try:
            browser = Browser(driver_name='phantomjs', user_agent=myheaders['User-Agent'], load_images=False)
            browser.visit(url)
            html = browser.html
            browser.quit()
            returnhtml = html
        except Exception, e:
            msg = 'Function: fetch_1, Info: ' + str(e)
            spider_logger.error(msg)
            return ""
    else:
        return ""

    if len(returnhtml) < 10:
        return ''

    html = html_pretreatment(returnhtml).decode('gb2312','ignore')
    time.sleep(fetch_time_interval)  # 抓取时间间隔

    return html


def random_http_header():
    user_agents = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
    ]
    return random.choice(user_agents)
