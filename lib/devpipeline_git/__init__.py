#!/usr/bin/python3

import devpipeline_git.git


def make_git(current_target, common_wrapper):
    return devpipeline_git.git._make_git(current_target, common_wrapper)

_GIT_SCM = (make_git, "Support the git scm tool.")
