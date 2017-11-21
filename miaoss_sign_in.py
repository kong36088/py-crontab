#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import json

import sys
import random
from time import sleep

import requests
import http.cookiejar as cookiejar

reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.8,en;q=0.6",
    "cache-control": "no-cache",
    "cookie": "", # 放你帐号的cookie，最好修改一下过期时间。这样就很久登陆状态都不会过期了
    "pragma": "no-cache",
    "referer": "https://www.miaoss.cat/user",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36"
}


def date_fmt(fmt="%Y-%m-%d", date=None):
    if not date:
        date = datetime.datetime.now()
    return date.strftime(fmt)


# 写日志
def write_log(file, args, mode='a'):
    with open(file, mode) as f:
        f.write('%s %s\n' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ' '.join(str(x) for x in args)))


def ascii2utf8(string):
    """
    utf8转码
    :type string: str 
    :return: 
    """
    return string.encode('utf-8').decode('unicode_escape')


def start():
    print date_fmt("%Y-%m-%d %H:%M:%S") + " start"

    sleep_time = random.randint(100, 1200)
    print "sleep " + str(sleep_time)
    sleep(sleep_time)

    session = requests.Session()
    session.cookies = cookiejar.LWPCookieJar(filename='cookie')
    session.keep_alive = False
    try:
        session.cookies.load(ignore_discard=True)
    except Exception as e:
        print('Cookie 未能加载')
    finally:
        pass

    req = session.post(url="https://www.miaoss.cat/user/checkin", headers=headers, )
    req.encoding = 'gbk'
    session.cookies.save()
    write_log('./log/miaoss_sign_in.log', (str(req.status_code), ascii2utf8(req.text)))


if __name__ == '__main__':
    start()
