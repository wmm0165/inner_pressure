# -*- coding: utf-8 -*-
# @Time : 2019/11/25 22:41
# @Author : wangmengmeng
from locust import TaskSet, HttpLocust, task


class SceneOneTaskSet(TaskSet):
    """登录 审核门诊"""

    @task
    def one(self):
        print("1")


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
