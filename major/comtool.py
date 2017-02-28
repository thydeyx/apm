#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.http import JsonResponse
import json
import re
import zmq
import sys
import time
import urllib
from major.models import *

dataip = "10.109.247.80"
dataport = "8000"
dataprex = 'http://' + dataip + ':' + dataport

serverip = "10.109.247.80"
serverportpush = "7502"
serverportpushreq = "7501"
serveraddresspush = "tcp://" + serverip + ":" + serverportpush
serveraddressreq = "tcp://" + serverip + ":" + serverportpushreq

def sendZmqPush(message):
	zmqcontext = zmq.Context()
	socket = zmqcontext.socket(zmq.PUSH)
	socket.connect(serveraddresspush)
	socket.send(json.dumps(message))

def sendZmqReq(message):
	context = zmq.Context()
	socket = context.socket(zmq.REQ)
	socket.connect(serveraddressreq)
	socket.send(json.dumps(message))
	data = socket.recv()
	data = data[:-1]
	data = json.loads(data)
	return data

def getResult(mystr):
    data = urllib.urlopen(mystr.encode("UTF-8"))
    data = json.load(data)
    data = data['json']
    data = json.loads(data)
    data = data['hits']['hits']
    result = []
    for d in data:
        result.append(d['_source'])
    result.sort(key=lambda item : item['timestamp'])
    return result

def makesurefive(ve,data):
    n = len(ve)
    if (n < 1 ):
        ve.append(data)
        ve.append(data)
        ve.append(data)
        ve.append(data)
        ve.append(data)
    else :
        lastone = ve[n-1]
        while(n<5):
            ve.append(lastone)
            n = n+1
    return ve

def getMemory(mystr):
    content = []
    result = getResult(mystr)
    valueofmem = []
    valueofswap = []
    valueofmemoryradio = []
    valueofswapradio = []
    valueofmemoryuse = []
    valueofswapuse = []
    valueofmemoryfree = []
    valueofswapfree = []
    for mem in result:
        valueofmem.append(mem['MemTotal'])
        #valueofswap.append(mem['SwapTotal'])
        #valueofmemoryuse.append(mem['MemUsed'])
        #valueofswapuse.append(mem['SwapUsed'])
        #valueofmemoryfree.append(mem['MemFree'])
        #valueofswapfree.append(mem['SwapFree'])
        valueofmemoryradio.append(mem['MemRatio'])
        #valueofswapradio.append(mem['SwapRatio'])
    #valueofmem = makesurefive(valueofmem)
    #valueofswap = makesurefive(valueofswap)
    valueofmemoryradio = makesurefive(valueofmemoryradio,0)
    #valueofswapradio = makesurefive(valueofswapradio)
    #valueofmemoryuse = makesurefive(valueofmemoryuse)
    #valueofswapuse = makesurefive(valueofswapuse)
    #valueofmemoryfree = makesurefive(valueofmemoryfree)
    #valueofswapfree = makesurefive(valueofswapfree)
    #content.append({'key': '总内存大小', 'value': valueofmem})
    #content.append({'key': '总交换区大小', 'value': valueofswap})
    content.append({'key': '内存使用率', 'value': valueofmemoryradio})
    #content.append({'key': '交换区使用率', 'value': valueofswapradio})
    #content.append({'key': '活跃内存', 'value': valueofmemoryuse})
    #content.append({'key': '空闲内存', 'value': valueofmemoryfree})
    #content.append({'key': '活跃交换区', 'value': valueofswapuse})
    #content.append({'key': '空闲交换区', 'value': valueofswapfree})
    return content

def getNet(mystr):
    content = []
    result = getResult(mystr)
    valueofsend = []
    valueofreceive = []
    for net in result:
        valueofsend.append(net['if']['net_all_send'])
        valueofreceive.append(net['if']['net_all_recv'])
    valueofsend = makesurefive(valueofsend,0)
    valueofreceive = makesurefive(valueofreceive,0)
    content.append({'key': '网络发送速度', 'value': valueofsend})
    content.append({'key': '网络接收速度', 'value': valueofreceive})
    return content

