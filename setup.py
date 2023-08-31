from setuptools import setup

setup(
    name="daily",
    version='0.1',
    py_modules=['daily.scan'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        daily=daily.scan:cli
    ''',
)
