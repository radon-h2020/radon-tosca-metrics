#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='toscametrics',
      version='0.1',
      description='A module to measure metrics on TOSCA blueprints',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Stefano Dalla Palma',
      maintainer='Stefano Dalla Palma',
      author_email='stefano.dallapalma0@gmail.com',
      packages=find_packages(exclude=('test',)),
      entry_points = {
        'console_scripts': ['tosca-metrics=toscametrics.command_line:main'],
      },
      classifiers=[
         "Programming Language :: Python :: 3.6",
         "License :: Apache 2",
         "Operating System :: OS Independent"
     ]
)