def getDiskIO(mystr):
    content = []
    result = getResult(mystr)
    valueofdiskread = []
    valueofdiskwrite = []
    valueofdisktps = []
    valueofdiskawait = []
    valueofdisksvctm = []
    valueofdiskavgqu = []
    for disk in result:
        valueofdiskread.append(disk['dskio']['disk_all_read'])
        valueofdiskwrite.append(disk['dskio']['disk_all_write'])
        #valueofdisktps.append(disk['disk_all_tps'])
        #valueofdiskawait.append(disk['disk_all_await'])
        #valueofdisksvctm.append(disk['disk_all_svctm'])
        #valueofdiskavgqu.append(disk['disk_all_avgqu'])
    valueofdiskread = makesurefive(valueofdiskread,0)
    valueofdiskwrite = makesurefive(valueofdiskwrite,0)
    #valueofdisktps = makesurefive(valueofdisktps)
    #valueofdiskawait = makesurefive(valueofdiskawait)
    #valueofdisksvctm = makesurefive(valueofdisksvctm)
    #valueofdiskavgqu = makesurefive(valueofdiskavgqu)
    content.append({'key': '磁盘读速率', 'value': valueofdiskread})
    content.append({'key': '磁盘写速率', 'value': valueofdiskwrite})
    #content.append({'key': '每秒钟磁盘IO次数', 'value': valueofdisktps})
    #content.append({'key': 'IO请求平均等待时间', 'value': valueofdiskawait})
    #content.append({'key': 'IO请求平均服务时间', 'value': valueofdisksvctm})
    #content.append({'key': 'IO请求平均队列长度', 'value': valueofdiskavgqu})
    return content

def getCpu(mystr):
    content = []
    result = getResult(mystr)
    valueofcpuuser = []
    valueofsys = []
    valueofidle = []
    for cpu in result:
        valueofcpuuser.append(cpu['cpu']['user'])
        valueofsys.append(cpu['cpu']['sys'])
        valueofidle.append(cpu['cpu']['idle'])
    valueofcpuuser = makesurefive(valueofcpuuser,0)
    valueofsys = makesurefive(valueofsys,0)
    valueofidle = makesurefive(valueofidle,0)
    content.append({'key': '用户CPU利用率', 'value': valueofcpuuser})
    content.append({'key': '系统CPU利用率', 'value': valueofsys})
    content.append({'key': 'CPU空闲率', 'value': valueofidle})
    return content

def getNfs(mystr):
    content = []
    result = getResult(mystr)
    nfs_all_in = []
    nfs_all_out = []
    nfs_pkg_out = []
    nfs_pkg_in = []
    for nfs in result:
        nfs_all_in.append(nfs['nfs_all_in'])
        nfs_all_out.append(nfs['nfs_all_out'])
        nfs_pkg_out.append(nfs['nfs_pkg_out'])
        nfs_pkg_in.append(nfs['nfs_pkg_in'])
    nfs_all_in = makesurefive(nfs_all_in,0)
    nfs_all_out = makesurefive(nfs_all_out,0)
    nfs_pkg_out = makesurefive(nfs_pkg_out,0)
    nfs_pkg_in = makesurefive(nfs_pkg_in,0)
    content.append({'key': '网络文件系统接收量', 'value': nfs_all_in})
    content.append({'key': '网络文件系统发送量', 'value': nfs_all_out})
    content.append({'key': '网络文件系统发送包数量', 'value': nfs_pkg_out})
    content.append({'key': '网络文件系统接收包数量', 'value': nfs_pkg_in})
    return content

def getInfinibandtest(mystr):
    content = []
    infiniband_all_xmt = []
    infiniband_all_rcv = []
    for nfs in range(5):
        infiniband_all_xmt.append(0.00)
        infiniband_all_rcv.append(0.00)
    content.append({'key': '网卡发送速度', 'value': infiniband_all_xmt})
    content.append({'key': '网卡接收速度', 'value': infiniband_all_rcv})
    return content


def getInfiniband(mystr):
    content = []
    result = getResult(mystr)
    infiniband_all_xmt = []
    infiniband_all_rcv = []
    for infiniband in result:
        infiniband_all_xmt.append(infiniband['infiniband_all_xmt'])
        infiniband_all_rcv.append(infiniband['infiniband_all_rcv'])
    infiniband_all_xmt = makesurefive(infiniband_all_xmt,0)
    infiniband_all_rcv = makesurefive(infiniband_all_rcv,0)
    content.append({'key': '网卡发送速度', 'value': infiniband_all_xmt})
    content.append({'key': '网卡接收速度', 'value': infiniband_all_rcv})
    return content

def getip(str,hostname,starttime,endtime):
    result = dataprex + '/ELKPlatform/'
    result = result + 'loadServerDataByType-INTERFACE'
    result = result + '?hostname=' + hostname + '&type=' + str + '&starttime='+starttime+'&endtime='+endtime
    return result

