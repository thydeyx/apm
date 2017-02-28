# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.http import JsonResponse
import json
from major.models import *
import time
import datetime
import zmq
from major.comtool import sendZmqReq

def get_cpuMax(ParaScore):
    maxValue = max(ParaScore.cpu_all_cpi, ParaScore.cpu_all_idle, ParaScore.cpu_all_sywa)
    return maxValue

def get_networkMax(ParaScore):
    maxValue = max(ParaScore.net_all_recv, ParaScore.net_all_send)
    return maxValue

def get_memoryMax(ParaScore):
    maxValue = max(ParaScore.mem_all_mem_ratio, ParaScore.mem_all_swap_ratio)
    return maxValue

def get_diskMax(ParaScore):
    maxValue = max(ParaScore.disk_all_read, ParaScore.disk_all_write)
    return maxValue

def get_nfsMax(ParaScore):
    maxValue = max(ParaScore.nfs_all_in, ParaScore.nfs_all_out)
    return maxValue

def get_percentage(phaseType,para):
    total = phaseType.nullType + phaseType.cpuType + phaseType.networkType + phaseType.diskType + phaseType.memoryType
    per = round(para*100/float(total),2)
    return per

def pfmtstReport(request,taskid):
    taskid = int(taskid)
    task = Tasks.objects.get(id=taskid)
    environmentJob = task.nodes.all()
    jobInfos = task.JobInfo.all()
    programSugession = task.Suggestion.filter(type=1)
    hardwareSugession = task.Suggestion.filter(type=2)
    #speedTrend = task.SpeedTrend.all()

    context = {}
    benchmark = {}
    mainFeature = {}
    paraScore_list = []
    class jobObject:
        def __init__(self, name, cpu, network, memory, disk, nfs):
            self.name = name
            self.cpu = cpu
            self.network = network
            self.memory = memory
            self.disk = disk
            self.nfs = nfs

    system_consume_name = {}
    system_consume_max = {}
    system_consume_max["cpu_all_cpi"] = 0
    system_consume_max["cpu_all_idle"] = 0
    system_consume_max["cpu_all_sywa"] = 0
    system_consume_max["mem_all_mem_ratio"] = 0
    system_consume_max["mem_all_swap_ratio"] = 0
    system_consume_max["disk_all_write"] = 0
    system_consume_max["disk_all_read"] = 0
    system_consume_max["net_all_recv"] = 0
    system_consume_max["net_all_send"] = 0
    system_consume_max["nfs_all_in"] = 0
    system_consume_max["nfs_all_out"] = 0
    job_consume_list = []

    system_consume_acc_name = {}
    system_consume_acc_max = {}
    system_consume_acc_max["cpu_all_cpi"] = 0
    system_consume_acc_max["cpu_all_idle"] = 0
    system_consume_acc_max["cpu_all_sywa"] = 0
    system_consume_acc_max["mem_all_mem_ratio"] = 0
    system_consume_acc_max["mem_all_swap_ratio"] = 0
    system_consume_acc_max["disk_all_write"] = 0
    system_consume_acc_max["disk_all_read"] = 0
    system_consume_acc_max["net_all_recv"] = 0
    system_consume_acc_max["net_all_send"] = 0
    system_consume_acc_max["nfs_all_in"] = 0
    system_consume_acc_max["nfs_all_out"] = 0
    job_consume_list_acc = []

    jobinfos = task.JobInfo.all()

    for jobinfo in jobinfos:
        try:
            if(jobinfo.benchmark):
                parameterscore = jobinfo.benchmark.benchmark_sorted_consume_score

                job = jobObject(jobinfo.job_name, get_cpuMax(parameterscore), get_networkMax(parameterscore),
                            get_memoryMax(parameterscore), get_diskMax(parameterscore), get_nfsMax(parameterscore))
                job_consume_list.append(job)

                if (parameterscore.cpu_all_cpi > system_consume_max["cpu_all_cpi"]):
                    system_consume_name["cpu_all_cpi"] = jobinfo.job_name
                    system_consume_max["cpu_all_cpi"] = parameterscore.cpu_all_cpi
                if (parameterscore.cpu_all_idle > system_consume_max["cpu_all_idle"]):
                    system_consume_name["cpu_all_idle"] = jobinfo.job_name
                    system_consume_max["cpu_all_idle"] = parameterscore.cpu_all_idle
                if (parameterscore.cpu_all_sywa > system_consume_max["cpu_all_sywa"]):
                    system_consume_name["cpu_all_sywa"] = jobinfo.job_name
                    system_consume_max["cpu_all_sywa"] = parameterscore.cpu_all_sywa
                if (parameterscore.mem_all_mem_ratio > system_consume_max["mem_all_mem_ratio"]):
                    system_consume_name["mem_all_mem_ratio"] = jobinfo.job_name
                    system_consume_max["mem_all_mem_ratio"] = parameterscore.mem_all_mem_ratio
                if (parameterscore.mem_all_swap_ratio > system_consume_max["mem_all_swap_ratio"]):
                    system_consume_name["mem_all_swap_ratio"] = jobinfo.job_name
                    system_consume_max["mem_all_swap_ratio"] = parameterscore.mem_all_swap_ratio
                if (parameterscore.disk_all_write > system_consume_max["disk_all_write"]):
                    system_consume_name["disk_all_write"] = jobinfo.job_name
                    system_consume_max["disk_all_write"] = parameterscore.disk_all_write
                if (parameterscore.disk_all_read > system_consume_max["disk_all_read"]):
                    system_consume_name["disk_all_read"] = jobinfo.job_name
                    system_consume_max["disk_all_read"] = parameterscore.disk_all_read
                if (parameterscore.net_all_recv > system_consume_max["net_all_recv"]):
                    system_consume_name["net_all_recv"] = jobinfo.job_name
                    system_consume_max["net_all_recv"] = parameterscore.net_all_recv
                if (parameterscore.net_all_send > system_consume_max["net_all_send"]):
                    system_consume_name["net_all_send"] = jobinfo.job_name
                    system_consume_max["net_all_send"] = parameterscore.net_all_send
                if (parameterscore.nfs_all_in > system_consume_max["nfs_all_in"]):
                    system_consume_name["nfs_all_in"] = jobinfo.job_name
                    system_consume_max["nfs_all_in"] = parameterscore.nfs_all_in
                if (parameterscore.nfs_all_out > system_consume_max["nfs_all_out"]):
                    system_consume_name["nfs_all_out"] = jobinfo.job_name
                    system_consume_max["nfs_all_out"] = parameterscore.nfs_all_out

        except Exception, e:
            print (e)

    job_consume_list_cpu = sorted(job_consume_list, key=lambda job_cpu: job_cpu.cpu)
    job_consume_list_network = sorted(job_consume_list, key=lambda job_network: job_network.network)
    job_consume_list_memory = sorted(job_consume_list, key=lambda job_memory: job_memory.memory)
    job_consume_list_disk = sorted(job_consume_list, key=lambda job_disk: job_disk.disk)
    job_consume_list_nfs = sorted(job_consume_list, key=lambda job_nfs: job_nfs.nfs)


    for jobinfo in jobinfos:
        try:
            if(jobinfo.benchmark):
                parameterscore = jobinfo.benchmark.benchmark_total_consume_score
                job = jobObject(jobinfo.job_name, get_cpuMax(parameterscore), get_networkMax(parameterscore),
                                get_memoryMax(parameterscore), get_diskMax(parameterscore), get_nfsMax(parameterscore))
                job_consume_list_acc.append(job)
        except Exception, e:
            print (e)

    job_consume_list_cpu_acc = sorted(job_consume_list_acc, key=lambda job_cpu: job_cpu.cpu)
    job_consume_list_network_acc = sorted(job_consume_list_acc, key=lambda job_network: job_network.network)
    job_consume_list_memory_acc = sorted(job_consume_list_acc, key=lambda job_memory: job_memory.memory)
    job_consume_list_disk_acc = sorted(job_consume_list_acc, key=lambda job_disk: job_disk.disk)
    job_consume_list_nfs_acc = sorted(job_consume_list_acc, key=lambda job_nfs: job_nfs.nfs)

    try:
        for item in environmentJob:
            print item
        nodes = [item for item in environmentJob]
        nodes = list(set(nodes))
    except Exception, e:
        print (e)

    if task.app_type == 0:
        majorType= '均衡型(null)'
    elif task.app_type == 1:
        majorType= 'CPU密集型(cpu_Bound)'
    elif task.app_type == 2:
        majorType = 'CPU浮点运算密集型(flops_Bound)'
    elif task.app_type == 3:
        majorType = '内存密集型(mem_Bound)'
    elif task.app_type == 4:
        majorType = 'IO密集型(io_Bound)'
    elif task.app_type == 5:
        majorType = '网络密集型(net_Bound)'

    paraBenchmarkScore = task.benchmark.benchmark_sorted_consume_score
    paraMainFeatureScore = task.main_feature

    class paraObject:
        def __init__(self, name, benchmark, mainFeature):
            self.name = name
            self.benchmark = benchmark
            self.mainFeature = mainFeature

    para = paraObject('cpu_all_cpi', paraBenchmarkScore.cpu_all_cpi, paraMainFeatureScore.cpu_all_cpi)
    paraScore_list.append(para)
    para = paraObject('cpu_all_idle', paraBenchmarkScore.cpu_all_idle, paraMainFeatureScore.cpu_all_idle)
    paraScore_list.append(para)
    para = paraObject('cpu_all_sywa', paraBenchmarkScore.cpu_all_sywa, paraMainFeatureScore.cpu_all_sywa)
    paraScore_list.append(para)
    para = paraObject('mem_all_mem_ratio', paraBenchmarkScore.mem_all_mem_ratio, paraMainFeatureScore.mem_all_mem_ratio)
    paraScore_list.append(para)
    para = paraObject('mem_all_swap_ratio', paraBenchmarkScore.mem_all_swap_ratio, paraMainFeatureScore.mem_all_swap_ratio)
    paraScore_list.append(para)
    para = paraObject('disk_all_write', paraBenchmarkScore.disk_all_write, paraMainFeatureScore.disk_all_write)
    paraScore_list.append(para)
    para = paraObject('disk_all_read', paraBenchmarkScore.disk_all_read, paraMainFeatureScore.disk_all_read)
    paraScore_list.append(para)
    para = paraObject('net_all_recv', paraBenchmarkScore.net_all_recv, paraMainFeatureScore.net_all_recv)
    paraScore_list.append(para)
    para = paraObject('net_all_send', paraBenchmarkScore.net_all_send, paraMainFeatureScore.net_all_send)
    paraScore_list.append(para)
    para = paraObject('nfs_all_in', paraBenchmarkScore.nfs_all_in, paraMainFeatureScore.nfs_all_in)
    paraScore_list.append(para)
    para = paraObject('nfs_all_out', paraBenchmarkScore.nfs_all_out, paraMainFeatureScore.nfs_all_out)
    paraScore_list.append(para)

    paraScoreSorted = sorted(paraScore_list, key=lambda para: para.mainFeature)

    length= len(job_consume_list)

    benchmark['cpu'] = get_cpuMax(paraBenchmarkScore)
    benchmark['network'] = get_networkMax(paraBenchmarkScore)
    benchmark['memory'] = get_memoryMax(paraBenchmarkScore)
    benchmark['disk'] = get_diskMax(paraBenchmarkScore)
    benchmark['nfs'] = get_nfsMax(paraBenchmarkScore)
    mainFeature['nfs'] = get_nfsMax(paraMainFeatureScore)
    mainFeature['cpu'] = get_cpuMax(paraMainFeatureScore)
    mainFeature['network'] = get_networkMax(paraMainFeatureScore)
    mainFeature['memory'] = get_memoryMax(paraMainFeatureScore)
    mainFeature['disk'] = get_diskMax(paraMainFeatureScore)

    context['taskid'] = taskid
    context['task'] = task
    context['nodes'] = nodes
    context['system_consume_name'] = system_consume_name
    context['system_consume_max'] = system_consume_max
    context['job_consume_list_cpu'] = job_consume_list_cpu
    context['job_consume_list_network'] = job_consume_list_network
    context['job_consume_list_memory'] = job_consume_list_memory

    context['job_consume_list_disk'] = job_consume_list_disk
    context['job_consume_list_nfs'] = job_consume_list_nfs
    context['job_consume_list_cpu_acc'] = job_consume_list_cpu_acc
    context['job_consume_list_network_acc'] = job_consume_list_network_acc
    context['job_consume_list_memory_acc'] = job_consume_list_memory_acc
    context['job_consume_list_disk_acc'] = job_consume_list_disk_acc
    context['job_consume_list_nfs_acc'] = job_consume_list_nfs_acc
    context['majorType'] = majorType
    context['benchmark'] = benchmark
    context['mainFeature'] = mainFeature
    context['paraScoreSorted'] = paraScoreSorted
    context['jobInfos'] = jobInfos
    context['programSugession'] = programSugession
    context['hardwareSugession'] = hardwareSugession
    if(length>15):
        context['height'] = length*25
    elif(length>5):
        context['height'] = max(length*30, 300)
    else:
        context['height'] = max(length*51, 200)
    return render_to_response('report/pfmtstReport.html',context)

