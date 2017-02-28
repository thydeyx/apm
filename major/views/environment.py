
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import json
from major.models import *

def environment(request):
    environments = Environment.objects.all()
    context = Context()
    context['environments'] = environments
    nodes = Node.objects.all()
    context['nodes'] = nodes
    username = request.session.get('username', '')
    if username == '':
        return HttpResponseRedirect('/login')
    context['username'] = username
    return render_to_response("config/environmentConfig.html", context)


def addEnvironment(request):
    req = json.loads(request.body)
    environment = Environment()
    environment.name = req['environment-name']
    environment.description = req['environment-description']
    environment.save()
    for key in req['nodes']:
        environmentNodes = (Node.objects.get(name=key.strip().encode("utf8")))
        print (environmentNodes)
        environment.node.add(environmentNodes)
    environment.save()
    return HttpResponse("EnvironmentAdded")


def editEnvironment(request):
    req = json.loads(request.body)
    environment = Environment.objects.get(id=req['environment-id'])
    environment.name = req['environment-name']
    environment.description = req['environment-description']
    for nodesold in environment.node.all():
        environment.node.remove(nodesold)
    for key in req['nodes']:
        environmentNodes = Node.objects.get(name=key)
        environment.node.add(environmentNodes)
    environment.save()
    return HttpResponse("TemplateDataUpdated")


def deleteEnvironment(request):
    environment = Environment.objects.get(id=request.POST['id'])
    environment.delete()
    return HttpResponse("EnvironmentDataDelete")