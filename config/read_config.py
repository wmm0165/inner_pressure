# -*- coding: utf-8 -*-
# @Time : 2019/9/25 22:45
# @Author : wangmengmeng
import os
from configparser import ConfigParser

from common.record_log import log


class ReadConfig():
    # 实例化ConfigParser 并加载配置文件
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        configfile = os.path.join(path, 'config.ini')
        self.conf = ConfigParser()
        log.info('开始解析配置文件...')
        self.conf.read(configfile, encoding='utf8')

    def get(self, field, key):
        return self.conf.get(field, key)
