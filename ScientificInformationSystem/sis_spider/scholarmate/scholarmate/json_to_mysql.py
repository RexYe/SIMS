# -*- coding: UTF-8 -*-
import pymysql
import json

# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect("localhost", "root", "1011", "sis",use_unicode=True, charset="utf8")

with open('wangwanliang0.json', encoding='utf-8') as f:
    data1 = json.load(f)
    for data in data1:
        # 取出year与journal脏数据
        if (len(data['year'])< 30 and len(data['journal'])<50):
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            sql = "INSERT INTO search_paper_title (title,authors,publish_time,journal,authors_uniid) VALUES (%s,%s,%s,%s,%s)"
            param = (data['title'], data['author'], data['year'], data['journal'], data['authors_uniid'])
            cursor.execute(sql, param)
db.commit()
# 关闭数据库连接
db.close()