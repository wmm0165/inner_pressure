# -*- coding: utf-8 -*-
# @Time : 2019/11/19 17:53
# @Author : wangmengmeng
from locust import HttpLocust, TaskSet, task

from utils import get_file_content


class ScriptTasks(TaskSet):
    file_content = get_file_content()

    @task
    def send_req(self):
        body = next(self.file_content)
        # self.file_content.__next__()
        headers = {"Content-Type": "text/plain"}
        res = self.client.post("/auditcenter/api/v1/auditcenter", data=body.encode("utf-8"), headers=headers,
                               name="/api/v1/auditcenter")
        # log.info("执行结果：{}".format(res.json()))


class WebsiteUser(HttpLocust):
    task_set = ScriptTasks
    host = "http://10.1.1.71:9999"
    min_wait = 300
    max_wait = 300


# if __name__ == '__main__':
#     os.system("locust -f locust_optimize.py")
