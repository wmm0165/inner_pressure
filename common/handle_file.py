# -*- coding: utf-8 -*-
# @Time : 2019/9/24 16:10
# @Author : wangmengmeng
import os, sys, zipfile
from common.config import ZIP_PATH


class HandleFile:
    def __init__(self):
        pass

    def unzip_file(self, fullPath):
        f = zipfile.ZipFile(fullPath)
        f.extractall()
        filenames = f.namelist()
        print(filenames)

    def get_file_content(self,file):
        """根据文件名获取文件内容"""


if __name__ == '__main__':
    a = HandleFile()
    a.unzip_file(ZIP_PATH)
