# -*- coding: utf-8 -*-
# @Time : 2019/7/17 16:25
# @Author : wangmengmeng
from common.add_user import AddUser
from common.delete_user import DeleteUser


def run_user():
    deleteuser = DeleteUser()
    deleteuser.delete_user()
    num = int(input("请输入需要新增的用户数(输入按回车键):"))
    adduser = AddUser()
    adduser.add_user(num)


if __name__ == '__main__':
    run_user()
