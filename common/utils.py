# -*- coding: utf-8 -*-
# @Time : 2019/11/25 10:45
# @Author : wangmengmeng
import os
from config.config import FILE_PATH


def get_file_content():
    files = os.listdir(FILE_PATH)
    length = len(files)
    index = 0

    while True:
        with open(os.path.join(FILE_PATH, files[index]), mode='r', encoding='utf-8', buffering=True) as f:
            file_content = f.read()
        yield file_content
        index += 1
        if index == length:
            exit(0)
