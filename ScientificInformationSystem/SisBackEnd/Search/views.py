from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from django.core import serializers
from .models import authors
import urllib
import sys
import hashlib

@require_http_methods(["GET"])
def get_authors_by_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
    response = {}
    try:
        # name = '王万良'
        list = []
        tempList = authors.objects.raw('SELECT * FROM Search_authors WHERE name = %s', [name])
        tempList2 = json.loads(serializers.serialize("json", tempList))
        for i in tempList2:
            list.append({
                'name': i['fields']['name'],
                'organization': i['fields']['organization']
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

