#!/usr/bin/python3
""" creates and distributes an archive to your web servers """
from fabric.api import local, run, put, env
from datetime import datetime
import os
import sys
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['100.26.221.219', '100.25.20.74']
if len(sys.argv) > 4:
    env.key_filename = sys.argv[4]
else:
    env.key_filename = None
if len(sys.argv) > 6:
    env.user = sys.argv[6]
else:
    env.user = None


def deploy():
    """ define the function deploy """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
