#!/usr/bin/python3
# distributes an archive to your web servers, using the
# function do_deploy
from fabric.api import *
from fabric.operations import put, sudo, run
import os.path
env.hosts = ['66.70.184.33', '184.72.199.191']


def do_deploy(archive_path):
    """ """
    if (os.path.isfile(archive_path) is False):
        return False
    try:
        put(archive_path, "/tmp/")
        archivepath1 = (archive_path.split("/")[-1])
        archivepath2 = archivepath1.split(".")
        run("sudo mkdir -p /data/web_static/releases/{}".format
            (archivepath2[0]))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format
            (archivepath1, archivepath2[0]))
        run("sudo rm /tmp/{}".format(archivepath1))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}".format(archivepath2[0], archivepath2[0]))
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(archivepath2[0]))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} \
        /data/web_static/current".format(archivepath2[0]))
        return True
    except:
        return False
