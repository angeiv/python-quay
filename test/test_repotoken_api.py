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
from api.repotoken_api import RepotokenApi  # noqa: E501
from quay.rest import ApiException


class TestRepotokenApi(unittest.TestCase):
    """RepotokenApi unit test stubs"""

    def setUp(self):
        self.api = api.repotoken_api.RepotokenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_token(self):
        """Test case for change_token

        """
        pass

    def test_create_token(self):
        """Test case for create_token

        """
        pass

    def test_delete_token(self):
        """Test case for delete_token

        """
        pass

    def test_get_tokens(self):
        """Test case for get_tokens

        """
        pass

    def test_list_repo_tokens(self):
        """Test case for list_repo_tokens

        """
        pass


if __name__ == '__main__':
    unittest.main()