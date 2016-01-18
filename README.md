# MSpider

## Talk

You can join the QQ Group of 153691452, we can talk about MSpider.


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

## MSpider's help

```
Usage:
  __  __  _____       _     _
 |  \/  |/ ____|     (_)   | |
 | \  / | (___  _ __  _  __| | ___ _ __
 | |\/| |\___ \| '_ \| |/ _` |/ _ \ '__|
 | |  | |____) | |_) | | (_| |  __/ |
 |_|  |_|_____/| .__/|_|\__,_|\___|_|
               | |
               |_|
                        Author: Manning23


Options:
  -h, --help            show this help message and exit
  -u MSPIDER_URL, --url=MSPIDER_URL
                        Target URL (e.g. "http://www.site.com/")
  -t MSPIDER_THREADS_NUM, --threads=MSPIDER_THREADS_NUM
                        Max number of concurrent HTTP(s) requests (default 10)
  --depth=MSPIDER_DEPTH
                        Crawling depth
  --count=MSPIDER_COUNT
                        Crawling number
  --time=MSPIDER_TIME   Crawl time
  --referer=MSPIDER_REFERER
                        HTTP Referer header value
  --cookies=MSPIDER_COOKIES
                        HTTP Cookie header value
  --spider-model=MSPIDER_MODEL
                        Crawling mode: Static_Spider: 0  Dynamic_Spider: 1
                        Mixed_Spider: 2
  --spider-policy=MSPIDER_POLICY
                        Crawling strategy: Breadth-first 0  Depth-first 1
                        Random-first 2
  --focus-keyword=MSPIDER_FOCUS_KEYWORD
                        Focus keyword in URL
  --filter-keyword=MSPIDER_FILTER_KEYWORD
                        Filter keyword in URL
  --filter-domain=MSPIDER_FILTER_DOMAIN
                        Filter domain
  --focus-domain=MSPIDER_FOCUS_DOMAIN
                        Focus domain
  --random-agent=MSPIDER_AGENT
                        Use randomly selected HTTP User-Agent header value
  --print-all=MSPIDER_PRINT_ALL
                        Will show more information
```
