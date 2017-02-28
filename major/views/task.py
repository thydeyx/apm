#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2015-10-30 10:45:03
# @Last Modified by:   anchen
# @Last Modified time: 2016-06-25 20:33:34

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.http import JsonResponse
import json
import urllib
from major.models import *
import time
import sys
import zmq
import datetime,time
import random
from major.comtool import sendZmqPush , getReal ,getReals
from django.utils import timezone
from major.tasks import add
from major.tasks import analysisZMQ_test

def taskinfo(request,taskid):
    taskid = int(taskid)
    task = Tasks.objects.get(id=taskid)
    nodeJobs = task.nodes.all()
    print "nodeJobs:", nodeJobs
    for nodeJob in nodeJobs:
        print "nodeJob:", nodeJob

    #log = Logs.objects.filter(task=taskid)
    #latest_log = log.latest('timestamp')

    context = {}

    context['taskid']=taskid
    context['task'] = task
    #context['log'] = latest_log
    context['nodeJobs'] = nodeJobs
    parameters = Parameters.objects.all()
    CPUs = Parameters.objects.filter(type="CPU")
    Memorys = Parameters.objects.filter(type="Memory")
    Networks = Parameters.objects.filter(type="Network")
    IOs = Parameters.objects.filter(type="I/O")
    NFSs = Parameters.objects.filter(type="NFS")
    context['parameters'] = parameters
    context['CPUs'] = CPUs
    context['Memorys'] = Memorys
    context['Networks'] = Networks
    context['IOs'] = IOs
    context['NFSs'] = NFSs
    context['CPU'] = 'CPU'
    context['Memory'] = 'Memory'
    context['Network'] = 'Network'
    context['IO'] = 'I/O'
    context['NFS'] = 'NFS'
    return render_to_response('task/taskinfo.html',  context)


def taskUnusual(request,taskid):
    taskid = int(taskid)
    task = Tasks.objects.get(id=taskid)
    nodeApp = task.nodes.all()
    context = {}
    try:
        nodes = [item.node for item in nodeApp]
        nodes = list(set(nodes))
    except Exception,e:
        print (e)
    for item in nodes:
        print (item.os)
    context['taskid']=taskid
    context['task'] = task
    context['nodes'] = nodes
    return render_to_response('report/taskUnusualReport.html',context)


def ioedit(request,taskid):
    taskid = int(taskid)
    task = Tasks.objects.get(id=taskid)
    nodeApp = task.nodes.all()
    context = {}
    try:
        nodes = [item.node for item in nodeApp]
        nodes = list(set(nodes))
    except Exception,e:
        print (e)
    for item in nodes:
        print (item.os)
    context['taskid']=taskid
    context['task'] = task
    context['nodes'] = nodes
    return render_to_response('ioedit.html',context)


def analysisZMQ(taskid):
    task = Tasks.objects.get(id=taskid)
    starttime = (task.start_date + ' ' + task.start_time).encode("UTF-8")
    endtime = (task.end_date + ' ' + task.end_time).encode("UTF-8")
    starttime = time.strptime(starttime,'%Y-%m-%d %H:%M:%S')
    endtime = time.strptime(endtime, "%Y-%m-%d %H:%M:%S")
    starttime = int(time.mktime(starttime))
    endtime = int(time.mktime(endtime))
    param = {}
    hostid = task.nodes.all()[0].environment.node.all()[0].name
    filtermode = 0
    if (cmp(task.data_type.encode("UTF-8"),"预处理数据")==0):
        filtermode = 1
    if cmp((task.type.name).encode("UTF-8"),'单作业基准测试')==0:
        ptype = 1
        param = {'start':str(starttime),'end':str(endtime),'taskid':taskid,'ptype':ptype,'hostid':hostid,'filtermode':filtermode}
    elif cmp((task.type.name).encode("UTF-8"),'多作业基准测试')==0:
        ptype = 2
        param = {'start':str(starttime),'end':str(endtime),'taskid':taskid,'ptype':ptype,'hostid':hostid,'filtermode':filtermode}
    else:
        ptype = 3
        param = {'start':str(starttime),'end':str(endtime),'taskid':taskid,'ptype':ptype,'filtermode':filtermode}
    sendZmqPush(param)

def updateStatus(request):
    taskid = request.POST['taskid']
    newStatus = request.POST['newStatus']
    print  taskid, ' ', newStatus
    task = Tasks.objects.get(id=taskid)
    if newStatus == 'collect_start':
        task.process = '数据采集中'
        task.start_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
        task.start_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        try:
            task.save()
        except Exception, e:
            print (e)
    elif newStatus == 'analysis_start':
        task.process = '特征分析中'
        task.end_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        task.end_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
        task.save()
        analysisZMQ(taskid)
    elif newStatus == 'task_cancel':
        task.process = '任务已取消'
        task.save()
    return HttpResponse("data updated")

def getcollecttimerresult(taskid,parameters):
    #sys.setdefaultencoding('utf8')
    task = Tasks.objects.get(id=taskid)
    hostname = task.nodes.all()[0].environment.node.all()[0].name
    endtime = int (time.time())-30
    starttime = endtime - 5
    contents = getReal(hostname,str(starttime)+"000",str(endtime)+"000")
    newcontents = []
    for parameter in parameters:
        para = parameter.encode("UTF-8")
        for content in contents:
            if cmp(content['key'],para)==0:
                newcontents.append(content)
                break
    return newcontents

def collectTimer(request):
    taskid = request.POST['taskid']
    parameters = request.POST['parameter']
    parameters = parameters.rsplit(',')
    param = {"content":getcollecttimerresult(taskid,parameters)}
    return HttpResponse(json.dumps(param))

def analysisTimer(request):
    taskid = request.POST['taskid']
    newStatus = request.POST['newStatus']
    task = Tasks.objects.get(id=taskid)

    time_now = timezone.localtime(timezone.now()) + datetime.timedelta(hours=8)
    time_last = time_now - datetime.timedelta(seconds=5)

    #test_begin = time_now - datetime.timedelta(hours=6)
    #test_end = test_begin + datetime.timedelta(hours=1)

    logs = Logs.objects.filter(task=taskid)
    logs_latest = logs.filter(timestamp__range=(time_last, time_now))

    if cmp(task.process.encode("UTF-8"),'任务已完成')==0:
        message = 'OK'
    else:
        message = 'NO'
    for log in logs_latest:
        message += '|' + log.level + ',' + log.info

    #task.process = '任务已完成'

    return HttpResponse(message)
