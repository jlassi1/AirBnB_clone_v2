#!/usr/bin/python3
"""Fabric script that deletes out-of-date archives, using the function do_clean"""
from fabric.api import *
from datetime import datetime
from os.path import exists
env.hosts = ['34.73.99.74', '35.231.27.105']
env.user = "ubuntu"


def do_clean(number=0):
    """ """
    