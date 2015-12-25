#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17
import sys
sys.path.append(sys.path[0].split('MSpider')[0] + "MSpider")
from lib.core.fetch import fetch


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print fetch(url)
