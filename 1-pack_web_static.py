#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from fabric.api import local
from datetime import datetime
from os import path


def do_pack():
    """ Fabric script that generates a .tgz archive"""
    date = datetime.today().isoformat()
    name_file = "versions/web_static_" + date + ".tgz"
    local('mkdir -p versions')
    if local('tar -czvf {} web_static'.format(name_file)):
        return name_file
    else:
        return None
