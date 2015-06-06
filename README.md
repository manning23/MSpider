Mspider2.0  网页链接爬虫
===========================
 爬虫功能 
-----------------------------------------------------------------------------------------
1. 可控的线程数                                             
2. 可控的爬取深度                                                                   
3. 可控的爬取数量                                                                 
4. 可控的爬取时间                                                     
5. 可控的域名聚焦、过滤（字符支持","(逗号)分割）                                       
6. 可控的关键字聚焦、过滤（字符支持","(逗号)分割）                                                                  
8. URL相似度过滤（可控开关）                                               
9. 3种下载模式                     
10. 3种爬取策略：宽度优先、深度优先、随机优先   
11. 2种运行时的显示模式                                                      
12. 数据存储（数据库为mongo）                                                     
13. 内置起始URL字典
14. 自动选择代理池（待完成）  

v2.0 更新说明
----------------------------
本次更新主要完成了如下内容。

1. 构建全局变量类
2. 构建UrlRule规则类
3. 优化爬虫流程
4. 补全过滤标签
5. 更新相似度检查函数
6. gevent模型



BUG提交、需求提交、批评意见
------------------------------------------------------

 联系 乌云[Manning](http://www.wooyun.org/whitehats/Manning)   
 
 qq 408468023

      
参考文章
-------------------------------------
[《爬虫技术浅析》](http://drops.wooyun.org/tips/3915)—运用技术概述

[《爬虫技术实战》](http://drops.wooyun.org/tips/5462)—Mspider使用实例



效果截图
------------------------------------------------------------
```c
Usage: 
       MMMM   MMMM                              MM                                         
     MMMMMMMMMMMMMMM                          MM MMM       MMMMMMM                         
    MM      M      MM                         M   MM       MM   MM                         
    M               M     MMMMMM  MMMMMMMM    MMMMMM   MMMMMM   MM   MMMMMMMM     MMMMMM   
    M    MM   MM    M   MMM   MM MM      MMM  M   MM  MM    M   MM  MM      MMM  MM    M   
    M    MM   MM    M   M     MMMM         M  M   MM M      M   MM MM   MM    M MM     M   
    M    MM   MM    M  MM    MMMM   MMMM   MM M   MMMM   MMMM   MMMM   MM     MMMM   MMM   
    M    MM   MM    M MM    MM  M   MMMM   MM M   MM M   MMMM   MM M   MMMMMMMMMMM   M     
    M    MM   MM    M M     MM MM   M     MM  M   MM MM        MM  MM      MM   MM   M     
    M    MM   MM    MMM  MMMM  MM   MM   MM   M   MM  MMM    MMM    MMM    MMM  MM   M     
    MMMMMMMMMMMMMMMMM MMMM     MM   MMMMM     MMMMMM    MMMMMM        MMMMMM    MMMMMM     
                               MM   MM                                                     
                                MMMMMM                                                     
                                                                              by Manning

Options:
  Options:
  -h, --help            show this help message and exit
  -u MSPIDER_URL, --url=MSPIDER_URL
                        Start the domain name
  -t MSPIDER_THREADS_NUM, --threads=MSPIDER_THREADS_NUM
                        Number of threads
  --depth=MSPIDER_DEPTH
                        Crawling depth
  --count=MSPIDER_COUNT
                        Crawling number: The default download 100000000 pages
  --time=MSPIDER_TIME   Crawl time: The default crawl for 7 days
  --similarity=MSPIDER_SIMILARITY
                        Similarity check: True   False
  --storage=MSPIDER_STORAGE
                        Storage true save  false don't save
  --spider-model=MSPIDER_MODEL
                        Crawling mode: Static 0  Dynamic 1  Mixed 2
  --spider-policy=MSPIDER_POLICY
                        Crawling strategy: Breadth-first 0  Depth-first 1
                        Random-first 2
  --focus-keyword=MSPIDER_FOCUS_KEYWORD
                        Focus keyword in URL's path
  --filter-keyword=MSPIDER_FILTER_KEYWORD
                        Filter keyword in URL's path
  --filter-domain=MSPIDER_FILTER_DOMAIN
                        Filter domain
  --focus-domain=MSPIDER_FOCUS_DOMAIN
                        Focus domain
  --random-agent=MSPIDER_AGENT
                        like sqlmap --random-agent default is false: no random
  --print-all=MSPIDER_PRINT_ALL
                        mspider_print_all
``` 



