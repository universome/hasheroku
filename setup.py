#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='hasheroku',
    version='0.1.1',
    author='Ivan Skorokhodov',
    author_email='iskorokhodov@gmail.com',
    url='https://github.com/universome/hasheroku',
    description='Generates nice heroku-ish hash from the string',
    packages=find_packages(exclude=('test',)),
    zip_safe=True
)
