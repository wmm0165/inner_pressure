# -*- coding: utf-8 -*-
# @Time : 2019/11/19 17:53
# @Author : wangmengmeng
from locust import HttpLocust, TaskSet, task
import os
import requests
import time
from common.record_log import log
from concurrent.futures import ThreadPoolExecutor
import queue


class ScriptTasks(TaskSet):
    def req(self, content):
        headers = {"Content-Type": "text/plain"}
        res = self.client.post("/auditcenter/api/v1/auditcenter", data=content.encode("utf-8"), headers=headers)
        log.info("执行结果：{}".format(res.json()))
        # return res

    @task
    def read_file(self):
        # path = r'D:\data\2019-11-02\H0003\receive_path'
        path = '/mnt/sf_tools/py_inner_perssure/testdata/2019-11-03/H0003/receive_path'
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

                with ThreadPoolExecutor(max_workers=8) as executor:
                    while not q.empty():
                        for i in range(4):
                            executor.submit(self.req(q.get()))


class WebsiteUser(HttpLocust):
    task_set = ScriptTasks
    host = "http://10.1.1.71:9999"
    min_wait = 300
    max_wait = 300

# if __name__ == '__main__':
#     sx = SendXml()
#     path = r'D:\data\2019-11-02\H0003\receive_path'
#     sx.read_file(path)
