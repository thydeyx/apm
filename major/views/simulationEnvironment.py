
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import json
from major.models import *

def simulationEnvironment(request):
    simulationEnvironments = SimulationEnvironment.objects.all()
    environments = Environment.objects.all()
    context = Context()
    context['simulationEnvironments'] = simulationEnvironments
    context['environments'] = environments
    nodes = Node.objects.all()
    context['nodes'] = nodes
    username = request.session.get('username', '')
    if username == '':
        return HttpResponseRedirect('/login')
    context['username'] = username
    return render_to_response("config/simulationEnvironmentConfig.html", context)


def addSimulationEnvironment(request):
    req = json.loads(request.body)
    simulationEnvironment = SimulationEnvironment()
    simulationEnvironment.name = req['simulationEnvironment-name']
    simulationEnvironment.description = req['simulationEnvironment-description']
    environmentId = req['simulationEnvironment-environment']
    simulationEnvironment.environment = Environment.objects.get(id=environmentId)
    simulationEnvironment.save()
    for key in req['nodes']:
        simulationEnvironmentNodes = (Node.objects.get(name=key.strip().encode("utf8")))
        print (simulationEnvironmentNodes)
        simulationEnvironment.node.add(simulationEnvironmentNodes)
    simulationEnvironment.save()
    return HttpResponse("SimulationEnvironmentAdded")


def editSimulationEnvironment(request):
    req = json.loads(request.body)
    simulationEnvironment = SimulationEnvironment.objects.get(id=req['simulationEnvironment-id'])
    simulationEnvironment.name = req['simulationEnvironment-name']
    simulationEnvironment.description = req['simulationEnvironment-description']
    environmentId = req['simulationEnvironment-environment']
    simulationEnvironment.environment = Environment.objects.get(id=environmentId)
    for nodesold in simulationEnvironment.node.all():
        simulationEnvironment.node.remove(nodesold)
    for key in req['nodes']:
        simulationEnvironmentNodes = Node.objects.get(name=key)
        simulationEnvironment.node.add(simulationEnvironmentNodes)
    simulationEnvironment.save()
    return HttpResponse("TemplateDataUpdated")


def deleteSimulationEnvironment(request):
    simulationEnvironment = SimulationEnvironment.objects.get(id=request.POST['id'])
    print (simulationEnvironment)
    simulationEnvironment.delete()
    return HttpResponse("SimulationEnvironmentDataDelete")