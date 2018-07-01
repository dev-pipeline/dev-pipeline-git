#!/usr/bin/python3

"""This modules implement support for Git SCM tools."""

import devpipeline_plugins.git.git

def get_scms():
    return {
        "git": devpipeline_plugins.git.git._make_git
    }
