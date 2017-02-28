# -*- coding: utf-8 -*-
# !/usr/bin/python

# @author: YangYu
# @date: 15/10/22
# @description:


import json

from django.core import serializers


class QuerySetEncoder(json.JSONEncoder):
    """
    Encoding QuerySet into JSON format.
    """
    def default(self, object):
        try:
            return serializers.serialize("python", object, ensure_ascii=False)
        except :
            return json.JSONEncoder.default(self, object)