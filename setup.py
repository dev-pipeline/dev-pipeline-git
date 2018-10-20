#!/usr/bin/python3

from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name="dev-pipeline-git",
    version="0.3.0",
    package_dir={
        "": "lib"
    },
    packages=find_packages("lib"),

    install_requires=[
        'dev-pipeline-core >= 0.3.0',
        'dev-pipeline-scm >= 0.3.0'
    ],

    entry_points={
        'devpipeline.scms': [
            'git = devpipeline_git:_GIT_SCM'
        ]
    },

    author="Stephen Newell",
    description="git plugin for dev-pipeline",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license="BSD-2",
    url="https://github.com/dev-pipeline/dev-pipeline-git",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: Utilities"
    ]
)
