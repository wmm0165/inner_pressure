# -*- coding: utf-8 -*-
# @Time : 2019/11/20 15:11
# @Author : wangmengmeng
import os
import requests
import time
from common.record_log import log
from concurrent.futures import ThreadPoolExecutor
# 使用线程池
import datetime
import queue


# python2中是Queue，python3中是queue

class SendXml:
    def __init__(self):
        pass

    def read_file(self, path):
        files = os.listdir(path)
        q = queue.Queue()
        n = 0
        for file in files:
            with open(os.path.join(path, file), mode='r', encoding='utf-8', buffering=True) as f:
                file_content = f.read()
            q.put(file_content)
            n += 1
            print(n)
            if n % 100 == 0:
                time.sleep(3)

                with ThreadPoolExecutor(max_workers=3) as executor:
                    while not q.empty():
                        for i in range(2):
                            executor.submit(self.req(q.get()))

    def req(self, content):
        url = "http://10.1.1.71:9999/auditcenter/api/v1/auditcenter"
        headers = {"Content-Type": "text/plain"}
        res = requests.post(url, data=content.encode("utf-8"), headers=headers)
        log.info("执行结果：{}".format(res.json()))
        # return res


if __name__ == '__main__':
    sx = SendXml()
    path = r'D:\data\2019-11-02\H0003\receive_path'
    sx.read_file(path)