def regressionReport(request,taskid):
    taskid = int(taskid)
    task = Tasks.objects.get(id = taskid)
    jobInfos = task.JobInfo.all()
    programSugession = task.Suggestion.filter(type=1)
    hardwareSugession = task.Suggestion.filter(type=2)
    context = {}
    jobName=[]
    phaseNames = []
    cpuIdle={}
    phaseNames=[]
    cpuIdle['sorted_consume_score']=[]
    cpuIdle['total_consume_score']=[]
    cpuIdle['time_density_score']=[]
    cpuIdle['max_score']=[]
    cpuIdle['average_score']=[]
    cpuFlops={}
    cpuFlops['sorted_consume_score']=[]
    cpuFlops['total_consume_score']=[]
    cpuFlops['time_density_score']=[]
    cpuFlops['max_score']=[]
    cpuFlops['average_score']=[]
    memRatio={}
    memRatio['sorted_consume_score']=[]
    memRatio['total_consume_score']=[]
    memRatio['time_density_score']=[]
    memRatio['max_score']=[]
    memRatio['average_score']=[]
    swapRatio={}
    swapRatio['sorted_consume_score']=[]
    swapRatio['total_consume_score']=[]
    swapRatio['time_density_score']=[]
    swapRatio['max_score']=[]
    swapRatio['average_score']=[]
    ioRatio={}
    ioRatio['sorted_consume_score']=[]
    ioRatio['total_consume_score']=[]
    ioRatio['time_density_score']=[]
    ioRatio['max_score']=[]
    ioRatio['average_score']=[]
    for job in jobInfos:
        phaseNames.append(job.phase_names)
        jobName.append(job.job_name)
        phaseNames.append(job.phase_names)
        benchmark=job.benchmark
        cpuIdle['sorted_consume_score'].append(benchmark.benchmark_sorted_consume_score.cpu_all_idle)
        cpuIdle['total_consume_score'].append(benchmark.benchmark_total_consume_score.cpu_all_idle)
        cpuIdle['time_density_score'].append(benchmark.benchmark_time_density_score.cpu_all_idle)

        cpuFlops['sorted_consume_score'].append(benchmark.benchmark_sorted_consume_score.cpu_all_flops)
        cpuFlops['total_consume_score'].append(benchmark.benchmark_total_consume_score.cpu_all_flops)
        cpuFlops['time_density_score'].append(benchmark.benchmark_time_density_score.cpu_all_flops)

        memRatio['sorted_consume_score'].append(benchmark.benchmark_sorted_consume_score.mem_all_mem_ratio)
        memRatio['total_consume_score'].append(benchmark.benchmark_total_consume_score.mem_all_mem_ratio)
        memRatio['time_density_score'].append(benchmark.benchmark_time_density_score.mem_all_mem_ratio)

        swapRatio['sorted_consume_score'].append(benchmark.benchmark_sorted_consume_score.mem_all_swap_ratio)
        swapRatio['total_consume_score'].append(benchmark.benchmark_total_consume_score.mem_all_swap_ratio)
        swapRatio['time_density_score'].append(benchmark.benchmark_time_density_score.mem_all_swap_ratio)

        ioRatio['sorted_consume_score'].append(benchmark.benchmark_sorted_consume_score.disk_all_write+benchmark.benchmark_sorted_consume_score.disk_all_read)
        ioRatio['total_consume_score'].append(benchmark.benchmark_total_consume_score.disk_all_write+benchmark.benchmark_total_consume_score.disk_all_read)
        ioRatio['time_density_score'].append(benchmark.benchmark_time_density_score.disk_all_write+benchmark.benchmark_sorted_consume_score.disk_all_read)

        statistic=job.statistic
        cpuIdle['max_score'].append(statistic.max_score.cpu_all_idle)
        cpuIdle['average_score'].append(statistic.average_score.cpu_all_idle)
        cpuFlops['max_score'].append(statistic.max_score.cpu_all_flops)
        cpuFlops['average_score'].append(statistic.average_score.cpu_all_flops)
        memRatio['max_score'].append(statistic.max_score.mem_all_mem_ratio)
        memRatio['average_score'].append(statistic.average_score.mem_all_mem_ratio)
        swapRatio['max_score'].append(statistic.max_score.mem_all_swap_ratio)
        swapRatio['average_score'].append(statistic.average_score.mem_all_swap_ratio)
        ioRatio['max_score'].append(statistic.max_score.disk_all_write+statistic.max_score.disk_all_read)
        ioRatio['average_score'].append(statistic.average_score.disk_all_write+statistic.average_score.disk_all_read)

    phaseType = task.regression_reportType
    percentage_type = {}
    percentage_type['null'] = get_percentage(phaseType, phaseType.nullType)
    percentage_type['cpu']= get_percentage(phaseType, phaseType.cpuType)
    percentage_type['network']= get_percentage(phaseType, phaseType.networkType)
    percentage_type['disk']= get_percentage(phaseType, phaseType.diskType)
    percentage_type['memory']= get_percentage(phaseType, phaseType.memoryType)


    abnormalType = AbnormalType.objects.all()

    context['phaseNames'] = phaseNames
    context['task']=task
    context['jobName']=jobName
    context['phaseNames']=phaseNames
    context['percentage_type'] = percentage_type

    context['cpuIdle']=cpuIdle
    context['cpuFlops']=cpuFlops
    context['memRatio']=memRatio
    context['swapRatio']=swapRatio
    context['ioRatio']=ioRatio
    context['taskid']=taskid
    context['abnormalType'] = abnormalType
    context['programSugession'] = programSugession
    context['hardwareSugession'] = hardwareSugession

    return render_to_response('report/regressionReport.html',context)

