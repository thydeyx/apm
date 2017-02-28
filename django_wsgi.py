# -*- coding: utf-8 -*-
# !/usr/bin/python

# @author: YangYu
# @date: 15/11/3
# @description:



import os
import sys
reload(sys)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apm.settings")
from django.core.wsgi import get_wsgi_application

application =get_wsgi_application()