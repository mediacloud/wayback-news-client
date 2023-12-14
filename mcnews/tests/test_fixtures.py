from unittest import TestCase
import datetime as dt
import os
import pytest
import mcnews.searchapi as searchapi

INTEGRATION_TEST_COLLECTION = "mediacloud_test"
INTEGRATION_TEST_HOST = "http://127.0.0.1:8000"


class TestMediaCloudCollection(TestCase):

    def setUp(self) -> None:
        self._api = searchapi.SearchApiClient(INTEGRATION_TEST_COLLECTION)
        self._api.API_BASE_URL = f"{INTEGRATION_TEST_HOST}/{searchapi.VERSION}/"

    def test_count(self):
        results = self._api.count("*", dt.datetime(2023, 1, 1), dt.datetime(2024, 1, 1))
        assert results > 0
        assert results < 5000

    def test_count_over_time(self):
        results = self._api.count_over_time("*", dt.datetime(2020, 1, 1), dt.datetime(2025, 1, 1))
        assert len(results) > 30
        for day in results:
            assert 'date' in day
            assert 'count' in day
            assert 'timestamp' in day

    def test_count_no_results(self):
        results = self._api.count("*", dt.datetime(2010, 1, 1), dt.datetime(2010, 1, 1))
        assert results == 0

    def test_count_date_filter(self):
        all = self._api.count("*", dt.datetime(2023, 1, 1), dt.datetime(2024, 1, 1))
        assert all > 0
        w1 = self._api.count("*", dt.datetime(2023, 11, 1), dt.datetime(2024, 11, 8))
        assert all > w1

    def test_paged_articles(self):
        query = "*"
        start_date = dt.datetime(2023, 10, 1)
        end_date = dt.datetime(2023, 12, 31)
        story_count = self._api.count(query, start_date, end_date)
        # make sure test case is reasonable size (ie. more than one page, but not too many pages
        assert story_count > 1000
        assert story_count < 10000
        # fetch first page
        page1, next_token1 = self._api.paged_articles(query, start_date, end_date)
        assert len(page1) > 0
        assert next_token1 is not None
        page1_url1 = page1[0]['url']
        # grab token, fetch next page
        page2, next_token2 = self._api.paged_articles(query, start_date, end_date, pagination_token=next_token1)
        assert len(page2) > 0
        assert next_token2 is not None
        assert next_token1 != next_token2  # verify paging token changed
        page2_urls = [s['url'] for s in page2]
        assert page1_url1 not in page2_urls  # verify pages don't overlap

