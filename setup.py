#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2013, Evan Leis
#
# Distributed under the terms of the Apache Software License
#-----------------------------------------------------------------------------

import os

from setuptools import setup, find_packages


rel = lambda * x: os.path.abspath(os.path.join(os.path.dirname(__file__), *x))

short_description = "Garbage project for mimicking neural networks through various learning processes."

try:
    with open(rel('./README.md')) as readme:
        long_description = readme.read()
except IOError:
    long_description = short_description


setup(
    name='brain',
    version='0.0.0',
    description=short_description,
    long_description=long_description,
    author='Evan Leis',
    author_email='evan.explodes@gmail.com',
    url='https://github.com/explodes/brain',
    install_requires=[
    ],
    setup_requires=[
    ],
    packages=find_packages(exclude=[
    ]),
    include_package_data=True,
    package_data={},
    zip_safe=False,
    entry_points="""
    """,
    license="Apache Software License",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)