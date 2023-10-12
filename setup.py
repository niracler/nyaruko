from setuptools import setup

setup(
    name="nyaruko",
    version='0.1',
    py_modules=['nyaruko.main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ny=nyaruko.main:cli
    ''',
)
