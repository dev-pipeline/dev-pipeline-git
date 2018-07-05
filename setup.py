#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name="dev-pipeline-git",
    version="0.2.0",
    package_dir={
        "": "lib"
    },
    packages=find_packages("lib"),

    install_requires=[
        'dev-pipeline-core >= 0.2.0'
    ],

    entry_points={
        'devpipeline.scms': [
            'git = devpipeline_git:make_git',
        ]
    },

    author="Stephen Newell",
    description="git plugin for dev-pipeline",
    license="BSD-2",
    url="https://github.com/dev-pipeline/dev-pipeline-git",
)
