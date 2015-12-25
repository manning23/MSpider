#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17
"""
MSpider HtmlNode结点类
"""
class HtmlNode(object):
    def __init__(self, url, html, time, depth):
        self.url = url
        self.html = html
        self.time = time
        self.depth = depth
