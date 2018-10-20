#!/usr/bin/python3

"""
The main module for devpipeline_git (a dev-pipeline plugin).  It provides git
support to dev-pipeline, and exposes the make_git function to create an Scm
that supports git.
"""

import devpipeline_git.git


def make_git(current_target):
    """
    Create a class that provides git SCM support.

    Arguments
    current_target - The configuration for the currently processed target.
                     Black box, don't look at it directly.
    common_wrapper - A function to hook into executors and other common
                     functionality.
    """
    # pylint: disable=protected-access
    return devpipeline_git.git._make_git(current_target)


_MAJOR = 0
_MINOR = 2
_PATCH = 0

_STRING = "{}.{}.{}".format(_MAJOR, _MINOR, _PATCH)

_GIT_SCM = (make_git, "({}) Support the git scm tool.".format(_STRING))
