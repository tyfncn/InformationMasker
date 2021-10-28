# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='information_masker',
    version='0.1.0',
    description='masks info from cvs file for development purposes',
    long_description=readme,
    author='Tayfun Can Güven',
    author_email='tayfuncanguven@gmail.com',
    url='https://github.com/tyfncn/InformationMasker',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
