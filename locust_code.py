# -*- coding: utf-8 -*-
# @Time : 2019/11/19 17:53
# @Author : wangmengmeng
import os
import queue
import time
from concurrent.futures import ThreadPoolExecutor

from locust import HttpLocust, TaskSet, task

from common.record_log import log


class ScriptTasks(TaskSet):
    def req(self, content):
        headers = {"Content-Type": "text/plain"}
        res = self.client.post("/api/v1/auditcenter", data=content.encode("utf-8"), headers=headers)
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
    task_set = ScriptTasks # 指定一个用户行为
    host = "http://10.1.1.71:9999/auditcenter"
    min_wait = 300 # 模拟用户在执行每个任务之间等待的最小时间，单位为毫秒；
    max_wait = 300 # 模拟用户在执行每个任务之间等待的最大时间，单位为毫秒（min_wait和max_wait默认值为1000，因此，如果没有声明min_wait和max_wait，则locust将在每个任务之间始终等待1秒。

# if __name__ == '__main__':
#     sx = SendXml()
#     path = r'D:\data\2019-11-02\H0003\receive_path'
#     sx.read_file(path)
# locust -f locustfile.py --host=http://192.168.x.xx:80 --no-web -c 1 -r 1
