# -*- coding: utf-8 -*-
# @Time : 2019/11/25 22:41
# @Author : wangmengmeng
from locust import TaskSet, HttpLocust, task
import hashlib, json


class SceneOneTaskSet(TaskSet):
    """登录 审核门诊"""

    def login(self):
        username = 'admin'
        password = 'ipharmacare'
        pwd = hashlib.md5().update(password.encode()).hexdigest()
        url = 'http://10.1.1.71:9999/syscenter/api/v1/currentUser'
        params = {"name": username, "password": pwd}
        headers = {'Content-Type': "application/json"}
        self.client.post(url, data=json.dumps(params), headers=headers)

    def setup(self):
        self.login()

    @task
    def one(self):
        pass


class SceneTwoTaskSet(TaskSet):
    """登录 审核住院"""

    @task
    def two(self):
        print("2")


class SceneThreeTaskSet(TaskSet):
    """登录 查看已审门诊"""

    @task
    def three(self):
        print("3")


class SceneFourTaskSet(TaskSet):
    """登录 查看已审住院"""

    @task
    def four(self):
        print("4")


class SceneOne(HttpLocust):
    weight = 4
    task_set = SceneOneTaskSet
    host = "http://www.baidu.com"
    min_wait = 300
    max_wait = 300


class SceneTwo(HttpLocust):
    weight = 4
    task_set = SceneTwoTaskSet
    host = "http://www.baidu.com"
    min_wait = 300
    max_wait = 300


class SceneThree(HttpLocust):
    weight = 1
    task_set = SceneThreeTaskSet
    host = "http://www.baidu.com"
    min_wait = 300
    max_wait = 300


class SceneFour(HttpLocust):
    weight = 1
    task_set = SceneFourTaskSet
    host = "http://www.baidu.com"
    min_wait = 300
    max_wait = 300
