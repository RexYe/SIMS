from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from django.core import serializers
from .models import authors, paper_detail, paper_title, journal
import urllib
import sys
import hashlib
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
            print(i[0], i[1])
            list.append({
                'sum': i[1],
                'publish_time': i[0],
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
        # print(keyword_all_arr)
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
        sql = 'SELECT DISTINCT d.title, d.key_words from search_paper_detail d JOIN ' \
              'search_paper_title t ON d.title = t.title WHERE t.journal = %s;'
        param = (name)
        cursor.execute(sql, param)
        sql_result = cursor.fetchall()
        keyword_all_arr = []
        for i in sql_result:
            keyword_all_arr = keyword_all_arr + i[1].split(';')
        # print(keyword_all_arr)
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