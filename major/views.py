# -*- coding: utf-8 -*-
# !/usr/bin/python

# @author: YangYu
# @date: 15/10/13
# @description:

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.


def test(request):
    print request.path
    print request.get_host()
    print request.get_full_path()
    print request.is_secure()
    print request.META['HTTP_USER_AGENT']
    return HttpResponse('hello')


#如下 为测试项目  表示ajax 表单控制等
def ajax_list(request):
    a = range(100)

    print json.dumps(a)
    return HttpResponse(json.dumps(a),)


def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    a = json.dumps(name_dict)
    print a
    return HttpResponse(a, content_type="application/json")


def index(request):
    return render(request, 'test.html')


def add(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    return HttpResponse(str(a+b))
