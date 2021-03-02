#!/usr/bin/env python

from setuptools import setup, find_packages

with open("requirements.txt", "r") as reqs_file:
    requirements = reqs_file.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='tosca-metrics',
      version='0.0.8',
      description='A module to extract metrics rom TOSCA blueprints',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Stefano Dalla Palma',
      maintainer='Stefano Dalla Palma',
      author_email='stefano.dallapalma0@gmail.com',
      packages=find_packages(exclude=('test',)),
      entry_points = {
        'console_scripts': ['tosca-metrics=toscametrics.command_line:cli'],
      },
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "License :: OSI Approved :: Apache Software License",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Operating System :: OS Independent"
      ],
      insall_requires=requirements)

