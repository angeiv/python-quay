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
from api.team_api import TeamApi  # noqa: E501
from quay.rest import ApiException


class TestTeamApi(unittest.TestCase):
    """TeamApi unit test stubs"""

    def setUp(self):
        self.api = api.team_api.TeamApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_organization_team(self):
        """Test case for delete_organization_team

        """
        pass

    def test_delete_organization_team_member(self):
        """Test case for delete_organization_team_member

        """
        pass

    def test_delete_team_member_email_invite(self):
        """Test case for delete_team_member_email_invite

        """
        pass

    def test_get_organization_team_members(self):
        """Test case for get_organization_team_members

        """
        pass

    def test_get_organization_team_permissions(self):
        """Test case for get_organization_team_permissions

        """
        pass

    def test_invite_team_member_email(self):
        """Test case for invite_team_member_email

        """
        pass

    def test_update_organization_team(self):
        """Test case for update_organization_team

        """
        pass

    def test_update_organization_team_member(self):
        """Test case for update_organization_team_member

        """
        pass


if __name__ == '__main__':
    unittest.main()