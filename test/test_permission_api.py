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
from api.permission_api import PermissionApi  # noqa: E501
from quay.rest import ApiException


class TestPermissionApi(unittest.TestCase):
    """PermissionApi unit test stubs"""

    def setUp(self):
        self.api = api.permission_api.PermissionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_team_permissions(self):
        """Test case for change_team_permissions

        """
        pass

    def test_change_user_permissions(self):
        """Test case for change_user_permissions

        """
        pass

    def test_delete_team_permissions(self):
        """Test case for delete_team_permissions

        """
        pass

    def test_delete_user_permissions(self):
        """Test case for delete_user_permissions

        """
        pass

    def test_get_team_permissions(self):
        """Test case for get_team_permissions

        """
        pass

    def test_get_user_permissions(self):
        """Test case for get_user_permissions

        """
        pass

    def test_get_user_transitive_permission(self):
        """Test case for get_user_transitive_permission

        """
        pass

    def test_list_repo_team_permissions(self):
        """Test case for list_repo_team_permissions

        """
        pass

    def test_list_repo_user_permissions(self):
        """Test case for list_repo_user_permissions

        """
        pass


if __name__ == '__main__':
    unittest.main()
