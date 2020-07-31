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


class NewPrototypeDelegate(object):
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
        'kind': 'str',
        'name': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'name': 'name'
    }

    def __init__(self, kind=None, name=None):  # noqa: E501
        """NewPrototypeDelegate - a model defined in Swagger"""  # noqa: E501
        self._kind = None
        self._name = None
        self.discriminator = None
        self.kind = kind
        self.name = name

    @property
    def kind(self):
        """Gets the kind of this NewPrototypeDelegate.  # noqa: E501

        Whether the delegate is a user or a team  # noqa: E501

        :return: The kind of this NewPrototypeDelegate.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this NewPrototypeDelegate.

        Whether the delegate is a user or a team  # noqa: E501

        :param kind: The kind of this NewPrototypeDelegate.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["user", "team"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this NewPrototypeDelegate.  # noqa: E501

        The name for the delegate team or user  # noqa: E501

        :return: The name of this NewPrototypeDelegate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewPrototypeDelegate.

        The name for the delegate team or user  # noqa: E501

        :param name: The name of this NewPrototypeDelegate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(NewPrototypeDelegate, dict):
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
        if not isinstance(other, NewPrototypeDelegate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
