from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from django.core import serializers
from .models import authors, paper_detail, paper_title
import urllib
import sys
import hashlib

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
        # print(uniid)
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
            authors_all += author
        authors_set = set(authors_all)
        for item in authors_set:
            list.append({
                'name': item,
                'symbolSize': authors_all.count(item)*5,
                'value': authors_all.count(item),
                'category': item
            })
            links.append({
                'source': mainAuthor,
                'target': item
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