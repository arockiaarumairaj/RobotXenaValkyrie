#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function
from setuptools import setup, find_packages
import io

import xenaValkyrie


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


with open('requirements.txt') as f:
    required = f.read().splitlines()
install_requires = [r for r in required if r and r[0] != '#' and not r.startswith('git')]

setup(
    name='RobotXenaValkyrie',
    version=RobotXenaValkyrie.__version__,
    url='https://github.com/xenadevel/PyRobotXenaValkyrie/',
    license='Apache Software License',
    author='arockia arumairaj',
    install_requires=install_requires,
    author_email='arockiaarumairaj@gmail.com',
    description='Python OO API package to automate Xena traffic generator',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    charset='UTF-8',
    variant='GFM',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    platforms='any',
    tests_require=['pytest','robotframework'],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing :: Traffic Generation',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'],
)
