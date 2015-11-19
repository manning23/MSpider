import os
import optparse
import time
from function.server import server
from config.config import *

def main():
    global DOWNLOAD_MODE
    global THREAD_NUM
    global KEY_WORD
    global FETCH_TIME
    global SPIDER_PROXY
    global START_URLS
    global IGNORE_KEY_WORD

    photo = """
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
                                                                              by Manning"""

    usage = photo
    parser = optparse.OptionParser(usage=usage)  #帮助文档的 usage项目 是 上面那张图片，666
    #这样就没有了自带的usage ,推荐使用description=.
    parser.add_option("-u", "--url",#命令行参数名称，可选
                  dest = "url", #输出的时候的名字
                  default = 'http://www.bistu.edu.cn', #默认值
                  help="Start the domain name")#属性用法帮助

    parser.add_option("-t", "--thread", 
                  dest = "threads_num", 
                  default = 10, 
                  help="Number of threads") 

    parser.add_option("--depth", 
                  dest = "depth", 
                  default = 1000, 
                  help="Crawling depth") 

    parser.add_option("--model",
                  dest = "model", 
                  default = 0, 
                  help='''Crawling mode: Static 0  Dynamic 1  Mixed 2''') 

    parser.add_option("--policy",
                  dest = "policy", #？这个地方改成 choices=["1","2","3"]更好一点
                  default = 0, 
                  help="Crawling strategy: Breadth-first 0  Depth-first 1  Random-first 2") 

    parser.add_option("-k", "--keyword",
                  dest = "keyword", #？这个应该是 action ="append"更好一点。接受多个参数，成为列表
                  default = 'bistu.edu', 
                  help="Focusing on the keywords in host") 

    parser.add_option("--time", 
                  dest = "fetch_time", 
                  default = 3600*24*7, 
                  help="Crawl time: The default crawl for 7 days") 

    parser.add_option("--count", 
                  dest = "fetch_count", 
                  default = 1000*1000, 
                  help="Crawling number: The default download 100000000 pages") 

    parser.add_option("--proxy", action="store_true", 
                  dest = "proxy", 
                  default = False, #推荐用法是： action="store_Flase" 
                  help="The proxy pattern")

    parser.add_option("--ignore",
                  dest="ignore_keyword", 
                  default = 'bbs', 
                  help="Filter keyword in URL's host or path")  

    parser.add_option("--focus",
                  dest="focus_keyword", 
                  default = '', 
                  help="Focus keyword in URL's path")  

    parser.add_option("--storage",
                  dest="storage_model", 
                  default = 1, 
                  help="Storage mode: A small model 1  Large schemas 0  Don't store  3") 

    parser.add_option("--similarity",
                  dest="similarity", 
                  default = 0, #用true和false更好理解
                  help="Similarity check: True 0  False 1") 
    '''
    parser.add_option("-s", "--zdbk", action="store_true", 
                  dest="zdcl", 
                  default=False, 
                  help="write zdbk data to oracle db") 
    '''

    (options, args) = parser.parse_args()#把解析到的参数变成元组，也可以用vars(args)变成字典。

    
    
    download_mode = int(options.model)#得到参数并格式化，也可以add_option中加入type='int'。
    threads_num = int(options.threads_num)
    keyword = set_key_word(options.keyword)
    fetch_time = int(options.fetch_time)
    spider_proxy = options.proxy
    start_urls = set_start_urls(options.url)
    crawl_depth = int(options.depth)
    fetch_mode = int(options.policy)
    fetch_count = int(options.fetch_count)
    storage_model = int(options.storage_model)
    similarity = int(options.similarity)
    ignore_keyword = list(set(IGNORE_KEY_WORD + options.ignore_keyword.split(',')))
    focus_keyword = list(set(options.focus_keyword.split(',')))
     
    #print options 用 python run.py 调用的时候打印
    
    print photo
    #把这些参数传入 function.server模块的server方法。
    server(threads_num,start_urls,fetch_time,keyword,ignore_keyword,download_mode,crawl_depth,fetch_count,fetch_mode,storage_model,similarity,focus_keyword)

if __name__ == "__main__": 
    main()

