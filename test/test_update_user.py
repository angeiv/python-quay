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
from models.update_user import UpdateUser  # noqa: E501
from quay.rest import ApiException


class TestUpdateUser(unittest.TestCase):
    """UpdateUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateUser(self):
        """Test UpdateUser"""
        # FIXME: construct object with mandatory attributes with example values
        # model = quay.models.update_user.UpdateUser()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()