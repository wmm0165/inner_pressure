# -*- coding: utf-8 -*-
# @Time : 2019/9/28 23:55
# @Author : wangmengmeng
class FileUtil:
    def __init__(self):
        pass

    def get_file_content(self, file):
        with open(file, mode='r', encoding='utf-8', buffering=True) as f:
            file_content = f.read()
        return file_content
    