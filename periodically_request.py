#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import json

import sys
import time

import requests

reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

headers = {
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Proxy-Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}


# 写日志
def write_log(file, args, mode='a'):
    f = open(file, mode)
    log_content = '%s %s\n' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ' '.join(str(x) for x in args))
    print log_content
    f.write(log_content)
    f.close()


def date_fmt(fmt="%Y-%m-%d", date=None):
    if not date:
        date = datetime.datetime.now()
    return date.strftime(fmt)


def ascii2utf8(string):
    """
    utf8转码
    :type string: str
    :return:
    """
    return string.encode('utf-8').decode('unicode_escape')


def send_req(url='', data=None, head=None):
    req, code, body = '', '', ''
    try:
        if data:
            req = requests.post(url=url, headers=head, data=data, timeout=120)
        else:
            req = requests.get(url=url, headers=head, timeout=120)
        req.encoding = 'utf8'
        body = ascii2utf8(req.text)
        # body = req.text
        code = str(req.status_code)
        write_log('./log/periodically_request.log', (data, code, body))
    except Exception as err:
        print err
    return req, code, body


def start():
    print date_fmt("%Y-%m-%d %H:%M:%S") + " start"

    cookie = ""
    urls = [
        'http://zhihu.jwlchina.cn/get_count',
        'http://zhihu.jwlchina.cn/get_sex_count',
        'http://zhihu.jwlchina.cn/get_school_count',
        'http://zhihu.jwlchina.cn/get_trade_count',
        'http://zhihu.jwlchina.cn/get_location_count',
        'http://zhihu.jwlchina.cn/get_company_count',
        'http://zhihu.jwlchina.cn/get_agree_count',
        'http://zhihu.jwlchina.cn/get_follower_count',
        'http://zhihu.jwlchina.cn/get_nickname_count',
        'http://zhihu.jwlchina.cn/get_job_count'
    ]
    for url in urls:
        headers['Cookie'] = cookie
        req, code, body = send_req(url, None, headers)

    print date_fmt("%Y-%m-%d %H:%M:%S") + " end"


if __name__ == '__main__':
    start()
