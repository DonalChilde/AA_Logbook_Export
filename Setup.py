#!/usr/bin/env python
# -*- coding: utf-8 -*-

# From: https://github.com/kennethreitz/setup.py/blob/master/setup.py

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'aaLogbookExport'
DESCRIPTION = 'A command line program to convert an AA logbook from xml to csv or json.'
URL = 'https://github.com/DonalChilde/AA_Logbook_Export'
EMAIL = 'pfmsoft@gmail.com'
AUTHOR = 'Chad'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '0.1.0'

# What packages are required for this module to be executed?
REQUIRED = [
    'dataclasses-json','arrow','pytz','python-dateutil','click'
]

# What packages are optional?
# EXTRAS = {
#     # 'fancy feature': ['django'],
# }

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
# if not VERSION:
#     with open(os.path.join(here, NAME, '__version__.py')) as f:
#         exec(f.read(), about)
# else:
#     about['__version__'] = VERSION
about['__version__'] = VERSION


# class UploadCommand(Command):
#     """Support setup.py upload."""

#     description = 'Build and publish the package.'
#     user_options = []

#     @staticmethod
#     def status(s):
#         """Prints things in bold."""
#         print('\033[1m{0}\033[0m'.format(s))

#     def initialize_options(self):
#         pass

#     def finalize_options(self):
#         pass

#     def run(self):
#         try:
#             self.status('Removing previous builds…')
#             rmtree(os.path.join(here, 'dist'))
#         except OSError:
#             pass

#         self.status('Building Source and Wheel (universal) distribution…')
#         os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

#         self.status('Uploading the package to PyPI via Twine…')
#         os.system('twine upload dist/*')

#         self.status('Pushing git tags…')
#         os.system('git tag v{0}'.format(about['__version__']))
#         os.system('git push --tags')
        
#         sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    package_dir={'':'src'},
    packages=find_packages(where='src',exclude=['tests',]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    entry_points={
        'console_scripts': ['aaLogbookExport=aaLogbook.aaLogbookExport:main'],
    },
    install_requires=REQUIRED,
    # extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # # $ setup.py publish support.
    # cmdclass={
    #     'upload': UploadCommand,
    # },
)