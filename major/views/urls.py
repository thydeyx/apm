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
from major.views import index, newtask, user, config, node,task,echart,usermanagement


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^index/page/(\d+)/$', index.index),

    url(r'^index/$',index.redirect),
    url(r'^$',index.redirect),
    url(r'^index/edit/$',index.edit),
    url(r'^index/delete/$',index.delete),
    url(r'^index/detail/(\d+)/$', index.detail),
    url(r'^index/newtask/$',newtask.newtask)
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

    url(r'^task/(\d+)/pfmtstReport$', task.taskinfo),
    url(r'^task/(\d+)/sysevlReport$', task.taskinfo),

]

urlpatterns += [ 
    url(r'^newtask/$',newtask.addtask),
    url(r'^newtask/edit/$', newtask.edit),

]
urlpatterns += [
    url(r'^userprofile/$', user.user),
    url(r'^userprofile/edit$', user.editUser),
    url(r'^userprofile/delete$', user.deleteUser),
    url(r'^userprofile/add$', user.addUser),
]
urlpatterns += [
    url(r'^nodeConfig/$', config.nodeConfig),
    url(r'^appConfig/$', config.appConfig),
    url(r'templateConfig/$', config.templateConfig),
]
urlpatterns += [
    url(r'^node/edit$', node.edit),
    url(r'^node/delete$', node.delete),
    url(r'^node/add$', node.addNode),
]

urlpatterns += [
    url(r'^echart/getData$', echart.getData),
]

