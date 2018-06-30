#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name="dev-pipeline-git",
    version="0.2.0",
    package_dir={
        "": "lib"
    },
    packages=['devpipeline_plugins.git'],

    author="Stephen Newell",
    description="git plugin for dev-pipeline",
    license="BSD-2",
    url="https://github.com/dev-pipeline/dev-pipeline-git",
)
