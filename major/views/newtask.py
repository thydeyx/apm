#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2015-10-21 09:54:45
# @Last Modified by:   anchen
# @Last Modified time: 2016-06-25 20:26:07

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.http import JsonResponse
import json
from major.models import *
import time


def newtask(request):

    nodes = Node.objects.all()
    jobstreams = JobStream.objects.all()
    templates = Template.objects.all()
    parameters = Parameters.objects.all()
    environments = Environment.objects.all()
    CPUs = Parameters.objects.filter(type="CPU")
    Memorys = Parameters.objects.filter(type="Memory")
    Networks = Parameters.objects.filter(type="Network")
    IOs = Parameters.objects.filter(type="I/O")
    NFSs = Parameters.objects.filter(type="NFS")
    username = request.session.get('username', '')

    context = Context()
    context['username'] = username
    context['nodes'] = nodes
    context['jobstreams'] = jobstreams
    context['templates'] = templates
    context['parameters'] = parameters
    context['environments'] = environments
    context['CPUs'] = CPUs
    context['Memorys'] = Memorys
    context['Networks'] = Networks
    context['IOs'] = IOs
    context['NFSs'] = NFSs

    return render_to_response("task/newtask.html", context)

def simulationConfig(request):
    req = json.loads(request.body)
    ename = req['name']
    result = []
    simulationEnvironments = SimulationEnvironment.objects.filter(environment=Environment.objects.get(name=ename))
    for simulation in simulationEnvironments:
        result.append({'name':simulation.name,'description':simulation.description})

    return HttpResponse(json.dumps(result),content_type="application/json")

def addtask(request):
    try:
        req = json.loads(request.body)
        task = Tasks()
        task.name = req['name'].encode('utf8')
        task.type = TaskType.objects.get(name=req['type'].encode('utf8'))
        task.introduction = req['introduction'].encode('utf8')
        task.process = req['process']
        task.start_date = '---'
        task.start_time = '---'
        task.end_time = '---'
        task.end_date = '---'
        username = request.session.get('username', '')
        task.user = Users.objects.get(name = username)
        task.data_type = req['datatype'].encode('utf8')
        try:
            if req['jobstream']:
                task.regression_jobstream = JobStream.objects.get(name = req['jobstream'])

            if req['start_date'] and req['start_time']:
                task.regression_start_time = req['start_date'] + ' ' + req['start_time']

            if req['end_date'] and req['end_time']:
                task.regression_end_time = req['end_date'] + ' ' + req['end_time']
        except Exception, e:
            print (e)
        task.save()
        for key in req['parameters']:
            taskparameterconfigs = Parameters.objects.get(name=key.strip().encode("utf8"))
            task.parameterconfigs.add(taskparameterconfigs)
        if req['nodejobs']:
            for key in req['nodejobs']:
                for item in req['nodejobs'][key]:
                    jobstream = JobStream.objects.get(name=item.encode("utf8"))
                    nodejob = EnvironmentJob.objects.get_or_create(environment=Environment.objects.get(name=key.encode('utf8')),job=jobstream)
                    nodejob[0].save()
                    for job in jobstream.jobs.all():
                        task.JobInfo.add(JobInfo.objects.create(job_name = job.name,job_number=job.number))
                    task.save()
                    task.nodes.add(nodejob[0])
        if req['jobModes']:
            jobModes = req['jobModes']
            for jobinfo in task.JobInfo.all():
                for key in jobModes:
                    if cmp(jobinfo.job_name, key) == 0:
                        if jobModes[key]:
                            jobinfo.runmode = RunMode.objects.get(name=jobModes[key].encode("utf8"))
                            jobinfo.save()
            task.save()
        if req['simulations']:
            for key in req['simulations']:
                simulation = SimulationEnvironment.objects.get(name=key)
                task.simulationEnvironments.add(simulation)
            task.save()
    except Exception, e:
        print (e)
    return JsonResponse({})


def edit(request):
    template_id = request.POST['template-id']
    node_id = request.POST['node-id']
    jobstream_id = request.POST['jobstream-id']
    template = Template.objects.get(id=template_id)
    template.jobstream = JobStream.objects.get(id=jobstream_id)
    template.node = Node.objects.get(id=node_id)
    template.save()
    return HttpResponse("data updated!")


def editPara(request):
    req = json.loads(request.body)
    template_id = req['template_id']
    template = Template.objects.get(id=template_id)
    for parameterold in template.parameter.all():
        template.parameter.remove(parameterold)
    for para_id in req['para_id']:
        parameter = Parameters.objects.get(id=para_id)
        print (parameter.name)
        template.parameter.add(parameter)
    template.save()
    return JsonResponse({})
