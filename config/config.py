# -*- coding: utf-8 -*-
# @Time : 2019/9/25 16:41
# @Author : wangmengmeng
import os

PROJ_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZIP_PATH=os.path.join(os.path.dirname(os.path.abspath(__file__)),'test_2019.zip')

if __name__ == '__main__':
    print(ZIP_PATH)
    print(os.getcwd())