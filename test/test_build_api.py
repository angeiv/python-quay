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
from api.build_api import BuildApi  # noqa: E501
from quay.rest import ApiException


class TestBuildApi(unittest.TestCase):
    """BuildApi unit test stubs"""

    def setUp(self):
        self.api = api.build_api.BuildApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_repo_build(self):
        """Test case for cancel_repo_build

        """
        pass

    def test_get_repo_build(self):
        """Test case for get_repo_build

        """
        pass

    def test_get_repo_build_logs(self):
        """Test case for get_repo_build_logs

        """
        pass

    def test_get_repo_build_status(self):
        """Test case for get_repo_build_status

        """
        pass

    def test_get_repo_builds(self):
        """Test case for get_repo_builds

        """
        pass

    def test_request_repo_build(self):
        """Test case for request_repo_build

        """
        pass


if __name__ == '__main__':
    unittest.main()
