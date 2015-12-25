# MSpider

MSpider is a pure web crawler, you can use it to collect all kinds of information.


## Installation

In Ubuntu, you need to install some libraries.

You can use pip or easy_install or apt-get to do this.

- lxml
- chardet
- splinter
- gevent
- phantomjs

## Example

1. Use MSpider collect the vulnerability information on the wooyun.org.
```
	python mspider.py -u "http://www.wooyun.org/bugs/" --focus-domain "wooyun.org" --filter-keyword "xxx" --focus-keyword "bugs" -t 15 --random-agent true
```


2. Use MSpider collect the news information on the news.sina.com.cn.
```
	python mspider.py -u "http://news.sina.com.cn/c/2015-12-20/doc-ifxmszek7395594.shtml" --focus-domain "news.sina.com.cn"  -t 15 --random-agent true
```
## ToDo

1. Crawl and storage of information.
2. Distributed crawling.