# -*- coding: utf-8 -*-
# @Time : 2019/11/19 13:43
# @Author : wangmengmeng
import os
import requests
from common.record_log import log


class SendXml:
    def __init__(self):
        pass

    def send_xml(self, path):
        url = "http://10.1.1.71:9999/auditcenter/api/v1/auditcenter"
        headers = {"Content-Type": "text/plain"}
        files = os.listdir(path)
        for file in files:
            with open(os.path.join(path, file), mode='r', encoding='utf-8', buffering=True) as f:
                file_content = f.read()
                res = requests.post(url, data=file_content.encode("utf-8"), headers=headers)
                log.info("执行结果：{}".format(res.json()))


if __name__ == '__main__':
    sx = SendXml()
    paths = [r'C:\Users\iphauser\Desktop\data\2019-11-01\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-02\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-03\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-04\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-05\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-06\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-07\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-08\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-09\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-10\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-11\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-12\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-13\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-14\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-15\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-16\H0003\receive_path',
             r'C:\Users\iphauser\Desktop\data\2019-11-17\H0003\receive_path', ]
    # for path in paths:
    #     sx.send_xml(path)
    path = r'D:\ccc'
    sx.send_xml(path)
