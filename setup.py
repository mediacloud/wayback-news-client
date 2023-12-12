#! /usr/bin/env python
import re
import os
from setuptools import setup

REQUIRED_PACKAGES = [
    # utilities
    "requests==2.*",  # widely used HTTP library
    "ciso8601==2.2.*"  # super-fast date parsing
]

with open('mcnews/__init__.py', 'r', encoding='utf8') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

# add README.md to distribution
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), 'r', encoding='utf8') as f:
    long_description = f.read()

setup(name='mediacloud-news-search',
      maintainer='Rahul Bhargava',
      maintainer_email='r.bhargava@northeastern.edu',
      version=version,
      description='Mediacloud news archive search api client',
      long_description=long_description,
      long_description_content_type='text/markdown',
      test_suite="mcnews.test",
      packages=['mcnews'],
      package_data={'': ['LICENSE']},
      python_requires='>3.7',
      install_requires=REQUIRED_PACKAGES,
      extras_require={'dev': ['pytest', 'twine']},
      project_urls={
              'Bug Reports': 'https://github.com/mediacloud/mediacloud-news-search/issues',
              'Source': 'https://github.com/mediacloud/mediacloud-news-search',
          },
      )
