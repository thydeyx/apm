#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
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
from django.utils import timezone
from celery import task
serverip = "10.109.247.80"
serverport = "7502"
serveraddress = "tcp://" + serverip + ":" + serverport

dataip = "10.109.247.80"
dataport = "8000"
dataprex = 'http://' + dataip + ':' + dataport

@task()
def add(x,y):
	print '123'
	return x+y

@task()
def analysisZMQ_test(taskid):
    time.sleep(5)
    print '222222222222222222222222222222222'
    task = Tasks.objects.get(id=taskid)
    starttime = (task.start_date + ' ' + task.start_time).encode("UTF-8")
    endtime = (task.end_date + ' ' + task.end_time).encode("UTF-8")
    starttime = time.strptime(starttime,'%Y-%m-%d %H:%M:%S')
    endtime = time.strptime(endtime, "%Y-%m-%d %H:%M:%S")
    starttime = int(time.mktime(starttime)) - 28800
    endtime = int(time.mktime(endtime)) - 28800
    param = {}
    hostid = 'oa-kyfz-th-c5-1'
    if cmp((task.type.name).encode("UTF-8"),'单作业基准测试')==0:
        ptype = 1
        param = {'start':str(starttime),'end':str(endtime),'taskid':taskid,'ptype':ptype,'hostid':hostid}
    elif cmp((task.type.name).encode("UTF-8"),'多作业基准测试')==0:
        ptype = 2
        param = {'start':str(starttime),'end':str(endtime),'taskid':taskid,'ptype':ptype,'hostid':hostid}
    else:
        ptype = 3
        param = {'start':str(starttime),'end':str(endtime),'taskid':taskid,'ptype':ptype}
    print json.dumps(param)
    zmqcontext = zmq.Context()
    socket = zmqcontext.socket(zmq.PUSH)
    socket.connect(serveraddress)
    print "sending........................."
    socket.send(json.dumps(param))
