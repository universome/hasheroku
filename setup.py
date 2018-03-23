#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='hasheroku',
    version='0.1.2',
    author='Ivan Skorokhodov',
    author_email='iskorokhodov@gmail.com',
    url='https://github.com/universome/hasheroku',
    description='Generates nice heroku-ish hash from the string',
    packages=find_packages(exclude=('test',)),
    license='BSD',
    python_requires='>=3',
    long_description=open('README.rst').read(),
    zip_safe=True
)
