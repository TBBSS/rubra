#!/usr/bin/env python

from setuptools import setup
import sys
import os


# Helper functions
if sys.argv[-1] == 'publish':
    print "Please use twine or do_release.sh"
    sys.exit()

if sys.argv[-1] == 'clean':
    os.system('rm -rf Rubra.egg-info build dist')
    sys.exit()

if sys.argv[-1] == 'docs':
    os.system('cd docs && make html')
    sys.exit()

setup(
    name='Rubra',
    version='0.1.7',
    author='Bernie Pope',
    author_email='bjpope@unimelb.edu.au',
    packages=['rubra'],
    package_data={'rubra': ['examples/*.py']},
    entry_points={
        'console_scripts': ['rubra = rubra.rubra:main']
    },
    url='https://github.com/bjpop/rubra',
    license='LICENSE.txt',
    description=('Rubra is a pipeline system for bioinformatics workflows '
                 'with support for running pipeline stages on a distributed '
                 'compute cluster.'),
    long_description=open('README.txt').read(),
    install_requires=[
        "ruffus >= 2.0.0",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],

)
