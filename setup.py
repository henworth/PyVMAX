#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='PyVMAX',
    version='0.8.2',
    description='EMC VMAX REST API client package',
    author='Scott Brightwell',
    author_email='scott@brightwell.org',
    url='https://github.com/scottbri/PyVMAX',
    include_package_data=True,
    packages=['pyvmax'],
)
