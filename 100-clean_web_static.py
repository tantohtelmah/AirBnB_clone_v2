#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives using the function do_clean.
"""

from fabric.api import env, run, local
from os.path import exists
env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs
env.user = 'ubuntu'  # Replace with actual username


def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Args:
        number (int): Number of archives to keep (including the most recent).

    Example:
        If number is 2, keep the most recent and second most recent versions.
    """
    if number < 1:
        number = 1

    # Delete unnecessary archives in versions folder
    local("ls -t versions | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number + 1))

    # Delete unnecessary archives in /data/web_static/releases folder
    releases = run("ls -t /data/web_static/releases").split()
    for release in releases[number:]:
        if exists("/data/web_static/releases/{}".format(release)):
            run("rm -rf /data/web_static/releases/{}".format(release))
