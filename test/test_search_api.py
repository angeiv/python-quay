# coding: utf-8

"""
    Quay Frontend

    This API allows you to perform many of the operations required to work with Quay repositories, users, and organizations. You can find out more at <a href=\"https://quay.io\">Quay</a>.  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@quay.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import quay
from api.search_api import SearchApi  # noqa: E501
from quay.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_conduct_repo_search(self):
        """Test case for conduct_repo_search

        """
        pass

    def test_conduct_search(self):
        """Test case for conduct_search

        """
        pass

    def test_get_matching_entities(self):
        """Test case for get_matching_entities

        """
        pass


if __name__ == '__main__':
    unittest.main()
