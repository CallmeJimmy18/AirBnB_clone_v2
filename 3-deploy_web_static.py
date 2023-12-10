#!/usr/bin/python3
""" creates and distributes an archive to your web servers """
from fabric.api import local, run, put, env
from datetime import datetime
import os

env.hosts = ['100.26.221.219', '100.25.20.74']


def do_pack():
    """ define the do_pack function """

    source = "web_static"
    local("mkdir -p versions")

    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_filename = "versions/eb_static_{}.tgz".format(time_now)

    result = local("sudo tar -cvzf {} web_static".format(archive_filename))

    if result.failed:
        return None
    else:
        return archive_filename

def do_deploy(archive_path):
    """ defines the function do_deploy """

    if os.path.exists(archive_path) is False:
        return False
    release = archive_path.split('/')[-1]
    rel_path = '/data/web_static/releases/' + "{}".format(release.split('.')[0])

    try:
        put(archive_path, "/tmp/")


        run("mkdir -p {}/".format(rel_path))
        run("tar -xzf /tmp/{} -C {}/".format(release, rel_path))

        run("rm /tmp/{}".format(release))
        run("mv {}/web_static/* {}/".format(rel_path, rel_path))
        run("rm -rf {}/web_static".format(rel_path))

        run("rm -rf /data/web_static/current")

        run("ln -s {}/ /data/web_static/current".format(rel_path))

        return True
    except:
        return False

def deploy():
    """ define the function deploy """
    archive_path = do_pack()
    if os.path.exists(archive_path) is False:
        return False
    result = do_deploy(archive_path)
    return result