def detail(request, taskid, jobID):
    taskid = int(taskid)
    jobID = int(jobID)
    jobInfo = JobInfo.objects.get(id=jobID)
    task = Tasks.objects.get(id=taskid)
    environmentJob = task.nodes.all()
    abnormalType = AbnormalType.objects.all()
    simulationEnvironments = task.simulationEnvironments.all()
    programSugession = jobInfo.Suggestion.filter(type=1)
    hardwareSugession = jobInfo.Suggestion.filter(type=2)
    cmpconfig_task = CmpConfigT.objects.filter(taskid=taskid)
    cmpconfig_jobs = cmpconfig_task.filter(jobname=jobInfo.job_number)
    context = {}
    benchmark = {}
    mainFeature = {}
    paraScore_list = []

    try:
        for item in environmentJob:
            print item
        nodes = [item for item in environmentJob]
        nodes = list(set(nodes))
    except Exception, e:
        print (e)

    if jobInfo.job_type == 0:
        majorType = '均衡型(null)'
    elif jobInfo.job_type == 1:
        majorType = 'CPU密集型(cpu_Bound)'
    elif jobInfo.job_type == 2:
        majorType = 'CPU浮点运算密集型(flops_Bound)'
    elif jobInfo.job_type == 3:
        majorType = '内存密集型(mem_Bound)'
    elif jobInfo.job_type == 4:
        majorType = 'IO密集型(io_Bound)'
    elif jobInfo.job_type == 5:
        majorType = '网络密集型(net_Bound)'

    paraBenchmarkScore = jobInfo.benchmark.benchmark_sorted_consume_score
    paraMainFeatureScore = jobInfo.main_feature

    class paraObject:
        def __init__(self, name, benchmark, mainFeature):
            self.name = name
            self.benchmark = benchmark
            self.mainFeature = mainFeature

    para = paraObject('cpu_all_cpi', paraBenchmarkScore.cpu_all_cpi, paraMainFeatureScore.cpu_all_cpi)
    paraScore_list.append(para)
    para = paraObject('cpu_all_idle', paraBenchmarkScore.cpu_all_idle, paraMainFeatureScore.cpu_all_idle)
    paraScore_list.append(para)
    para = paraObject('cpu_all_sywa', paraBenchmarkScore.cpu_all_sywa, paraMainFeatureScore.cpu_all_sywa)
    paraScore_list.append(para)
    para = paraObject('mem_all_mem_ratio', paraBenchmarkScore.mem_all_mem_ratio, paraMainFeatureScore.mem_all_mem_ratio)
    paraScore_list.append(para)
    para = paraObject('mem_all_swap_ratio', paraBenchmarkScore.mem_all_swap_ratio,
                      paraMainFeatureScore.mem_all_swap_ratio)
    paraScore_list.append(para)
    para = paraObject('disk_all_write', paraBenchmarkScore.disk_all_write, paraMainFeatureScore.disk_all_write)
    paraScore_list.append(para)
    para = paraObject('disk_all_read', paraBenchmarkScore.disk_all_read, paraMainFeatureScore.disk_all_read)
    paraScore_list.append(para)
    para = paraObject('net_all_recv', paraBenchmarkScore.net_all_recv, paraMainFeatureScore.net_all_recv)
    paraScore_list.append(para)
    para = paraObject('net_all_send', paraBenchmarkScore.net_all_send, paraMainFeatureScore.net_all_send)
    paraScore_list.append(para)
    para = paraObject('nfs_all_in', paraBenchmarkScore.nfs_all_in, paraMainFeatureScore.nfs_all_in)
    paraScore_list.append(para)
    para = paraObject('nfs_all_out', paraBenchmarkScore.nfs_all_out, paraMainFeatureScore.nfs_all_out)
    paraScore_list.append(para)

    paraScoreSorted = sorted(paraScore_list, key=lambda para: para.mainFeature)

    benchmark['cpu'] = get_cpuMax(paraBenchmarkScore)
    benchmark['network'] = get_networkMax(paraBenchmarkScore)
    benchmark['memory'] = get_memoryMax(paraBenchmarkScore)
    benchmark['disk'] = get_diskMax(paraBenchmarkScore)
    benchmark['nfs'] = get_nfsMax(paraBenchmarkScore)
    mainFeature['nfs'] = get_nfsMax(paraMainFeatureScore)
    mainFeature['cpu'] = get_cpuMax(paraMainFeatureScore)
    mainFeature['network'] = get_networkMax(paraMainFeatureScore)
    mainFeature['memory'] = get_memoryMax(paraMainFeatureScore)
    mainFeature['disk'] = get_diskMax(paraMainFeatureScore)

    context['jobInfo'] = jobInfo
    context['taskid'] = taskid
    context['task'] = task
    context['nodes'] = nodes
    context['jobID'] = jobID
    context['majorType'] = majorType
    context['benchmark'] = benchmark
    context['mainFeature'] = mainFeature
    context['paraScoreSorted'] = paraScoreSorted
    context['programSugession'] = programSugession
    context['hardwareSugession'] = hardwareSugession
    context['cmpconfig_jobs'] = cmpconfig_jobs
    context['abnormalType'] = abnormalType

    return render_to_response('report/detail.html', context)

