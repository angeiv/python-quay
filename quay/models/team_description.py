# coding: utf-8

"""
    Quay Frontend

    This API allows you to perform many of the operations required to work with Quay repositories, users, and organizations. You can find out more at <a href=\"https://quay.io\">Quay</a>.  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@quay.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class TeamDescription(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'role': 'str',
        'description': 'str'
    }

    attribute_map = {
        'role': 'role',
        'description': 'description'
    }

    def __init__(self, role=None, description=None):  # noqa: E501
        """TeamDescription - a model defined in Swagger"""  # noqa: E501
        self._role = None
        self._description = None
        self.discriminator = None
        self.role = role
        if description is not None:
            self.description = description

    @property
    def role(self):
        """Gets the role of this TeamDescription.  # noqa: E501

        Org wide permissions that should apply to the team  # noqa: E501

        :return: The role of this TeamDescription.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this TeamDescription.

        Org wide permissions that should apply to the team  # noqa: E501

        :param role: The role of this TeamDescription.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["member", "creator", "admin"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def description(self):
        """Gets the description of this TeamDescription.  # noqa: E501

        Markdown description for the team  # noqa: E501

        :return: The description of this TeamDescription.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TeamDescription.

        Markdown description for the team  # noqa: E501

        :param description: The description of this TeamDescription.  # noqa: E501
        :type: str
        """

        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TeamDescription, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TeamDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
