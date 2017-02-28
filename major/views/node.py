
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
import re
import zmq
import sys
import time
import urllib
from major import tools
from major.comtool import getServer

def nodeJSON(request):

    a=Node.objects.all()
    return HttpResponse(json.dumps(a,cls=tools.QuerySetEncoder), content_type="application/json")

# def test(request):
#     return render_to_response('xxxx.html')


def getServers(request):
    getServer(request.POST['name'])
    return HttpResponse("ok")

#新增节点
def addNode(request):
	node = Node()
	node.name = request.POST['name']
	node.introduction = request.POST['node-desc']
	node.ip = request.POST['node-ip']
	node.save()
	getServer(node.name)
	return HttpResponse("NodeAdded")

#编辑节点
def edit(request):
    node = Node.objects.get(id=request.POST['node-id'])
    node.name = request.POST['node-name']
    node.introduction = request.POST['node-desc']
    node.ip = request.POST['node-ip']
    node.cpu_number = int(request.POST['node-cpucount'])
    node.cpu_frequency = request.POST['node-cpuFrequency']
    node.memory = request.POST['node-memory']
    node.memory_Speed = request.POST['node-memorySpeed']
    node.disk = request.POST['node-disk']
    node.gpu = request.POST['node-gpu']
    node.net = request.POST['node-net']
    node.os = request.POST['node-os'].encode('utf8')
    node.save()
    return HttpResponse("NodeDataUpdated")


#删除节点
def delete(request):
    node = Node.objects.get(id=request.POST['id'])
    node.delete()
    return HttpResponse("NodeDataDelete")


