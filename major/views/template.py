from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import json
from major.models import *

def edit(request):
    req = json.loads(request.body)
    template = Template.objects.get(id=req['template-id'])
    print (req['template-name'])
    template.name = req['template-name']
    template.description = req['template-desc']
    for parameterold in template.parameter.all():
        template.parameter.remove(parameterold)
    for key in req['parameters']:
        parameter = Parameters.objects.get(name=key)
        template.parameter.add(parameter)
    template.save()
    return HttpResponse("TemplateDataUpdated")

def add(request):
    req = json.loads(request.body)
    template = Template()
    template.name = req['template-name']
    template.description = req['template-desc']
    template.save()
    for key in req['parameters']:
        templateParameters = (Parameters.objects.get(name=key.strip().encode("utf8")))
        templateParameters.save()
        template.parameter.add(templateParameters)
    return HttpResponse("TemplateAdded")

def delete(request):
    template = Template.objects.get(id=request.POST['id'])
    template.delete()
    return HttpResponse("TemplateDataDelete")
