# -*- coding: utf-8 -*-
# @Time : 2019/7/10 16:23
# @Author : wangmengmeng
"""用户中心批量添加用户"""
import hashlib
import requests
import json
from config.read_config import ReadConfig
import csv
import os


class AddUser:
    def __init__(self):
        self.cf = ReadConfig()
        self.csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'users.csv')
        url = self.cf.get('login', 'address') + '/syscenter/api/v1/currentUser'
        username = self.cf.get('login', 'username')
        passwd = self.cf.get('login', 'password')
        m = hashlib.md5()  # 创建md5对象
        m.update(passwd.encode())  # 生成加密字符串
        password = m.hexdigest()
        params = {"name": username, "password": password}
        self.headers = {'Content-Type': "application/json"}
        self.session = requests.session()
        res = self.session.post(url, data=json.dumps(params), headers=self.headers).json()
        print(res)

    def add_user(self, count):
        """
        添加多个用户
        :param count:  添加用户的数量
        """
        out = open(self.csv_path, 'w', newline='')  # 打开csv文件
        write_csv = csv.writer(out, dialect='excel')  # 定义文件类型为excel类型
        for i in range(1, (count + 1)):
            url = self.cf.get('login', 'address') + '/syscenter/api/v1/auth/addUser'
            user = [("cs" + str(i)), "123456"]  # 用户名和密码
            write_csv.writerow(user)
            params = {
                "dtoUser": {
                    "username": "cs" + str(i),
                    "realname": "测试" + str(i),
                    "password": "123456"
                },
                "drugIdList": [],
                "roleIdList": [88, 91, 89],
                "dtoUserDeptList": [],
                "resourceIdList": [],
                "dtoUserWorknumList": []
            }
            self.session.post(url, data=json.dumps(params), headers=self.headers).json()


if __name__ == '__main__':
    user = AddUser()
    user.add_user(100)
