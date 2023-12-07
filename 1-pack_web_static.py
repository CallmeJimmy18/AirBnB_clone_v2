#!/usr/bin/python3
""" Fabric script generates .tgz archive from the contents of web_static """
from fabric.api import local, run
from datetime import datetime
import os


def do_pack():
    """ define the do_pack function """

    source = "web_static"
    destination = "versions"

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_filename = "web_static_{}.tgz".format(timestamp)

    local("mkdir -p {}".format(destination))
    local("tar -czvf {}/{} -C {}".format(destination, archive_filename,
                                         source))
    archive_path = "{}/{}".format(destination, archive_filename)

    if os.path.exists(archive_path):
        return archive_path
    else:
        return None
