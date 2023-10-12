"""
Setup file for nyaruko
"""
from setuptools import setup

setup(
    name="nyaruko",
    version='0.1',
    py_modules=['nyaruko.main'],
    package_data={
        'nyaruko': ['data/*.txt'],
    },
    install_requires=[
        'Click',
        'python-telegram-bot[socks]'
    ],
    entry_points='''
        [console_scripts]
        ny=nyaruko.main:cli
    ''',
)