def getReal(hostname,starttime,endtime):
    content = []
    starttime = str(starttime)
    endtime = str(endtime)
    try:
        content.extend(getMemory(dataprex + '/ELKPlatform/loadMem?hostname=' + hostname + '&type=mem&starttime='+starttime+'&endtime='+endtime))
    except Exception, e:
        print (e)
    try:
        content.extend(getNet(dataprex + '/ELKPlatform/loadNet?hostname=' + hostname + '&type=net&starttime='+starttime+'&endtime='+endtime))
    except Exception, e:
        print (e)
    try:
        content.extend(getDiskIO(dataprex + '/ELKPlatform/loadIo?hostname=' + hostname + '&type=io&starttime='+starttime+'&endtime='+endtime))
    except Exception, e:
        print (e)
    try:
        content.extend(getCpu(dataprex + '/ELKPlatform/loadCpu?hostname=' + hostname + '&type=cpu&starttime='+starttime+'&endtime='+endtime))
    except Exception, e:
        print (e)
    try:
        content.extend(getNfs(dataprex + '/ELKPlatform/loadDfs?hostname=' + hostname + '&type=dfs&starttime='+starttime+'&endtime='+endtime))
    except Exception, e:
        print (e)
    try:
        #content.extend(getNfs(dataprex + '/ELKPlatform/loadInfiniband?hostname=' + hostname + '&type=infiniband&starttime='+starttime+'&endtime='+endtime))
        content.extend(getInfinibandtest(dataprex + '/ELKPlatform/loadInfiniband?hostname=' + hostname + '&type=mem&starttime='+starttime+'&endtime='+endtime))
    except Exception, e:
        print (e)
    return content

def getReals(hostname,starttime,endtime):
    content = []
    starttime = str(starttime)
    endtime = str(endtime)
    try:
        content.extend(getMemory(getip('meminfo',hostname,starttime,endtime)))
    except Exception, e:
        print (e)
    try:
        content.extend(getNet(getip('net',hostname,starttime,endtime)))
    except Exception, e:
        print (e)
    try:
        content.extend(getDiskIO(getip('dskio',hostname,starttime,endtime)))
    except Exception, e:
        print (e)
    try:
        content.extend(getCpu(getip('cpu',hostname,starttime,endtime)))
    except Exception, e:
        print (e)
    return content

def getCpuNode(hostname,starttime,endtime):
	context = []
	try:
		result = getResult(dataprex + '/ELKPlatform/loadCpu')
		#result = getResult((getip('cpu',hostname,starttime,endtime)))
		for cpu in result:
			context.append(100*cpu['cpu']['user'])
	except Exception, e:
		print (e)
	context = makesurefive(context,-1)
	return context

def getIoNode(hostname,starttime,endtime):
    context = []
    try:
        result = getResult(dataprex + '/ELKPlatform/loadIo')
        #result = getResult((getip('dskio',hostname,starttime,endtime)))
        for disk in result:
            diskinfo = (disk['dskio']['disk_all_read']+disk['dskio']['disk_all_write'])/10000
            if diskinfo>100:
                diskinfo = 100
            context.append(diskinfo)
    except Exception, e:
        print (e)
    context = makesurefive(context,-1)
    return context

def getMemNode(hostname,starttime,endtime):
	context = []
	try:
		result = getResult(dataprex + '/ELKPlatform/loadMem')
		#result = getResult((getip('meminfo',hostname,starttime,endtime)))
		for mem in result:
			context.append(mem['MemRatio'])
	except Exception, e:
		print (e)
	context = makesurefive(context,-1)
	return context

def getNetNode(hostname,starttime,endtime):
    context = []
    try:
        result = getResult(dataprex + '/ELKPlatform/loadNet')
        #result = getResult((getip('net',hostname,starttime,endtime)))
        for net in result:
            netinfo = (net['if']['net_all_send'] + net['if']['net_all_recv'])/10000
            if netinfo > 100:
                netinfo = 100
            context.append(netinfo)
    except Exception, e:
        print (e)
    context = makesurefive(context,-1)
    return context

def judgeContext(context):
    if context[0]==-1:
        return False
    return True