def abnormalData(request):
    taskid = request.POST['taskid']
    abnormalid = request.POST['abnormalid']
    jobid = request.POST['jobid']
    abnormal = JobAbnormal.objects.get(id=int(abnormalid))
    jobname = abnormal.jobname
    hostid = abnormal.hostid
    parameters = abnormal.parameter.encode("UTF-8").rsplit(',')
    params = []
    legend = []
    for parameter in parameters:
        params.append(parameter)
        legend.append(parameter.rsplit(':')[-1])
    ##legend = ['net_all_send','MemTotal']
    start_time = abnormal.start_time
    end_time = abnormal.end_time
    start_time = (start_time.strftime('%Y-%m-%d %H:%M:%S'))
    end_time = (end_time.strftime('%Y-%m-%d %H:%M:%S'))
    start_time = str(int(time.mktime(time.strptime(start_time,'%Y-%m-%d %H:%M:%S'))) + 8*60*60)
    end_time = str(int(time.mktime(time.strptime(end_time,'%Y-%m-%d %H:%M:%S'))) + 8*60*60)
    #start_time = str (int (time.mktime(start_time)))
    #end_time = str (int (time.mktime(end_time)))
    ptype = 1
    param = {'hostid': hostid, 'end': end_time, 'ptype': ptype, 'jobname': jobname, 'start': start_time, 'params': params, 'taskid': int(taskid)}
    data = sendZmqReq(param)
    re = {}
    if int(data['flag']) == 0:
        re['flag'] = 0
        return HttpResponse(json.dumps(re))
    #data = {"flag": 1, "data": {"timestamp": ["1472004221.0", "1472004222.0", "1472004223.0", "1472004224.0", "1472004225.0", "1472004226.0", "1472004227.0", "1472004228.0", "1472004229.0", "1472004230.0", "1472004231.0", "1472004232.0", "1472004233.0", "1472004234.0", "1472004235.0", "1472004236.0", "1472004237.0", "1472004238.0", "1472004239.0", "1472004240.0", "1472004241.0", "1472004242.0"], "MemTotal": [131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012, 131984012], "net_all_send": [0.0, 63032.25, 0.0, 226081.12, 53.13, 126306.83, 0.0, 44840.77, 0.0, 232052.65, 0.0, 121114.62, 0.0, 61537.46, 0.0, 232816.38, 163.11, 102496.53, 56.02, 52617.43, 0.0, 228059.37]}}
    re['flag'] = 1
    timestamps = data['data']['timestamp']
    categories = []
    for timestamp in timestamps:
        t = time.localtime(int(float(timestamp)+28800))
        s = time.strftime('%H:%M:%S',t)
        categories.append(s)
    re['categories'] = categories
    re['legend'] = legend
    i = 1
    for le in legend:
        key = 'data' + str(i)
        re[key] = data['data'][le]
        i = i+1

    return HttpResponse(json.dumps(re))
