#!/usr/bin/python3
""" distributes an archive to your web servers """
from fabric.api import local, run, put, env
from datetime import datetime
import os
import sys

env.hosts = ['100.26.221.219', '100.25.20.74']
if len(sys.argv) > 4:
    env.key_filename = sys.argv[4]
else:
    env.key_filename = None
if len(sys.argv) > 6:
    env.user = sys.argv[6]
else:
    env.user = None


def do_deploy(archive_path):
    """ defines the function do_deploy """

    try:
        if not os.path.exists(archive_path):
            return False

        remote_arch_path = "/tmp/{}".format(os.path.basename(archive_path))
        put(archive_path, remote_arch_path, use_sudo=True)

        release = os.path.splitext(os.path.basename(archive_path))[0]
        rel_path = "/data/web_static/releases/{}".format(release)
        run("mkdir -p {}".format(rel_path))
        run("tar -xzf {} -C {}".format(remote_arch_path, rel_path))

        run("rm -f {}".format(remote_arch_path))

        link_path = '/data/web_static/current'
        run("rm -f {}".format(link_path))

        run("ln -s {} {}".format(rel_path, link_path))

        return True
    except Exception as e:
        return False
