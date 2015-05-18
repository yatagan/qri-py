#!/usr/bin/env python

from distutils.core import setup


setup(
    name='qri-py',
    version='1.0',
    description='Qri Python interface',
    author='va-dev',
    author_email='vadimanikin1@gmail.com',
    packages=['qri_py'],
    package_dir={'qri_py': 'src/qri_py'},
    install_requires=['msgpack-python']
)