#!/usr/bin/env python

PROJECT = 'scrabble-solver'

VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.md', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Scrabble Solver with CLI',
    long_description=long_description,

    author='Clark Perkins',
    author_email='r.clark.perkins@gmail.com',

    url='https://github.com/clarkperkins/Scrabble-Solver',
    download_url='https://github.com/clarkperkins/Scrabble-Solver/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Intended Audience :: Anyone',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'scrabble = scrabble.cli.main:main'
        ],
        'scrabble.cli': [
            'solve = scrabble.cli.solve:Solve',
            'match = scrabble.cli.match:Match',
            'solve-match = scrabble.cli.match:SolveMatch',
        ],
    },

    data_files=[
        ('dictionaries', ['dictionaries/ospd.dict'])
    ],

    zip_safe=False,
)
