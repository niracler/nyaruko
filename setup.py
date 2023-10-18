"""
Setup file for nyaruko
"""
from setuptools import find_packages, setup

setup(
    name="nyaruko",
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'python-telegram-bot[socks]'
    ],
    entry_points='''
        [console_scripts]
        ny=nyaruko.main:cli
    ''',
)
