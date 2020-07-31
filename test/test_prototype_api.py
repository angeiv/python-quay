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
from api.prototype_api import PrototypeApi  # noqa: E501
from quay.rest import ApiException


class TestPrototypeApi(unittest.TestCase):
    """PrototypeApi unit test stubs"""

    def setUp(self):
        self.api = api.prototype_api.PrototypeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_organization_prototype_permission(self):
        """Test case for create_organization_prototype_permission

        """
        pass

    def test_delete_organization_prototype_permission(self):
        """Test case for delete_organization_prototype_permission

        """
        pass

    def test_get_organization_prototype_permissions(self):
        """Test case for get_organization_prototype_permissions

        """
        pass

    def test_update_organization_prototype_permission(self):
        """Test case for update_organization_prototype_permission

        """
        pass


if __name__ == '__main__':
    unittest.main()
