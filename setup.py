#!/usr/bin/env python
# encoding=UTF-8

from distribute_setup import use_setuptools
use_setuptools()

try:
    import multiprocessing
except ImportError:
    pass

from setuptools import setup

from dotenv import __version__


setup(name='dotenv',
      version=__version__,
      description='Handle .env files',
      author='Pedro Burón',
      author_email='pedro@witoi.com',
      url='http://witoi.github.com',
      test_suite='nose.collector',
      packages=['dotenv'],
      tests_require=['nose'],
      scripts=['scripts/dotenv']
     )
