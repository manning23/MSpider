#!/usr/bin/env python
# coding:utf-8
# manning  2014-11-8

import lxml.html
from Fetcher import fetcher
from MyDataNode import DataNode

def crawler(node):
    html = node.html
    url = node.url
    if html == '':
        return
    else:
        '''
        获取页面内的links
        '''
        try:
            tmp = lxml.html.document_fromstring(html)
            tmp.make_links_absolute(url)
            links = tmp.iterlinks()
            link_list = list(set([i[2] for i in links]))
            node.set_links(link_list)
        except Exception, e:
            return 
        '''
        待补充其他操作
        如获取页面title等
        '''
        try:
            pass
        except Exception, e:
            pass 
        node.reset_html()
        return

if __name__ == '__main__':
    t = DataNode("http://www.sina.com.cn")

    fetcher(t)
    print 'static:'
    print len(t.html)
    crawler(t)
    print len(set(t.links))

    print "dynamic:"
    fetcher(t,"dynamic")
    print len(t.html)
    crawler(t)
    print len(set(t.links))

