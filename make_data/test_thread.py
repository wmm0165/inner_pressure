# -*- coding: utf-8 -*-
# @Time : 2019/9/23 14:18
# @Author : wangmengmeng

# 目的：通过调用接口批量造数据，考虑到性能问题需要使用线程池
# 总数据量为两个for循环的乘积

from concurrent.futures import ThreadPoolExecutor
import time
import requests
import random
from datetime import datetime


def test():
    url = "http://10.1.1.178:9999/auditcenter/api/v1/auditcenter"
    headers = {"Content-Type": "text/plain"}
    ts = int(time.mktime(time.strptime(datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")))
    change_after = ts + random.randint(1, 10000000)
    change_data = {"{{ts}}": str(change_after), "{{dt}}": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}
    with open('a', encoding="utf-8") as fp:
        body = fp.read()
    ss = body
    for k in change_data:
        ss = ss.replace(k, change_data[k])
    print(ss)
    requests.post(url, data=ss.encode("utf-8"), headers=headers)


def looptest():
    for i in range(100):
        test()


with ThreadPoolExecutor(max_workers=10) as executor:
    for i in range(5):
        executor.submit(looptest)
