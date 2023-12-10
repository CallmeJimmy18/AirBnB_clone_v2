#!/usr/bin/python3
""" Fabric script generates .tgz archive from the contents of web_static """
from fabric.api import local, run
from datetime import datetime
import os


def do_pack():
    """ define the do_pack function """

    source = "web_static"
    local("mkdir -p versions")

    time_now = datetime.utcnow()
    archive_filename = "web_static_{}{}{}{}{}{}.tgz".format(
                                                            time_now.year,
                                                            time_now.month,
                                                            time_now.day,
                                                            time_now.hour,
                                                            time_now.minute,
                                                            time_now.second
                                                            )

    result = local("tar -cvzf versions/{} web_static".format(archive_filename))

    if result.failed:
        return None
    else:
        return os.path.join("versions", archive_filename)
