#!/usr/bin/env python
import os
from setuptools import Command
from distutils.core import setup


def get_files(root):
    for dirname, dirnames, filenames in os.walk(root):
        for filename in filenames:
            yield os.path.join(dirname, filename)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


MODULE2PREFIX = {
    'beacon_manager': 'me',
}

MODULE = "registry"
PREFIX = "beacon"


setup(
    name='%s-%s' % (PREFIX, MODULE),
    # version='2.5',
    packages=['beacons'],
    url='https://www.github.com/rajatguptarg/beacons',
    license='MIT',
    author='Rajat Gupta',
    author_email='rajat.gupta712@gmail.com',
    description='Beacon Manager',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
        'Topic :: Office/Business',
    ],
    test_suite='tests'
)
