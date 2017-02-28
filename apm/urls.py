# -*- coding: utf-8 -*-
# !/usr/bin/python

# @author: YangYu
# @date: 15/10/13
# @description:


"""apm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import *
from major.views import index, newtask, user, config, node, task, echart, usermanagement, template, environment, zmqs, simulationEnvironment, report


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/page/(\d+)/$', index.index),
    url(r'^index/$',index.redirect),
    url(r'^$',index.redirect),
    url(r'^index/edit/$',index.edit),
    url(r'^index/delete/$',index.delete),
    url(r'^index/detail/(\d+)/$', index.detail),
    #url(r'^index/newtask/$',newtask.newtask)
    url(r'^index/newtask/$',newtask.newtask)
]

urlpatterns += [
    url(r'^zmq/finish/(\d+)/$', zmqs.finishwork),
    url(r'^zmq/finishwrong/(\d+)/$', zmqs.finishworkwrong),
    url(r'^task/change/(\d+)/$', zmqs.change),
	url(r'^ELKPlatform/loadServer-INTERFACE$', zmqs.hardwares),
    url(r'^ELKPlatform/loadJobData-INTERFACE$', zmqs.loadJobData),
    url(r'^ELKPlatform/loadServerData-INTERFACE$', zmqs.loadServerData),
	url(r'^ELKPlatform/loadMem$', zmqs.loadMem),
	url(r'^ELKPlatform/loadNet$', zmqs.loadNet),
	url(r'^ELKPlatform/loadCpu$', zmqs.loadCpu),
	url(r'^ELKPlatform/loadIo$', zmqs.loadIo),
	url(r'^ELKPlatform/loadMicroarch$', zmqs.loadMicroarch),
	url(r'^ELKPlatform/loadDfs$', zmqs.loadDfs),
    url(r'^ELKPlatform/loadtask$', zmqs.deletetask),
]

urlpatterns += [

    url(r'^login/$', usermanagement.login, name = 'login'),
    url(r'^regist/$', usermanagement.regist, name = 'regist'),
    url(r'^logout/$', usermanagement.logout, name = 'logout'),
]

urlpatterns += [
    url(r'^task/(\d+)/$', task.taskinfo),

    url(r'^task/(\d+)/unuslReport$', task.taskUnusual),
    url(r'^task/(\d+)/unuslReport/ioedit$', task.ioedit),
    url(r'^task/(\d+)/sysevlReport$', task.taskinfo),
    url(r'^task/updateStatus/$', task.updateStatus),
    url(r'^task/collectTimer/$', task.collectTimer),
    url(r'^task/analysisTimer/$', task.analysisTimer),


]
urlpatterns += [
    url(r'^task/(\d+)/regressionReport$', report.regressionReport),
    url(r'^task/(\d+)/pfmtstReport$', report.pfmtstReport),
    url(r'^task/(\d+)/pfmtstReport/(\d+)$', report.detail),
    url(r'^report/abnormalData/$', report.abnormalData),
]

urlpatterns += [ 
    url(r'^newtask/$',newtask.addtask),
    url(r'^newtask/edit/$', newtask.edit),
    url(r'^newtask/simulationConfig/$', newtask.simulationConfig),
]

urlpatterns += [
    url(r'^userprofile/$',user.user),
    url(r'^userprofile/edit$', user.editUser),
    url(r'^userprofile/delete$', user.deleteUser),
    url(r'^userprofile/add$', user.addUser),
]

urlpatterns += [
    url(r'^environment/$',environment.environment),
    url(r'^environment/edit$', environment.editEnvironment),
    url(r'^environment/delete$', environment.deleteEnvironment),
    url(r'^environment/add$', environment.addEnvironment),
]

urlpatterns += [
    url(r'^simulationEnvironment/$',simulationEnvironment.simulationEnvironment),
    url(r'^simulationEnvironment/edit$', simulationEnvironment.editSimulationEnvironment),
    url(r'^simulationEnvironment/delete$', simulationEnvironment.deleteSimulationEnvironment),
    url(r'^simulationEnvironment/add$', simulationEnvironment.addSimulationEnvironment),
]


urlpatterns += [
    url(r'^appConfig/(\d+)/$', config.jobinfo),
    url(r'^job/edit$', config.editJob),
    url(r'^nodeConfig/$', config.nodeConfig),
    url(r'^appConfig/$', config.jobStream),
    url(r'^templateConfig/$', config.templateConfig),
    url(r'^nodeState/$', config.nodeState),
    url(r'^config/inTimeState/$', config.inTimeState),
]

urlpatterns += [
    url(r'^node/edit$', node.edit),
    url(r'^node/delete$', node.delete),
    url(r'^node/add$', node.addNode),
    url(r'^node/getServer$', node.getServers)
]

urlpatterns += [

    url(r'^echart/getData$', echart.getData),
]

urlpatterns += [
    url(r'^template/edit$',template.edit),
    url(r'^template/delete$', template.delete),
    url(r'^template/add$', template.add),
]

urlpatterns +=[
    url(r'^mode/edit$', config.editMode),
    url(r'^mode/add$', config.addMode),
    url(r'^job/add$', config.addJob),
    url(r'^jobstream/edit$', config.editJobStream),
    url(r'^jobstream/add$', config.addJobStream),
    url(r'^jobstream/delete$', config.deleteJobStream),
]
