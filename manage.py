#!/usr/bin/env python
import os
import sys
import time
import zmq
import threading
import httplib

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apm.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
