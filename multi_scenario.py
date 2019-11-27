# -*- coding: utf-8 -*-
# @Time : 2019/11/25 22:41
# @Author : wangmengmeng
import hashlib
import json
import os
import queue
import random
from locust import TaskSet, HttpLocust, task
from common.utils import get_file_content
from config.read_config import ReadConfig


class SceneOneTaskSet(TaskSet):
    file_content = get_file_content()

    def login(self):
        """登录系统"""
        param = self.locust.user_queue.get()
        params = {"name": param['username'], "password": param['password']}
        print(params)
        headers = {'Content-Type': "application/json"}
        self.client.post('/syscenter/api/v1/currentUser', data=json.dumps(params), headers=headers)
        self.client.get('/auditcenter/api/v1/startAuditWork')

        # def start_sf(self):
        """开始审方"""
        self.client.get('/auditcenter/api/v1/startAuditWork')

    def on_start(self):  # 每个虚拟用户执行操作时运行
        self.login()
        # self.start_sf()

    @task(3)
    def audit_ipt(self):
        """审核住院任务: 1.查询待审住院任务，随机获取页面数据的engineid；2.审核审核该引擎id的数据"""
        headers = {'Content-Type': "application/json"}
        param = {}
        res = self.client.post('/auditcenter/api/v1/ipt/selNotAuditIptList', data=json.dumps(param).encode("utf-8"),
                               headers=headers)
        print("selNotAuditIptList", res.json())
        if (res.json())['data']['engineInfos']:
            engineids = [i['id'] for i in (res.json())['data']['engineInfos']]
            print(engineids)
            random_engineid = random.choice(engineids)
            orderlist = self.client.get('/auditcenter/api/v1/ipt/orderList' + '?id=' + str(random_engineid),
                                        name='/auditcenter/api/v1/ipt/orderList').json()
            print("orderlist: \"",orderlist,"\"")
            # gps = list(orderlist['data'].keys())[0] # 获取组号
            gp = [i for i in list(orderlist['data'].keys()) if orderlist['data'][i][0]['auditMarkStatus'] is None]
            non_gp = [i for i in list(orderlist['data'].keys()) if orderlist['data'][i][0]['auditMarkStatus'] is not None]
            print("gp ---------", gp)
            print("non_gp -----", non_gp)
            para = {
                "groupOrderList": [{
                    "auditBoList": [],
                    "groupNo": gp[0],
                    "auditInfo": "必须修改",
                    "auditStatus": 0,
                    "engineId": random_engineid,
                    "orderType": 1
                }]
            }
            self.client.post('/auditcenter/api/v1/ipt/auditSingle', data=json.dumps(para).encode("utf-8"), headers=headers)

    @task
    def query_ipt(self):
        """查询已审住院"""
        param = {
            "drugCondition": {
                "drugCodeList": []
            },
            "startTime": 1574611200000,
            "endTime": 1574697599000,
            "zoneId": [],
            "pageSize": 20,
            "page": 1
        }
        headers = {'Content-Type': "application/json"}
        res = self.client.post("/auditcenter/api/v1/ipt/all/iptList", data=json.dumps(param), headers=headers)
        print(res)

    @task(3)
    def query_auth(self):
        """查询已审门诊"""
        params = {
            "drugCondition": {
                "drugCodeList": []
            },
            "startTime": 1574611200000,
            "endTime": 1574783999000,
            "zoneId": [],
            "pageSize": 20,
            "page": 1
        }
        headers = {'Content-Type': "application/json"}
        res = self.client.post("/auditcenter/api/v1/opt/all/optRecipeList", data=json.dumps(params),headers=headers).json()
        print(res)


class SceneOne(HttpLocust):
    task_set = SceneOneTaskSet
    rc = ReadConfig()
    host = rc.get('login', 'address')
    user_queue = queue.Queue()
    password = '123456'
    m = hashlib.md5()  # 创建md5对象
    m.update(password.encode())  # 生成加密字符串
    pwd = m.hexdigest()
    for i in range(1, 50):
        param = {
            "username": "cs%s" % i,
            "password": "%s" % pwd
        }
        user_queue.put(param)
    min_wait = 300
    max_wait = 300


if __name__ == '__main__':
    # os.system("locust -f multi_scenario.py --no-web -c 4 -r 2 --logfile=logs/locust.log")  # 无web界面执行脚本
    os.system("locust -f multi_scenario.py")
