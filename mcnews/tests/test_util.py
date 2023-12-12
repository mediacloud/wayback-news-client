from unittest import TestCase

import mcnews.util as util


class TestUtil(TestCase):

    def test_sanitize_query(self):
        query = "url:*dailyvoice.com/new-york/mountpleasant*"
        sanitized = util.sanitize_query(query)
        assert sanitized == "url:*dailyvoice.com\/new-york\/mountpleasant*"

    def test_dict_to_list(self):
        api_like_data = { 'key1': 'value1', 'key2':'value2' }
        list_version = util.dict_to_list(api_like_data)
        assert len(list_version) == 2
        assert list_version[0]['name'] == 'key1'
        assert list_version[0]['value'] == 'value1'
        assert list_version[1]['name'] == 'key2'
        assert list_version[1]['value'] == 'value2'
