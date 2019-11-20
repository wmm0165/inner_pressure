# -*- coding: utf-8 -*-
# @Time : 2019/11/19 13:43
# @Author : wangmengmeng
import os
import requests
import time
from common.record_log import log
import datetime


class SendXml:
    def __init__(self):
        pass

    def send_xml(self, path):
        start = datetime.datetime.now()
        url = "http://10.1.1.71:9999/auditcenter/api/v1/auditcenter"
        headers = {"Content-Type": "text/plain"}
        files = os.listdir(path)
        n = 0
        for file in files:

            with open(os.path.join(path, file), mode='r', encoding='utf-8', buffering=True) as f:
                file_content = f.read()
                res = requests.post(url, data=file_content.encode("utf-8"), headers=headers)
                log.info("执行结果：{}".format(res.json()))

            n += 1
            if n % 100 == 0:
                time.sleep(10)
        end = datetime.datetime.now()
        print(end - start)


if __name__ == '__main__':
    sx = SendXml()
    paths = [r'C:\Users\iphauser\Desktop\data\2019-11-01\H0003\receive_path']
    # for path in paths:
    #     sx.send_xml(path)
    path = r'D:\data\2019-11-02\H0003\receive_path'
    sx.send_xml(path)
