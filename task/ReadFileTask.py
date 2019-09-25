# -*- coding: utf-8 -*-
# @Time : 2019/9/25 23:08
# @Author : wangmengmeng
import os

from common.record_log import log


class ReadFileTask:
    def __init__(self, file_path, xml_sum, sleep_time, effect_folder, read_date, start_time, end_time):
        self.file_path = file_path
        self.xml_sum = xml_sum
        self.sleep_time = sleep_time
        self.effect_foler = effect_folder
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
        else:
            log.info("this zip file path is not exist filePath:{}".format(self.file_path))

    def is_sleep(self):
        pass
