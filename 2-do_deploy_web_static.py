#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import *
from datetime import datetime
from os import path
env.hosts = ['34.73.99.74', '35.231.27.105']
env.user = ['ubuntu']


def do_deploy(archive_path):
    """ Fabric script that distributes an archive to your web servers"""
    if archive_path is None:
        return False

    filename = archive_path.split('/')[-1]
    try:
        put(archive_path, '/tmp/')
        pathfile = '/data/web_static/releases/' + filename.split('.')[0]
        run("sudo mkdir -p /data/web_static/releases/{}"
            .format(filename.split('.')[0]))
        sudo("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(filename))
        sudo("sudo rm  /tmp/{}".format(filename))
        sudo("sudo rm -rf /data/web_static/current/*")
        sudo("sudo ln -s /data/web_static/current/\
            /data/web_static/releases/{}".format(filename.split('.')[0]))
        return True
    except:
        return False
