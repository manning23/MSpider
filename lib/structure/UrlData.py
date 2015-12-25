#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17

class UrlNode(object):
    def __init__(self, url, referer, depth, method = 'get', data = ''):
        self.url = url
        self.referer = referer
        self.method = method
        self.depth = int(depth) + 1
        self.data = data
        self.check_url = None
        self.init_check_url()

    def show(self):
        print self.method
        print self.url
        print self.data
        print '--------------------'

    def init_check_url(self):
        self.check_url = self.url
        
