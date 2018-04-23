from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from django.core import serializers
from django.shortcuts import render
from models import authors
import urllib
import sys
import hashlib

@require_http_methods(["GET"])
def get_authors_by_name(request):
    response = {}
    try:
        authors_json = authors.objects.filter().order_by('id')
        tempList = json.loads(serializers.serialize("json", authors_json))
        tempList2 = []
        # 处理返回的数据
        for i in tempList:
            tempList2.append({
                'name': i['fields']['name'],
                'organization': i['fields']['organization'],
            })
        total = len(tempList2)
        data = {
            'list': tempList2,
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

