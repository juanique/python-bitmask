from setuptools import setup, find_packages

DESCRIPTION = "Simple bitmask wrapper library"

with open('README') as f:
    LONG_DESCRIPTION = f.read()

VERSION = '0.0.1'

setup(
    name = "python-bitmask",
    version = VERSION,
    description = DESCRIPTION,
    packages=find_packages(),
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    test_suite='test.py'
)