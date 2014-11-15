#!/usr/bin/env python
# coding:utf-8
# manning  2014-11-7

class DataNode(object):
    def __init__(self,url):
        self.url = url
        self.html = ''
        self.links = []
        self.depth = 1

    def set_html(self,html):
        self.html = html

    def reset_html(self):
        self.html = ''

    def set_links(self,tmp_list):
        self.links.extend(tmp_list)

    def set_depth(self,depth):
        self.depth = depth

    def add_depth(self):
        self.depth += 1