#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import *
from os.path import exists

env.hosts = ['34.73.99.74', '35.231.27.105']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Fabric script that distributes an archive to your web servers"""
    if not exists(archive_path):
        return False

    try:
        filename = archive_path.split('/')[-1]
        put(archive_path, '/tmp/')
        pathfile = '/data/web_static/releases/' + filename
        foldername = "/data/web_static/releases/" + filename.split('.')[0]
        run("sudo mkdir -p {}/".format(foldername))
        run("sudo tar -xzf /tmp/{} -C {}/".format(filename, foldername))
        run("sudo rm  /tmp/{}".format(filename))
        run('sudo mv {}/web_static/* {}/'.format(foldername, foldername))
        run("sudo rm -rf {}/web_static".format(foldername))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/\
            /data/web_static/current".format(foldername))
        return True

    except Exception:
        return False
    return True
