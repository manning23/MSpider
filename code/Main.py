#!/usr/bin/env python
# coding:utf-8
# manning  2014-11-8

import urlparse
import gevent
import time
from gevent import monkey
from gevent import Greenlet
from gevent import pool
from gevent import queue
from gevent import event
from gevent import Timeout


from Crawler import crawler
from Fetcher import fetcher
from MyDataNode import DataNode
from UrlSimilar import similarity
from BloomFilter import bloomfilter

monkey.patch_all()

class Spider(object):
    def __init__(self, node, concurrent_num = 20,  depth = 3, spider_timeout = 6*3600, spider_type = 'static' , keyword = ''):
        self.concurrent_num = concurrent_num
        self.depth = depth
        self.keyword = keyword
        self.spider_timeout = spider_timeout
        self.spider_type = spider_type
        self.node = node

        self.total_count = 0

        self.work_pool = pool.Pool(self.concurrent_num + 5)


        self.fetcher_queue = queue.Queue(maxsize = self.concurrent_num*10000)
        self.fetcher_flag = True

        self.crawler_queue = queue.Queue(maxsize = self.concurrent_num*10000)
        self.crawler_flag = True

        self.deal_queue = queue.Queue(maxsize = self.concurrent_num*10000)
        self.deal_flag = True

        self.hashtable_size = 10000000
        self.links_hash_table = '0' * self.hashtable_size

        self.url_similar_hashtable_size = 10000000
        self.url_similar_hash_table = '0' * self.url_similar_hashtable_size

        self.ignore_ext = ('js','css','png','jpg','gif','bmp','svg','exif','jpeg','exe','rar','zip','doc','docx','ppt','pptx','pdf','ico')

    def judge_duplication(self,url):
        tmp_list = bloomfilter(url,self.hashtable_size)
        count = 0
        for i in tmp_list:
            if self.links_hash_table[i] == '1':
                count += 1
        if count == 6:
            return True
        else:
            for i in tmp_list:
                self.links_hash_table = self.links_hash_table[:i] + '1' + self.links_hash_table[i+1:]
            return False

    def judge_url_similar(self,url):                #url相似度判断
        if urlparse.urlparse(url)[2][1:].split('.')[-1].lower() not in ['html','htm','shtml']:
            return False
        else:
            value = similarity(url,self.url_similar_hashtable_size)
            if self.url_similar_hash_table[value] != '0': #如果value值存在，则此url相似
                return True
            else:                                       #如果value不存在，存入hash表
                self.url_similar_hash_table = self.url_similar_hash_table[:value] + '1' + self.url_similar_hash_table[value+1:] 
                return False

    def my_fetcher(self):                           #fetcher的工作内容就是从fetcher_queue中取节点，操作后，放入crawler_queue中
        while self.fetcher_flag:
            if not self.fetcher_queue.empty():      #如果不为空
                tmp_node = self.fetcher_queue.get(block = False)
                fetcher(tmp_node,self.spider_type)
                print str(time.ctime()) + ' ' + tmp_node.url
                self.crawler_queue.put(tmp_node)

            else:                                   #如果下载队里为空
                gevent.sleep(0)
        return


    def my_crawler(self):
        while self.crawler_flag:
            if not self.crawler_queue.empty():
                tmp_node = self.crawler_queue.get(block = False)
                crawler(tmp_node)
                self.deal_queue.put(tmp_node)
            else:
                gevent.sleep(0)
        return

    def my_deal(self):                                      #deal函数，主要用作流程上的处理
        while self.deal_flag:
            if not self.deal_queue.empty():
                tmp_node = self.deal_queue.get(block = False)
                if tmp_node.depth > self.depth:             #深度判断
                    continue    
                for i in tmp_node.links:
                    if "http" not in i[:5]:
                        continue
                    elif i.split('.')[-1] in self.ignore_ext:
                        continue
                    elif self.keyword not in i:             #关键字判断
                        continue
                    elif self.judge_duplication(i):       #如果i已经爬取过
                        continue
                    elif self.judge_url_similar(i):
                        continue
                    else:
                        new_node = DataNode(i)
                        new_node.set_depth(tmp_node.depth + 1)
                        self.fetcher_queue.put(new_node)
                        self.total_count += 1
            else:
                gevent.sleep(0)
        return

    def moniter(self):
        count = 0
        flag = True
        while flag:
            if self.deal_flag and self.crawler_flag and self.fetcher_flag:
                if self.fetcher_queue.qsize() == 0 and self.crawler_queue.qsize() == 0 and self.deal_queue.qsize() == 0:
                    count += 1
                    if count == 6:
                        self.deal_flag = False
                        self.crawler_flag = False
                        self.fetcher_flag = False
                        print "finish spider"
                        flag = False
            gevent.sleep(10)
        return 
            


    def run(self):
        self.fetcher_queue.put(self.node)
        for _ in xrange(self.concurrent_num):
            self.work_pool.spawn(self.my_fetcher)
        self.work_pool.spawn(self.my_crawler)
        self.work_pool.spawn(self.my_crawler)
        self.work_pool.spawn(self.my_deal)
        self.work_pool.spawn(self.my_deal)
        self.work_pool.spawn(self.moniter)
        if self.spider_timeout > 0:   
            self.work_pool.join(timeout = self.spider_timeout)
        else:
            self.work_pool.join()


if __name__ == "__main__": 
    mynode = DataNode("http://www.bjut.edu.cn")
    spider = Spider(mynode,spider_type = "static" ,keyword = "bjut" ,depth = 2)
    #spider = Spider(mynode,spider_type = "dynamic" ,keyword = "bistu.edu.cn" ,depth = 2)
    spider.run()















