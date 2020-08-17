#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import *

env.hosts = ['34.73.99.74', '35.231.27.105']
env.user = ['ubuntu']


def do_deploy(archive_path):
    """ Fabric script that distributes an archive to your web servers"""
    if archive_path is None:
        return False

    filename = archive_path.split('/')[-1]
    try:
        put(filename, '/tmp/')
        pathfile = '/data/web_static/releases/' + filename.split('.')[0]
        foldername = "/data/web_static/releases/" + filename.split('.')[0]
        run("sudo mkdir -p {}/".format(foldername))
        run("sudo tar -xzf /tmp/{} -C {}/".format(filename, foldername))
        run("sudo rm  /tmp/{}".format(filename))
        run("sudo rm -rf {}/web_static".format(foldername))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}\
            /data/web_static/current/".format(foldername))
        return True

    except Exception:
        return False
