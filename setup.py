#!/usr/bin/env python
# encoding=UTF-8


from setuptools import setup

try: # fix nose error
    import multiprocessing
except ImportError:
    pass


setup(name='dotenv',
      version=__import__('dotenv').__version__,
      description='Handle .env files',
      author='Pedro Burón',
      author_email='pedro@witoi.com',
      url='https://github.com/pedroburon/dotenv',
      test_suite='nose.collector',
      packages=['dotenv'],
      tests_require=['nose'],
      setup_requires=['distribute'],
      scripts=['scripts/dotenv']
     )
