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

with open(rel('./README.md')) as readme:
    long_description = readme.read()

setup(
    name='brain',
    version='0.0.0',
    description="Garbage project for mimicking neural networks through various learning processes.",
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
        "Programming Language :: Python :: 2.6",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)