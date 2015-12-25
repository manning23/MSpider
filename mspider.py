#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-17
"""
MSpider 起始文件
"""
import optparse
import sys

from lib.structure.GlobalData import MSpiderGlobalVariable
from lib.common.initializtion import init_dict
from lib.common.logs import init_spider_log
from lib.common.focus import focus_domain
from lib.server.server import global_server

import logging
spider_logger = logging.getLogger('MSpiderLogs')

def main():
    usage = '''
  __  __  _____       _     _
 |  \/  |/ ____|     (_)   | |
 | \  / | (___  _ __  _  __| | ___ _ __
 | |\/| |\___ \| '_ \| |/ _` |/ _ \ '__|
 | |  | |____) | |_) | | (_| |  __/ |
 |_|  |_|_____/| .__/|_|\__,_|\___|_|
               | |
               |_|
                        Author: Manning23
    '''
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-u", "--url",
                      dest="mspider_url",
                      default='http://www.baidu.com',
                      help='''Target URL (e.g. "http://www.site.com/")''')

    parser.add_option("-t", "--threads",
                      dest="mspider_threads_num",
                      default=10,
                      help="Max number of concurrent HTTP(s) requests (default 10)")

    parser.add_option("--depth",
                      dest="mspider_depth",
                      default=1000,
                      help="Crawling depth")

    parser.add_option("--count",
                      dest="mspider_count",
                      default=1000 * 1000,
                      help="Crawling number")

    parser.add_option("--time",
                      dest="mspider_time",
                      default=3600 * 24 * 7,
                      help="Crawl time")

    parser.add_option("--referer",
                      dest="mspider_referer",
                      default='',
                      help="HTTP Referer header value")

    parser.add_option("--cookies",
                      dest="mspider_cookies",
                      default='',
                      help="HTTP Cookie header value")

    parser.add_option("--spider-model",
                      dest="mspider_model",
                      default=0,
                      help='''Crawling mode: Static_Spider: 0  Dynamic_Spider: 1  Mixed_Spider: 2''')

    parser.add_option("--spider-policy",
                      dest="mspider_policy",
                      default=2,
                      help="Crawling strategy: Breadth-first 0  Depth-first 1  Random-first 2")

    parser.add_option("--focus-keyword",
                      dest="mspider_focus_keyword",
                      default='',
                      help="Focus keyword in URL")

    parser.add_option("--filter-keyword",
                      dest="mspider_filter_keyword",
                      default='',
                      help="Filter keyword in URL")

    parser.add_option("--filter-domain",
                      dest="mspider_filter_domain",
                      default='',
                      help="Filter domain")

    parser.add_option("--focus-domain",
                      dest="mspider_focus_domain",
                      default='',
                      help="Focus domain")

    parser.add_option("--random-agent",
                      dest="mspider_agent",
                      default=False,
                      help="Use randomly selected HTTP User-Agent header value")

    parser.add_option("--print-all",
                      dest="mspider_print_all",
                      default=True,
                      help="Will show more information")




    (options, args) = parser.parse_args()
    print usage
    variable_dict = init_dict(options)

    spider_global_variable = MSpiderGlobalVariable(variable_dict)

    focus_domain(spider_global_variable)

    init_spider_log(spider_global_variable)

    global_server(spider_global_variable)




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt, e:
        print '\nBreak out.'
        sys.exit()
