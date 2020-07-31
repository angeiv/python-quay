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
from api.tag_api import TagApi  # noqa: E501
from quay.rest import ApiException


class TestTagApi(unittest.TestCase):
    """TagApi unit test stubs"""

    def setUp(self):
        self.api = api.tag_api.TagApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_tag(self):
        """Test case for change_tag

        """
        pass

    def test_delete_full_tag(self):
        """Test case for delete_full_tag

        """
        pass

    def test_list_repo_tags(self):
        """Test case for list_repo_tags

        """
        pass

    def test_list_tag_images(self):
        """Test case for list_tag_images

        """
        pass

    def test_restore_tag(self):
        """Test case for restore_tag

        """
        pass


if __name__ == '__main__':
    unittest.main()
