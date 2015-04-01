#!/usr/bin/env python
# coding:utf-8
# manning  2014-11-7
import time
import random
class UrlNode(object):
    def __init__(self,url,src_url,html_length,time,html_title,depth):
        self.url = url
        self.src_url = src_url
        self.html_length = html_length
        self.depth = int(depth) + 1
        self.time = time
        self.html_title = ''


class HtmlNode(object):
    def __init__(self,url,html,time,depth):
        self.url = url
        self.html = html
        self.time = time
        self.depth = depth

