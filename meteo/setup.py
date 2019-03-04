# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='airquality_meteo',
    version='0.0.1',
    description='Airquality meteo parser',
    long_description=readme,
    author='François Roland',
    author_email='francois.roland@umons.ac.be',
    url='https://github.com/froland/lora-variability',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
