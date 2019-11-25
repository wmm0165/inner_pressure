# -*- coding: utf-8 -*-
# @Time : 2019/11/25 10:45
# @Author : wangmengmeng
import os

def get_file_content():
    # path = r'D:\ccc'
    # path = r'D:\data\2019-11-02\H0003\receive_path'
    path = '/mnt/sf_tools/py_inner_perssure/testdata/2019-11-03/H0003/receive_path'
    files = os.listdir(path)
    length = len(files)
    index = 0

    while True:
        with open(os.path.join(path, files[index]), mode='r', encoding='utf-8', buffering=True) as f:
            file_content = f.read()
        yield file_content
        index += 1
        if index == length:
            exit(0)