def getNodeState(hostname,starttime,endtime):
    cpu = getCpuNode(hostname,starttime,endtime)
    mem =getMemNode(hostname,starttime,endtime)
    network = getNetNode(hostname,starttime,endtime)
    io = getIoNode(hostname,starttime,endtime)
    if(judgeContext(cpu)==False):
        return {"nodeName":hostname,"cpu":cpu,"memory":mem,"network":network,"io":io,"flag":0}
    if(judgeContext(mem)==False):
        return {"nodeName":hostname,"cpu":cpu,"memory":mem,"network":network,"io":io,"flag":0}
    if(judgeContext(network)==False):
        return {"nodeName":hostname,"cpu":cpu,"memory":mem,"network":network,"io":io,"flag":0}
    if(judgeContext(io)==False):
        return {"nodeName":hostname,"cpu":cpu,"memory":mem,"network":network,"io":io,"flag":0}
    context = {"nodeName":hostname,"cpu":cpu,"memory":mem,"network":network,"io":io,"flag":1}
    return context


def getServer(nodename):
    node = Node.objects.get(name=nodename)
    #data = urllib.urlopen(dataprex + '/ELKPlatform/loadServer-INTERFACE?hostname=' + nodename)
    data = urllib.urlopen('http://10.109.247.80:9099/hardinfo/FY4AHACVS1.txt')
    data = json.load(data)
    data = data['json']
    data = json.loads(data)
    data = data['hits']['hits'][0]['_source']
    node.ip = data['ip']
    node.cpu_number = int(re.search('CPU (\d+)',data['CPU']).group(1))

    try:
        node.cpu_frequency = float(re.search(' (\d+\.*\d+)MHz',data['CPU']).group(1))
        node.cpu_frequency = node.cpu_frequency/1000
    except Exception, e:
        print e

    try:
        node.cpu_frequency = float(re.search(' (\d+\.*\d+)GHz',data['CPU']).group(1))
    except Exception, e:
        print e

    try:
        node.memory = float(re.search('(\d+\.*\d+)MB',data['MEM']).group(1))
        node.memory = node.memory/1000
    except Exception, e:
        print e

    try:
        node.memory = float(re.search('(\d+\.*\d+)GB',data['MEM']).group(1))
    except Exception, e:
        print e

    try:
        node.memory_Speed = float(re.search('Speed: (\d+\.*\d+)MHz',data['MEM']).group(1))
    except Exception, e:
        print e

    try:
        node.memory_Speed = float(re.search('Speed: (\d+\.*\d+)GHz',data['MEM']).group(1))
        node.memory_Speed = node.memory_Speed*1000
    except Exception, e:
        print e
    #node.memory_Speed = float(re.search('Speed: (\d+.*\d+) MHz',data['MEM']).group(1))
    node.save()
    for d in node.disk.all():
        node.disk.remove(d)
        d.delete()
    disks_type = list(re.findall('Disk (((\w)|(\W))+?):',data['Disk']))
    disks_size = list(re.findall('(\d+\.*\d+)[MG]B',data['Disk']))
    disk_num = len(disks_type)
    for i in range(0, disk_num):
        d = Disk()
        d.name = disks_type[i][0]
        d.size = disks_size[i]
        d.save()
        node.disk.add(d)
    for g in node.gpu.all():
        node.gpu.remove(g)
        g.delete()
    try:
        gpus_name = list(re.findall('\d+x (((\w)|(\W))+?)}',data['GPU']))
        gpus_number = list(re.findall('GPU (\d+)x ',data['GPU']))
        gpus_num = len(gpus_name)
        for i in range(0, gpus_num):
            g = Gpu()
            g.name = gpus_name[i][0]
            g.number = gpus_number[i]
            g.save()
            node.gpu.add(g)
    except Exception, e:
        print e
    try:
        for n in node.net.all():
            node.net.remove(n)
            n.delete()
        net_name = list(re.findall('\d+x (((\w)|(\W))+?)}',data['NET']))
        net_number = list(re.findall('NET (\d+)x ',data['NET']))
        net_num = len(net_name)
        for i in range(0, net_num):
            n = Net()
            n.name = net_name[i][0]
            n.number = net_number[i][0]
            n.save()
            node.net.add(n)
    except Exception, e:
        print e
    node.os = data['OS']
    node.save()

def finishJob(taskid):
    taskid = int(taskid)
    task = Tasks.objects.get(id=taskid)
    state = task.process.encode("UTF-8")
    if (cmp(state,'特征分析中')==0):
        task.process='任务已完成'
        task.save()

def finishJobWrong(taskid):
    taskid = int(taskid)
    task = Tasks.objects.get(id=taskid)
    task.process='任务错误'
    task.save()
