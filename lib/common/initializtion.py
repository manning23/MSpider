#!/usr/bin/python
#-*-coding:utf-8-*-
#Author : Manning
#Date : 2015-10-18
import urlparse
from common import get_absolute_path

def check_word_has_not_meaning(word):
    '''
    return True
    '''
    has_number = False
    has_letter = False

    for i in xrange(10):
        if str(i) in word:
            has_number = True
            break
    try:
        int(word)
    except Exception as e:
        has_letter = True

    if len(word) > 3 and has_letter and has_number :
        return True
    else:
        return False


def set_domain(strs):
    '''
    可以处理的格式
    1, http://abc.baidu.com/asdas
    2, abc.baidu.com
    3, 1.1.1.1  return ''
    '''
    host = ''
    domain = ''
    if 'http://' in strs:
        host = urlparse.urlparse(strs)[1].split(':')[0]
    else:
        host = strs
    keyword_list = host.split('.')
    if len(keyword_list) == 2:
        domain = host

    elif len(keyword_list) == 3:
        if 'com.cn' in host:
            domain = host
        elif 'net.cn' in host:
            domain = host
        else:
            domain = '.'.join(host.split('.')[1:])

    elif len(keyword_list) > 3:
        count = 0
        for i in keyword_list:
            try:
                int(i)
                count += 1
            except Exception, e:
                break
        if count == 4:
            domain = ''
        else:
            if keyword_list[-1] == 'cn' and keyword_list[-2] in ['com', 'edu', 'gov', 'org', 'net']:
                domain = '.'.join(keyword_list[-3:])
            elif keyword_list[-1] in ['com', 'net', 'org','cc','me']:
                domain = '.'.join(keyword_list[-2:])
            elif keyword_list[-1] == 'cn':
                domain = '.'.join(keyword_list[-2:])
            else:
                domain = host
    return domain


def deal_url(start_urls):
    temp_url_list = start_urls.split(',')
    total_url_list = []
    url_list = []
    addr = get_absolute_path() + 'lib/data/allurl.txt'
    for i in open(addr).readlines():
        while True:
            if i[-1] in ['\r','\n']:
                i = i[:-1]
            else:
                break
        url = i
        if not url.startswith('http://'):
            url = 'http://' + url

        if url.endswith('/'):
            url = url[:-1]
        total_url_list.append(url)

    for i in temp_url_list:
        if i.startswith('http://'):
            url_list.append(i)
        else:
            if i.endswith('/'):
                url = i[:-1]
            else:
                url = i
            for j in total_url_list:
                keyword_j = set_domain(j)
                if url in keyword_j:
                    url_list.append(j)
    url_list = sorted(list(set(url_list)))
    new_list = []
    for i in url_list:
        netloc = urlparse.urlparse(i)[1]
        netloc_list = netloc.split('.')
        if len(netloc_list) == 3:
            if len(netloc_list[0]) > 10:
                continue
            else:
                new_list.append(i)
        elif len(netloc_list) == 4:
            if check_word_has_not_meaning(netloc_list[0]):
                continue
            else:
                new_list.append(i)
        elif len(netloc_list) == 5:
            if check_word_has_not_meaning(netloc_list[0]):
                continue
            elif check_word_has_not_meaning(netloc_list[1]):
                continue
            else:
                new_list.append(i)

    return new_list


def deal_common_strs(words):
    if len(words) == 0:
        return []
    else:
        return words.split(',')

def deal_strs(words):
    if len(words) == 0:
        return ''
    else:
        return words

def deal_common_int(num):
    num = str(num).split('.')[0]
    try:
        int(num)
    except Exception, e:
        raise e
    return int(num)


def deal_common_boolean(boolean):
    boolean = str(boolean).lower()
    if boolean == 'true':
        return True
    elif boolean == '1':
        return True
    elif boolean == '0':
        return False
    else:
        return False



def init_dict(options):
    variable_dict = {
        "start_url": deal_url(options.mspider_url),

        "threads": deal_common_int(options.mspider_threads_num),
        "depth": deal_common_int(options.mspider_depth),
        "count": deal_common_int(options.mspider_count),
        "time": deal_common_int(options.mspider_time),
        'referer': options.mspider_referer,
        'cookies': options.mspider_cookies,

        "spider_model": deal_common_int(options.mspider_model),
        "spider_policy": deal_common_int(options.mspider_policy),

        "focus_keyword": deal_common_strs(options.mspider_focus_keyword),
        "filter_keyword": deal_common_strs(options.mspider_filter_keyword),
        "focus_domain": deal_common_strs(options.mspider_focus_domain),
        "filter_domain": deal_common_strs(options.mspider_filter_domain),

        "random_agent": deal_common_boolean(options.mspider_agent),
        'print_all': deal_common_boolean(options.mspider_print_all),

    }
    return variable_dict
