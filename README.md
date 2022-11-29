Wayback Machine News Archive Search
===================================

🚧 _under construction_ 🚧

A simple library to access the Wayback Machine news archive search.


Installation
------------

`pip install wayback-news-search`


Basic Usage
-----------

Counting matching stories:

```python
from waybacknews.searchapi import SearchApiClient
import datetime as dt

api = SearchApiClient("mediacloud")
api.count("coronavirus", dt.datetime(2022, 3, 1), dt.datetime(2022, 4, 1))
```

Paging over all matching results:

```python
from waybacknews.searchapi import SearchApiClient
import datetime as dt

api = SearchApiClient("mediacloud")
for page in api.all_articles("coronavirus", dt.datetime(2022, 3, 1), dt.datetime(2022, 4, 1)):
    do_something(page)
```


Dev Installation
----------------

Install the dependencies for dev: `pip install -e .[dev]`



Distribution
------------

1. Run `pytest` to make sure all the test pass
2. Update the version number in `waybacknews/__init__.py`
3. Make a brief note in the version history section below about the changes
4. Commit the changes
5. Tag the commit with a semantic version number - 'v*.*.*'
6. Push to repo to GitHub
7. Run `python setup.py sdist` to create an installation package
8. Run `twine upload --repository-url https://test.pypi.org/legacy/ dist/*` to upload it to PyPI's test platform
9. Run `twine upload dist/*` to upload it to PyPI


Version History
---------------

* __v1.0.0__ - update to public API endpoint
* __v0.1.5__ - simpler return for top terms
* __v0.1.4__ - better error handling
* __v0.1.3__ - allow overriding base api URL 
* __v0.1.2__ - fix `article` endpoint, test case for fetching content (`snippet`) via `article_url` property 
* __v0.1.1__ - more consistent method names
* __v0.1.0__ - initial test-only release
