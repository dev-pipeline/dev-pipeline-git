#!/usr/bin/python3

"""This modules implement support for Git SCM tools."""

import io
import os.path
import re
import subprocess

import devpipeline_core.toolsupport
import devpipeline_scm


def _merge_command(match, repo_dir):
    branch_pattern = re.compile(r"^{} ([\w/]+)".format(match.group(1)))

    def _check_line(line):
        # We're going to take a line from the git for-each-ref command and
        # look for the normalized name.  If we get a match, we'll try a
        # fast-forward merge.
        matches = branch_pattern.match(line)
        if matches:
            return [
                {
                    "args": ["git", "merge", "--ff-only", matches.group(1)],
                    "cwd": repo_dir,
                }
            ]
        return None

    # This will give output similar to this:
    #   master origin/master
    #   feature-branch some-remote/remote-branch-name
    #
    # We're going to use this output to figure out the *proper* upstream
    # branch for a fastforward merge.  This protects against somebody using
    # dev-pipeline to get started on a project, then switching the branch to
    # track their fork of an upstream project.
    with subprocess.Popen(
        [
            "git",
            "for-each-ref",
            "--format=%(refname:short) %(upstream:short)",
            "refs/heads",
        ],
        cwd=repo_dir,
        stdout=subprocess.PIPE,
    ) as proc:
        for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
            result = _check_line(line)
            if result:
                return result
    return []


def _ff_command(revision, repo_dir):
    if os.path.isdir(repo_dir):
        # If the revision is something weird like master~~^4~14, we want to get
        # the actual branch so it can be updated.
        match = re.match(r"([\w\-\.]+)(?:[~^\d]+)?", revision)
        if match:
            return _merge_command(match, repo_dir)
    return []


def _make_clone_command(uri, clone_dir, bare=False):
    clone = ["git", "clone"]
    args = [uri, clone_dir]
    bare_args = []

    if bare:
        bare_args = ["--bare"]

    return [{"args": clone + args + bare_args}]


def _make_fetch_command(repo_dir):
    return [{"args": ["git", "fetch"], "cwd": repo_dir}]


class Git:

    """This class is the core class to handle Git SCM operations."""

    def __init__(self, args):
        self._args = args

    def checkout(self, repo_dir, shared_dir):
        """This function checks out code from a Git SCM server."""
        args = []
        if shared_dir:
            if not os.path.isdir(shared_dir):
                # initial clone for the shared directory
                args.extend(_make_clone_command(self._args["uri"], shared_dir, True))
            elif not os.path.isdir(repo_dir):
                # if this is a new version being checked out,
                # fetch the latest code
                args.extend(_make_fetch_command(shared_dir))
        if not os.path.isdir(repo_dir):
            if shared_dir:
                # used the shared folder if we can
                args.extend(_make_clone_command(shared_dir, repo_dir))
            else:
                args.extend(_make_clone_command(self._args["uri"], repo_dir))
        return args

    def update(self, repo_dir):
        """This function updates an existing checkout of source code."""
        rev = self._args.get("revision")
        if rev:
            return [{"args": ["git", "checkout", rev], "cwd": repo_dir}] + _ff_command(
                rev, repo_dir
            )
        return None


_GIT_ARGS = {"uri": None, "revision": None}


_GIT_ARG_FNS = {"uri": lambda v: ("uri", v), "revision": lambda v: ("revision", v)}


def _make_git(current_target):
    """This function initializes and Git SCM tool object."""
    git_args = {}

    def _add_value(value, key):
        args_key, args_value = _GIT_ARG_FNS[key](value)
        git_args[args_key] = args_value

    devpipeline_core.toolsupport.args_builder(
        "git", current_target, _GIT_ARGS, _add_value
    )
    if git_args.get("uri"):
        return devpipeline_scm.make_simple_scm(Git(git_args), current_target)
    else:
        raise Exception("No git uri ({})".format(current_target["current_target"]))
