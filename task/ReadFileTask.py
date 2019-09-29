# -*- coding: utf-8 -*-
# @Time : 2019/9/25 23:08
# @Author : wangmengmeng
import operator
import os
import re
from datetime import datetime

from common.record_log import log


class ReadFileTask:
    def __init__(self, file_path, xml_sum, sleep_time, effect_folder, read_date, start_time, end_time):
        self.file_path = file_path
        self.xml_sum = xml_sum
        self.sleep_time = sleep_time
        self.effect_folder = effect_folder
        self.read_date = read_date
        self.start_time = start_time
        self.end_time = end_time

    def run(self):
        log.info("read file task is beginning......")
        self.is_sleep()
        self.read_zip_file()
        log.info("read file task is end......")

    def read_zip_file(self):
        if self.file_path.exists():
            files = os.listdir(self.file_path)
            if not files:
                for file in files:
                    if ".zip" in os.path.abspath(file):
                        file_date = re.match(".*(\\d{4}-\\d{1,2}-\\d{1,2}).zip", str(file))

                    else:
                        pass
            else:
                log.info("this zip file is empty filePath:{}".format(self.file_path))
        else:
            log.info("this zip file path is not exist filePath:{}".format(self.file_path))

    def read_file(self, file_path, xml_num):
        if not file_path.exists():
            log.info("this txt file path is not exist filePath:{}".format(file_path))
            return
        files = os.listdir(file_path)
        if not files:
            log.info("this txt file is empty filePath:{}".format(file_path))
            return
        try:
            for file in files:
                if os.path.isdir(file):
                    self.read_file(file_path, xml_num)
                elif (file.endswith('txt') or file.endwith('xml')) and self.is_can_read(os.path.abspath(file)):
                    pass
        except:
            pass

    def is_can_read(self, file_path):
        if self.effect_folder in file_path:
            date = re.match(".*(\\d{4}-\\d{1,2}-\\d{1,2}).*", str(file_path))
            if not date and operator.gt(date, self.read_date):
                return True
        else:
            return False

    def is_sleep(self,is_fetch):
        is_sleep = self.is_match_time()




    def is_match_time(self):
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 获取当前时间
        if operator.gt(self.start_time,self.end_time):
            return operator.lt(self.start_time,now_time) or operator.gt(now_time,self.end_time)
        return operator.lt(self.start_time,now_time) or operator.gt(now_time,self.end_time)
        


if __name__ == '__main__':
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now_time)