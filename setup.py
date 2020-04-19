from setuptools import setup

setup(
    name = 'ex',
    version = '0.1',
    description = 'An example of an installable program',
    author = 'ghickman',
    url = '',
    license = 'MIT',
    packages = ['game'],
    entry_points = {'game': ['game = ex.py',],},
)
