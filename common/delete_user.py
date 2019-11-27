# -*- coding: utf-8 -*-
# @Time : 2019/7/10 17:13
# @Author : wangmengmeng

import pymysql
from config.read_config import ReadConfig


class DeleteUser:
    def __init__(self):
        cf = ReadConfig()
        self.host = cf.get('db', 'host')
        self.port = cf.get('db', 'port')
        self.username = cf.get('db', 'username')
        self.passwd = cf.get('db', 'password')
        self.dbname = cf.get('db', 'dbname')
        self.connect = pymysql.Connect(host=self.host, port=int(self.port), user=self.username, passwd=self.passwd,
                                       db=self.dbname,
                                       charset='utf8')
        self.cur = self.connect.cursor()

    def delete_user(self):
        """清除数据库中用户代码以cs开头的用户数据"""
        sql = "DELETE FROM auth_user WHERE username LIKE 'cs%%'"
        self.cur.execute(sql)
        self.connect.commit()  # 修改或删除需要提交事务


if __name__ == '__main__':
    a = DeleteUser()
    a.delete_user()
