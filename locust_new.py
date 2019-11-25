# -*- coding: utf-8 -*-
# @Time : 2019/11/23 19:56
# @Author : wangmengmeng
# -*- coding: utf-8 -*-
# @Time : 2019/11/19 17:53
# @Author : wangmengmeng
import os
import queue

from locust import HttpLocust, TaskSet, task


class ScriptTasks(TaskSet):
    def req(self, content):
        headers = {"Content-Type": "text/plain"}
        res = self.client.post("/auditcenter/api/v1/auditcenter", data=content.encode("utf-8"), headers=headers)
        # log.info("执行结果：{}".format(res.json()))
        # return res

    @task
    def read_file(self):
        try:
            body = self.locust.xml_data_queue.get()
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)
        # print(body)
        self.req(content=body)


class WebsiteUser(HttpLocust):
    host = "http://10.1.1.71:9999"
    task_set = ScriptTasks
    xml_data_queue = queue.Queue()
    path = r'F:\Download\2019-11-07\H0003\receive_path'
    # path = '/mnt/sf_tools/py_inner_perssure/testdata/2019-11-02/H0003/receive_path'
    files = os.listdir(path)
    n = 0
    for file in files:
        with open(os.path.join(path, file), mode='r', encoding='utf-8', buffering=True) as f:
            file_content = f.read()
        xml_data_queue.put(file_content)

    min_wait = 300
    max_wait = 300


# if __name__ == '__main__':
#     sx = SendXml()
#     path = r'D:\data\2019-11-02\H0003\receive_path'
#     sx.read_file(path)

if __name__ == '__main__':
    os.system("locust -f locust_new.py --no-web -c 2 -r 1")
