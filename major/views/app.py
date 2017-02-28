#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2015-11-02 09:07:12
# @Last Modified by:   anchen
# @Last Modified time: 2015-11-05 15:12:20
# -*- coding: utf-8 -*-
# !/usr/bin/python

# @author: YangYu
# @date: 15/10/22
# @description:



from major.models import *
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import json
from major import tools


#新增节点
def addApp(request):
    #req = json.loads(request.body)
        # task1 = Tasks().objects.get(name=req['name'].encode('utf8'))
    app = Applications()
    app.name = request.POST['app-name']
    app.introduction = request.POST['app-desc']
    app.pre_app = request.POST['app-pre']
    app.post_app = request.POST['app-next']
    app.save()
    return HttpResponse("AppsAdded")


#编辑节点
def edit(request):
    app = Applications.objects.get(id=request.POST['app-id'])
    app.name = request.POST['app-name']
    app.introduction = request.POST['app-desc']
    app.pre_app = request.POST['app-pre']
    app.post_app = request.POST['app-next']
    app.save()
    return HttpResponse("AppDataUpdated")


#删除节点
def delete(request):
    app = Applications.objects.get(id=request.POST['id'])
    app.delete()
    return HttpResponse("AppDataDelete")