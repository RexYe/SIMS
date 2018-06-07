# -*- coding: UTF-8 -*-
import pymysql
import json

# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect("localhost", "root", "1011", "sis",use_unicode=True, charset="utf8")

with open('results.json', encoding='utf-8') as f:
    data1 = json.load(f)
    for data in data1:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        if('year' in data.keys()):
            # 去除英文版脏数据
            if(data['author'].find(u"汤颖") != -1):
                if(data['title'] is not None):
                    sql = "INSERT INTO search_paper_title (title,authors,publish_time,journal,authors_uniid) VALUES (%s,%s,%s,%s,%s)"
                    param = (data['title'], data['author'].replace('*', ''), data['year'], data['journal'], data['authors_uniid'])
                    cursor.execute(sql, param)

        else:
            if (data['author2'].find(u"汤颖") != -1):
                if (data['title2'] is not None):
                    sql2 = "INSERT INTO search_paper_detail (title,authors,key_words,abstract,src,authors_uniid) VALUES (%s,%s,%s,%s,%s,%s)"
                    param2 = (
                    data['title2'], data['author2'].replace('*', ''), data['key_words'], data['abstract'], data['src'], data['authors_uniid2'])
                    cursor.execute(sql2, param2)
db.commit()
# 关闭数据库连接
db.close()