from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from django.core import serializers
from .models import authors, paper_detail, paper_title, journal, organization
import urllib
import sys
import hashlib
import random
import pymysql
from django.db.models import Count

@require_http_methods(["GET"])
def get_authors_by_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        list = []
        tempList = authors.objects.raw('SELECT * FROM Search_authors WHERE name = %s', [name])
        tempList2 = json.loads(serializers.serialize("json", tempList))
        for i in tempList2:
            list.append({
                'name': i['fields']['name'],
                'organization': i['fields']['organization'],
                'uniid': i['fields']['uniid']
            })
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def get_personalinfo_by_uniid(request):
    if 'uniid' in request.GET:
        uniid = request.GET['uniid']
    response = {}
    try:
        list = []
        tempList = authors.objects.raw('SELECT * FROM Search_authors WHERE uniid = %s', [uniid])
        tempList2 = json.loads(serializers.serialize("json", tempList))
        for i in tempList2:
            list.append({
                'name': i['fields']['name'],
                'organization': i['fields']['organization'],
                'uniid': i['fields']['uniid'],
                'avatar_src': i['fields']['avatar_src'],
                'work_experience': i['fields']['work_experience'],
                'edu_experience': i['fields']['edu_experience'],
                'domain': i['fields']['domain'],
                'intro': i['fields']['intro']
            })
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def get_paper_title_by_uniid(request):
    if 'uniid' in request.GET:
        uniid = request.GET['uniid']
    response = {}
    try:
        list = []
        tempList = paper_title.objects.raw('SELECT * FROM Search_paper_title WHERE authors_uniid = %s', [uniid])
        tempList2 = json.loads(serializers.serialize("json", tempList))
        for i in tempList2:
            list.append({
                'title': i['fields']['title'],
                'authors': i['fields']['authors'],
                'publish_time': i['fields']['publish_time'],
                'journal': i['fields']['journal'],
            })
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def get_paper_detail_by_title(request):
    if 'title' in request.GET:
        title = request.GET['title']
    response = {}
    try:
        list = []
        tempList = paper_detail.objects.raw('SELECT * FROM Search_paper_detail WHERE title = %s', [title])
        tempList2 = json.loads(serializers.serialize("json", tempList))
        for i in tempList2:
            list.append({
                'title': i['fields']['title'],
                'authors': i['fields']['authors'],
                'abstract': i['fields']['abstract'],
                'src': i['fields']['src'],
                'key_words': i['fields']['key_words'],
            })
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def get_interpersonal_relationship_network_by_uniid(request):
    if 'uniid' in request.GET:
        uniid = request.GET['uniid']
    response = {}
    try:
        list = []
        links = []
        author_list = []
        author_list_with_name = []
        mainAuthorList = authors.objects.raw('SELECT * FROM Search_authors WHERE uniid = %s', [uniid])
        tempList = paper_title.objects.raw('SELECT * FROM Search_paper_title WHERE authors_uniid = %s', [uniid])
        mainAuthorList2 = json.loads(serializers.serialize("json", mainAuthorList))
        tempList2 = json.loads(serializers.serialize("json", tempList))
        authors_all = []
        for i in mainAuthorList2:
            mainAuthor = i['fields']['name']
        for i in tempList2:
            author = i['fields']['authors'].split('; ')
            # print('author:', author)
            authors_all += author
            k_counter = 0
            for k in author:
                k_counter = k_counter + 1
                # print('k:', author[k_counter-1])
                for j in range(k_counter, len(author)):
                    # print(j)
                    links.append({
                        'source': author[k_counter - 1],
                        'target': author[j]
                    })
        authors_set = set(authors_all)
        item_counter = 0

        for item in authors_set:
            item_counter = item_counter + 1
            # print(item_counter)
            # print(item)
            list.append({
                'name': item,
                'symbolSize': authors_all.count(item)*2,
                'value': authors_all.count(item),
                # "draggable": "true",
                'category': item
            })
            author_list.append(item)
            author_list_with_name.append({
                'name': item
            })
        total = len(list)
        data = {
            'list': list,
            'links': links,
            'author_list': author_list,
            'author_list_with_name': author_list_with_name,
            'mainAuthor': mainAuthor,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def get_journal_by_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        list = []
        tempList = journal.objects.raw('SELECT * FROM Search_journal WHERE name = %s', [name])
        tempList2 = json.loads(serializers.serialize("json", tempList))
        for i in tempList2:
            influence = i['fields']['influence'].split(';')
            list.append({
                'name': i['fields']['name'],
                'website': i['fields']['website'],
                'introduction': i['fields']['introduction'],
                'category': i['fields']['category'],
                'logo': i['fields']['logo'],
                'english_name': i['fields']['english_name'],
                'host_unit': i['fields']['host_unit'],
                'complex_influence': influence[0],
                'comprehensive_influence': influence[1],
                'honor': i['fields']['honor']
            })
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def get_paper_by_journal_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        list = []
        tempList = paper_title.objects.raw('SELECT * FROM Search_paper_title WHERE journal = %s', [name])
        tempList2 = json.loads(serializers.serialize("json", tempList))
        for i in tempList2:
            list.append({
                'title': i['fields']['title'],
                'authors': i['fields']['authors'],
                'publish_time': i['fields']['publish_time'],
            })
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def get_journal_publish_every_year_by_journal_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        list = []
        num = paper_title.objects.filter(journal = name).values_list('publish_time').annotate(Count('id')).order_by('publish_time')
        for i in num :
            # print(i[0], i[1])
            list.append({
                'sum': i[1],
                'publish_time': i[0],
            })
        listMaxYear = sorted(list, key=lambda x: (-x['sum']))
        max = listMaxYear[0]['sum']
        total = len(list)
        data = {
            'list': list,
            #获取发表最多一年的值，利于坐标的上限取值
            'max': max,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def get_journal_keyword_by_journal_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        list = []
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("localhost", "root", "1011", "sis", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        sql = 'SELECT DISTINCT d.title, d.key_words from search_paper_detail d JOIN ' \
              'search_paper_title t ON d.title = t.title WHERE t.journal = %s;'
        param = (name)
        cursor.execute(sql, param)
        sql_result = cursor.fetchall()
        keyword_all_arr = []
        for i in sql_result:
            keyword_all_arr = keyword_all_arr + i[1].split(';')
        for x in range(keyword_all_arr.count('')):
            keyword_all_arr.remove('')
        keyword_set_arr = set(keyword_all_arr)
        for item in keyword_set_arr:
            # 统计关键词重复次数
            # print(item, keyword_all_arr.count(item))
            list.append({
                'keyword': item,
                'sum': keyword_all_arr.count(item)
            })
        list = sorted(list, key=lambda x: (-x['sum']))
        if (len(list)> 10):
            list = list[:10]
        db.close();
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def get_journal_author_rank_by_journal_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        list = []
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("localhost", "root", "1011", "sis", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        sql = 'SELECT  d.name, COUNT(d.name) as rank from search_authors d JOIN search_paper_title t ' \
              'ON d.uniid = t.authors_uniid WHERE t.journal = %s GROUP BY d.name ORDER BY rank'
        param = (name)
        cursor.execute(sql, param)
        sql_result = cursor.fetchall()
        for i in sql_result:
            list.append({
                'author': i[0],
                'sum': i[1]
            })
        db.close()
        list = sorted(list, key=lambda x: (-x['sum']))
        if (len(list) > 10):
            list = list[:10]
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def get_organization_by_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        list = []
        tempList = organization.objects.raw('SELECT * FROM Search_organization WHERE name = %s', [name])
        tempList2 = json.loads(serializers.serialize("json", tempList))
        for i in tempList2:
            list.append({
                'name': i['fields']['name'],
                'english_name': i['fields']['english_name'],
                'logo': i['fields']['logo'],
                'website': i['fields']['website'],
                'introduction': i['fields']['introduction'],
                'location': i['fields']['location'],
            })
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def get_paper_by_organization_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        list = []
        authorList = authors.objects.raw('SELECT * FROM Search_authors WHERE organization = %s', [name])
        authorList2 = json.loads(serializers.serialize("json", authorList))
        for i in authorList2:
            authors_uniid = i['fields']['uniid']
            paperList = paper_title.objects.raw('SELECT * FROM Search_paper_title WHERE authors_uniid = %s', [authors_uniid])
            paperList2 = json.loads(serializers.serialize("json", paperList))
            for i in paperList2:
                list.append({
                    'title': i['fields']['title'],
                    'authors': i['fields']['authors'],
                    'publish_time': i['fields']['publish_time'],
                })
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def get_organization_publish_every_year_by_organization_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        list = []
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("localhost", "root", "1011", "sis", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        sql = 'SELECT COUNT(p.title) , p.publish_time FROM search_paper_title p JOIN search_authors a ' \
              'ON p.authors_uniid = a.uniid  where a.organization = %s GROUP BY p.publish_time ORDER BY p.publish_time'
        param = (name)
        cursor.execute(sql, param)
        sql_result = cursor.fetchall()
        for i in sql_result:
            list.append({
                'year': i[1],
                'sum': i[0]
            })
        db.close()
        listMaxYear = sorted(list, key=lambda x: (-x['sum']))
        max = listMaxYear[0]['sum']
        total = len(list)
        data = {
            'list': list,
            #获取发表最多一年的值，利于坐标的上限取值
            'max': max,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def get_organization_keyword_by_organization_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        list = []
        authorList = authors.objects.raw('SELECT * FROM Search_authors WHERE organization = %s', [name])
        authorList2 = json.loads(serializers.serialize("json", authorList))
        keyword_all_arr = []
        for i in authorList2:
            authors_uniid = i['fields']['uniid']
            paperList = paper_detail.objects.raw('SELECT * FROM Search_paper_detail WHERE authors_uniid = %s', [authors_uniid])
            paperList2 = json.loads(serializers.serialize("json", paperList))
            for i in paperList2:
                keyword_all_arr = keyword_all_arr + i['fields']['key_words'].split(';')
        for x in range(keyword_all_arr.count('')):
            keyword_all_arr.remove('')
        keyword_set_arr = set(keyword_all_arr)
        for item in keyword_set_arr:
            # 统计关键词重复次数
            list.append({
                'keyword': item,
                'sum': keyword_all_arr.count(item)
            })
        list = sorted(list, key=lambda x: (-x['sum']))
        if (len(list) > 10):
            list = list[:10]
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)



@require_http_methods(["GET"])
def get_organization_author_rank_by_organization_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        list = []
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("localhost", "root", "1011", "sis", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        sql = 'SELECT COUNT(p.title ), a.name FROM search_paper_title p JOIN search_authors a ' \
              'ON p.authors_uniid = a.uniid  where a.organization = %s GROUP BY a.`name`'
        param = (name)
        cursor.execute(sql, param)
        sql_result = cursor.fetchall()
        for i in sql_result:
            list.append({
                'author': i[1],
                'sum': i[0]
            })
        db.close()
        list = sorted(list, key=lambda x: (-x['sum']))
        if (len(list) > 10):
            list = list[:10]
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def get_organization_core_author_net_by_organization_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        list1 = []
        links = []
        echarts_author_list_with_name = []
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("localhost", "root", "1011", "sis", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        sql = 'SELECT authors FROM search_paper_title'
        # param = (name)
        cursor.execute(sql)
        sql_result = cursor.fetchall()
        core_author_organization = []
        for i in sql_result:
            core_author = i[0].split('; ')[0]
            sql2 = 'SELECT COUNT(*) from search_authors WHERE name = %s AND organization = %s'
            param2 = (core_author, name)
            cursor.execute(sql2, param2)
            sql_result2 = cursor.fetchall()
            for i in sql_result2:
                author_exist = i[0]
                if(author_exist == 1):
                    core_author_organization.append(core_author)
        core_author_organization_set = list(set(core_author_organization))
        for i in core_author_organization_set:
            sql3 = 'SELECT authors FROM search_paper_title t JOIN search_authors a ON ' \
                   'a.uniid = t.authors_uniid WHERE a.`name` = %s'
            param3 = (i)
            author_now = i
            cursor.execute(sql3, param3)
            sql_result3 = cursor.fetchall()
            paper_core_counter = 0
            for i in sql_result3:
                if (author_now == i[0].split('; ')[0]):
                    paper_core_counter = paper_core_counter + 1
                    authors_arr_without_coreauthor = i[0].split('; ')
                    del authors_arr_without_coreauthor[0]
                    authors_arr_without_coreauthor_copy = []
                    # 拷贝备份用
                    for j in authors_arr_without_coreauthor:
                        authors_arr_without_coreauthor_copy.append(j)
                    for item in authors_arr_without_coreauthor_copy:
                        # print(item)
                        sql4 = 'SELECT COUNT(*) from search_authors WHERE name = %s'
                        param4 = (item)
                        cursor.execute(sql4, param4)
                        sql_result4 = cursor.fetchall()
                        for k in sql_result4:
                            if (k[0] == 0):
                                authors_arr_without_coreauthor.remove(item)
                    if (len(authors_arr_without_coreauthor)>0):
                        for g in authors_arr_without_coreauthor:
                            core_net_counter = 0
                            param5 = (g)
                            cursor.execute(sql3, param5)
                            sql_result5 = cursor.fetchall()
                            for f in sql_result5:
                                authors_about_coauthor_arr = f[0].split('; ')
                                # 当前查询作者的合作作者中存在合作作者为核心作者的情况
                                if author_now in authors_about_coauthor_arr and authors_about_coauthor_arr[0] == g:
                                    core_net_counter = core_net_counter + 1
                            if(core_net_counter > 0):
                                links.append({
                                    'source': author_now,
                                    'target': g,
                                    'lineStyle': {
                                        'normal': {
                                            'curveness': 0.3,
                                            # 根据连线宽度表示合作次数
                                            'width': core_net_counter
                                        }
                                    }
                                })
                                # print(author_now, '--', g, core_net_counter)
            # print(author_now, paper_core_counter)
            list1.append({
                'name': author_now,
                'symbolSize': paper_core_counter,
                'value': paper_core_counter,
            })
        links1 = []
        # 去重
        links1.append(links[0])
        for dict in links:
            k = 0
            for item in links1:
                if dict['target'] == item['target'] and dict['source'] == item['source']:
                    break
                else:
                    k = k + 1
                if k == len(links1):
                    links1.append(dict)
        db.close()
        total = len(list1)
        data = {
            'list': list1,
            'links': links1,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def user_login(request):
    if 'username' in request.GET:
        username = request.GET['username']
    if 'password' in request.GET:
        password = request.GET['password']
    response = {}
    try:
        list = []
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("localhost", "root", "1011", "sis", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        sql = 'SELECT COUNT(id) FROM `search_users` WHERE username = %s AND `password` = %s'
        param = (username, password)
        cursor.execute(sql, param)
        sql_result = cursor.fetchall()
        for i in sql_result:
            if(i[0] == 1):
                list.append({
                    'status': 1
                })
            else:
                list.append({
                    'status': 0
                })
        db.close()
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def add_authors(request):
    if 'name' in request.GET:
        name = request.GET['name']
    if 'uniid' in request.GET:
        uniid = request.GET['uniid']
    if 'sex' in request.GET:
        sex = request.GET['sex']
    if 'organization' in request.GET:
        organization = request.GET['organization']
    if 'avatar_src' in request.GET:
        if request.GET['avatar_src'] == '':
            avatar_src = 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2766636815,3165673923&fm=27&gp=0.jpg'
        else:
            avatar_src = request.GET['avatar_src']
    if 'work_experience' in request.GET:
        if request.GET['work_experience'] == '':
            work_experience = '无'
        else:
            work_experience = request.GET['work_experience']
    if 'edu_experience' in request.GET:
        if request.GET['edu_experience'] == '':
            edu_experience = '无'
        else:
            edu_experience = request.GET['edu_experience']
    if 'domain' in request.GET:
        if request.GET['domain'] == '':
            domain = '无'
        else:
            domain = request.GET['domain']
    if 'uniid' in request.GET:
        uniid = request.GET['uniid']
    if 'intro' in request.GET:
        if request.GET['intro'] == '':
            intro = '无'
        else:
            intro = request.GET['intro']
    response = {}
    try:
        list = []
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("localhost", "root", "1011", "sis", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        sql0 = 'SELECT COUNT(uniid) FROM search_authors WHERE uniid = %s'
        param0 = (uniid)
        cursor.execute(sql0, param0)
        sql_result2 = cursor.fetchall()
        for i in sql_result2:
            if i[0] == 0:
                sql = 'INSERT INTO search_authors (uniid,name,sex,organization,avatar_src,work_experience,' \
                      'edu_experience,domain,intro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
                param = (uniid,name,sex,organization,avatar_src,work_experience,edu_experience,domain,intro)
                cursor.execute(sql, param)
                db.commit()
        sql2 = 'SELECT COUNT(uniid) FROM search_authors WHERE uniid = %s'
        param2 = (uniid)
        cursor.execute(sql2, param2)
        sql_result2 = cursor.fetchall()
        for i in sql_result2:
            if i[0] == 1:
                list.append({
                    'status': 1
                })
            else:
                list.append({
                    'status': 0
                })
        db.close()

        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)



@require_http_methods(["GET"])
def add_organization(request):
    if 'name' in request.GET:
        name = request.GET['name']
    if 'english_name' in request.GET:
        english_name = request.GET['english_name']
    if 'logo' in request.GET:
        if request.GET['logo'] == '':
            logo = 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2766636815,3165673923&fm=27&gp=0.jpg'
        else:
            logo = request.GET['logo']
    if 'website' in request.GET:
        if request.GET['website'] == '':
            website = '无官网'
        else:
            website = request.GET['website']
    if 'introduction' in request.GET:
        if request.GET['introduction'] == '':
            introduction = '无'
        else:
            introduction = request.GET['introduction']
    if 'location' in request.GET:
        if request.GET['location'] == '':
            location = '不详'
        else:
            location = request.GET['location']
    response = {}
    try:
        list = []
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("localhost", "root", "1011", "sis", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        sql0 = 'SELECT COUNT(name) FROM search_organization WHERE name = %s'
        param0 = (name)
        cursor.execute(sql0, param0)
        sql_result2 = cursor.fetchall()
        for i in sql_result2:
            print(i)
        sql = 'INSERT INTO search_organization (name,english_name,logo,location,introduction,website' \
              ') VALUES (%s, %s, %s, %s, %s, %s)'
        param = (name,english_name,logo,location,introduction,website)
        cursor.execute(sql, param)
        db.commit()
        sql2 = 'SELECT COUNT(uniid) FROM search_authors WHERE name = %s'
        param2 = (name)
        cursor.execute(sql2, param2)
        sql_result2 = cursor.fetchall()
        for i in sql_result2:
            print(i)
        db.close()
        list.append({
            'status': 1
        })
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def add_journal(request):
    if 'name' in request.GET:
        name = request.GET['name']
    if 'english_name' in request.GET:
        english_name = request.GET['english_name']
    if 'logo' in request.GET:
        if request.GET['logo'] == '':
            logo = 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1056617409,3564418675&fm=27&gp=0.jpg'
        else:
            logo = request.GET['logo']
    if 'website' in request.GET:
        if request.GET['website'] == '':
            website = '无官网'
        else:
            website = request.GET['website']
    if 'influence' in request.GET:
        if request.GET['influence'] == '':
            influence = '无'
        else:
            influence = request.GET['influence']
    if 'honor' in request.GET:
        if request.GET['honor'] == '':
            honor = '无'
        else:
            honor = request.GET['honor'].replace(',', ';')
    if 'introduction' in request.GET:
        if request.GET['introduction'] == '':
            introduction = '无'
        else:
            introduction = request.GET['introduction']
    if 'host_unit' in request.GET:
        if request.GET['host_unit'] == '':
            host_unit = '不详'
        else:
            host_unit = request.GET['host_unit']
    response = {}
    try:
        list = []
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("localhost", "root", "1011", "sis", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        sql0 = 'SELECT COUNT(name) FROM search_journal WHERE name = %s'
        param0 = (name)
        cursor.execute(sql0, param0)
        sql_result2 = cursor.fetchall()
        for i in sql_result2:
            print(i[0])
            if i[0] == 0:
                sql = 'INSERT INTO search_journal (name,english_name,logo,influence,honor,introduction,' \
                      'website,host_unit,category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
                param = (name,english_name,logo,influence,honor,introduction,website,host_unit,honor)
                cursor.execute(sql, param)
                db.commit()
        sql2 = 'SELECT COUNT(name) FROM search_journal WHERE name = %s'
        param2 = (name)
        cursor.execute(sql2, param2)
        sql_result2 = cursor.fetchall()
        for i in sql_result2:
            print(i[0])
            if(i[0] == 1):
                list.append({
                    'status': 1
                })
            else:
                list.append({
                    'status': 0
                })
        db.close()
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def get_authors_list(request):
    response = {}
    try:
        list = []
        tempList = authors.objects.raw('SELECT * FROM Search_authors')
        tempList2 = json.loads(serializers.serialize("json", tempList))
        for i in tempList2:
            list.append({
                'name': i['fields']['name'],
                'organization': i['fields']['organization'],
                'avatar_src': i['fields']['avatar_src'],
                'sex': i['fields']['sex'],
                'uniid': i['fields']['uniid'],
            })
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def delete_author_by_uniid(request):
    if 'uniid' in request.GET:
        uniid = request.GET['uniid']
    response = {}
    try:
        list = []
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("localhost", "root", "1011", "sis", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        sql = 'DELETE  FROM `search_authors` WHERE uniid = %s'
        param = (uniid)
        cursor.execute(sql, param)
        db.commit()
        sql2 = 'SELECT COUNT(uniid) FROM `search_authors` WHERE uniid = %s'
        param2 = (uniid)
        cursor.execute(sql2, param2)
        sql_result = cursor.fetchall()
        for i in sql_result:
            if(i[0] == 0):
                list.append({
                    'status': 1
                })
            else:
                list.append({
                    'status': 0
                })
        db.close()
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def delete_journal_by_name(request):
    if 'uniid' in request.GET:
        uniid = request.GET['uniid']
    response = {}
    try:
        list = []
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("localhost", "root", "1011", "sis", use_unicode=True, charset="utf8")
        cursor = db.cursor()
        sql = 'DELETE  FROM `search_authors` WHERE uniid = %s'
        param = (uniid)
        cursor.execute(sql, param)
        db.commit()
        sql2 = 'SELECT COUNT(uniid) FROM `search_authors` WHERE uniid = %s'
        param2 = (uniid)
        cursor.execute(sql2, param2)
        sql_result = cursor.fetchall()
        for i in sql_result:
            if(i[0] == 0):
                list.append({
                    'status': 1
                })
            else:
                list.append({
                    'status': 0
                })
        db.close()
        total = len(list)
        data = {
            'list': list,
            'total': total
        }
        response['data'] = data
        response['msg'] = 'success'
        response['success'] = True
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)