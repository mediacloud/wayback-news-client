from unittest import TestCase
import datetime as dt

import waybacknews.searchapi as searchapi

INTEGRATION_TEST_COLLECTION = "mediacloud_test"
INTEGRATION_TEST_HOST = "http://127.0.0.1:8000"


class TestMediaCloudCollection(TestCase):

    def setUp(self) -> None:
        self._api = searchapi.SearchApiClient(INTEGRATION_TEST_COLLECTION)
        self._api.API_BASE_URL = f"{INTEGRATION_TEST_HOST}/{searchapi.VERSION}/"

    def test_count(self):
        results = self._api.count("*", dt.datetime(2020, 1, 1), dt.datetime(2025, 1, 1))
        assert results > 0
        assert results < 5000
