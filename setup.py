#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='gnrelib',
    version='0.1',
    author='Luis Felipe Mileo',
    author_email='mileo@kmee.com.br',
    url='https://github.com/kmee/gnrelib',
    description='gnrelib: TODO',
    long_description=open('README.rst').read(),
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        "Operating System :: OS Independent",
    ],
    keywords='MDF-e ERP Python',
    packages=find_packages(),
    include_package_data=True,
    scripts=[],
    zip_safe=False,
)
