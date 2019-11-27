# -*- coding: utf-8 -*-
# @Time : 2019/8/2 16:14
# @Author : wangmengmeng
import datetime
import time
import requests
import os
from config.read_config import ReadConfig
import random
from threading import Timer


class SendData:
    def __init__(self):
        self.conf = ReadConfig()
        group_no = random.randint(1, 1000000)
        cgroup_no = random.randint(1, 1000000)
        ggroup_no = random.randint(1, 1000000)
        self.change_data = {"{{ts}}": str(self.get_ts(0, 0)),  # 今天时间戳
                            "{{tf2}}": str(self.get_ts(-1, -2)),
                            "{{tf1}}": str(self.get_ts(-1, -1)),
                            "{{t}}": str(self.get_ts(-1, 0)),  # 昨天时间戳
                            "{{d}}": str(self.get_date(-1, 0)),  # 昨天时间
                            "{{tf3}}": str(self.get_ts(-1, -3)),
                            "{{df4}}": str(self.get_date(-1, -4)),
                            "{{tb1}}": str(self.get_ts(-1, +1)),
                            "{{db1}}": str(self.get_date(-1, +1)),
                            "{{dtb1}}": str(self.get_date(+1, 0)),  # 明天时间
                            "{{gp}}": str(group_no),
                            "{{cgp}}": str(cgroup_no),
                            "{{ggp}}": str(ggroup_no),
                            "{{df6}}": str(self.get_date(-1, -6)),
                            "{{df3}}": str(self.get_date(-1, -3)),
                            "{{df2}}": str(self.get_date(-1, -1)),
                            "{{df1}}": str(self.get_date(-1, -1)),
                            "{{dt}}": str(self.get_date(0, 0)),  # 今天时间
                            "{{f5}}": str(self.get_date(-5, 0)),
                            "{{f4}}": str(self.get_date(-4, 0)),
                            "{{f3}}": str(self.get_date(-3, 0)),
                            "{{f2}}": str(self.get_date(-2, 0)),
                            }

    # 获取日期格式为%Y-%m-%d %H:%M:%S：，n可取0（表示当前日期），正（表示当前日期+n天），负（表示当前日期-n天）
    def get_ymd(self, d, h):
        date = ((datetime.datetime.now() + datetime.timedelta(days=d)) + datetime.timedelta(hours=h)).strftime(
            "%Y-%m-%d")
        return date

    def get_date(self, d, h):
        date = ((datetime.datetime.now() + datetime.timedelta(days=d)) + datetime.timedelta(hours=h)).strftime(
            "%Y-%m-%d %H:%M:%S")
        return date

    # 获取指定日期的时间戳
    def get_ts(self, d, h):
        date = ((datetime.datetime.now() + datetime.timedelta(days=d)) + datetime.timedelta(hours=h)).strftime(
            "%Y-%m-%d %H:%M:%S")
        ts = int(time.mktime(time.strptime(date, "%Y-%m-%d %H:%M:%S")))  # 获取10位时间戳
        # ts = int(time.mktime(time.strptime(date, "%Y-%m-%d %H:%M:%S"))) * 1000   # 获取13位时间戳
        return ts

    def send_data(self, **change):
        xml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', '医嘱一')
        send_data_url = self.conf.get('login', 'address') + '/auditcenter/api/v1/auditcenter'
        headers = {"Content-Type": "text/plain"}
        print(xml_path)
        with open(xml_path, encoding="utf-8") as fp:
            body = fp.read()
        ss = body
        for k in change:
            ss = ss.replace(k, change[k])
        print(ss)
        requests.post(url=send_data_url, data=ss.encode("utf-8"), headers=headers)


if __name__ == '__main__':
    while True:
        time.sleep(2)
        for i in range(1, 3):
            sd = SendData()
            sd.send_data(**sd.change_data)


