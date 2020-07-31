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


class UpdateMirrorConfigRootRule(object):
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
        'rule_kind': 'str',
        'rule_value': 'list[str]'
    }

    attribute_map = {
        'rule_kind': 'rule_kind',
        'rule_value': 'rule_value'
    }

    def __init__(self, rule_kind=None, rule_value=None):  # noqa: E501
        """UpdateMirrorConfigRootRule - a model defined in Swagger"""  # noqa: E501
        self._rule_kind = None
        self._rule_value = None
        self.discriminator = None
        self.rule_kind = rule_kind
        self.rule_value = rule_value

    @property
    def rule_kind(self):
        """Gets the rule_kind of this UpdateMirrorConfigRootRule.  # noqa: E501

        The kind of rule type  # noqa: E501

        :return: The rule_kind of this UpdateMirrorConfigRootRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_kind

    @rule_kind.setter
    def rule_kind(self, rule_kind):
        """Sets the rule_kind of this UpdateMirrorConfigRootRule.

        The kind of rule type  # noqa: E501

        :param rule_kind: The rule_kind of this UpdateMirrorConfigRootRule.  # noqa: E501
        :type: str
        """
        if rule_kind is None:
            raise ValueError("Invalid value for `rule_kind`, must not be `None`")  # noqa: E501
        allowed_values = ["tag_glob_csv"]  # noqa: E501
        if rule_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `rule_kind` ({0}), must be one of {1}"  # noqa: E501
                .format(rule_kind, allowed_values)
            )

        self._rule_kind = rule_kind

    @property
    def rule_value(self):
        """Gets the rule_value of this UpdateMirrorConfigRootRule.  # noqa: E501

        Array of tag patterns  # noqa: E501

        :return: The rule_value of this UpdateMirrorConfigRootRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._rule_value

    @rule_value.setter
    def rule_value(self, rule_value):
        """Sets the rule_value of this UpdateMirrorConfigRootRule.

        Array of tag patterns  # noqa: E501

        :param rule_value: The rule_value of this UpdateMirrorConfigRootRule.  # noqa: E501
        :type: list[str]
        """
        if rule_value is None:
            raise ValueError("Invalid value for `rule_value`, must not be `None`")  # noqa: E501

        self._rule_value = rule_value

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
        if issubclass(UpdateMirrorConfigRootRule, dict):
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
        if not isinstance(other, UpdateMirrorConfigRootRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
