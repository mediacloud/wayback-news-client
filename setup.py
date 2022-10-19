#! /usr/bin/env python
from setuptools import setup
import re
import os

REQUIRED_PACKAGES = [
    # utilities
    "requests==2.*",  # widely used HTTP library
    "ciso8601==2.2.*"  # super-fast date parsing
]

with open('waybacknews/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

# add README.md to distribution
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(name='wayback-news-search',
      maintainer='Rahul Bhargava',
      maintainer_email='r.bhargava@northeastern.edu',
      version=version,
      description='Wayback Machine news archive search api client',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://web.archive.org',
      test_suite="waybacknews.test",
      packages=['waybacknews'],
      package_data={'': ['LICENSE']},
      python_requires='>3.7',
      install_requires=REQUIRED_PACKAGES,
      extras_require={'dev': ['pytest', 'twine']},
      project_urls={
              'Bug Reports': 'https://github.com/mediacloud/wayback-news-search/issues',
              'Source': 'https://github.com/mediacloud/wayback-news-search',
          },
      )
