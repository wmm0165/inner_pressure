# -*- coding: utf-8 -*-
# @Time : 2019/11/27 16:35
# @Author : wangmengmeng
import pymysql

# 定义数据库连接类
class DB:
    # 定义基本属性
    host = ''
    port = 0
    user = ''
    password = ''
    db = ''

    # 定义构造方法
    def __init__(self,h,p,u,pw,d):
        self.host = h
        self.port = p
        self.user = u
        self.password = pw
        self.db = d

    def connection(self):
        # 建立数据库连接
        conn = pymysql.connect(
            host=self.host,
            port=int(self.port),
            user=self.user,
            password=self.password,
            db=self.db,
            charset='utf8'
        )
        # 获取游标
        cursor = conn.cursor()
        if not cursor:
            raise Exception('数据库连接失败！')

        sql = 'SELECT COUNT(*) FROM tb_product'
        cursor.execute(sql)
        print(cursor.fetchone()[0])

        # 关闭连接
        conn.close()
        cursor.close()

if __name__ == '__main__':
    c = DB('10.1.1.147', 3306, 'root', 'root', 'ipharmacare_knowledge01')
    c.connection()