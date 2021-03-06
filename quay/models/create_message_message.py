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


class CreateMessageMessage(object):
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
        'content': 'str',
        'media_type': 'str',
        'severity': 'str'
    }

    attribute_map = {
        'content': 'content',
        'media_type': 'media_type',
        'severity': 'severity'
    }

    def __init__(self, content=None, media_type=None, severity=None):  # noqa: E501
        """CreateMessageMessage - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._media_type = None
        self._severity = None
        self.discriminator = None
        self.content = content
        self.media_type = media_type
        self.severity = severity

    @property
    def content(self):
        """Gets the content of this CreateMessageMessage.  # noqa: E501

        The actual message  # noqa: E501

        :return: The content of this CreateMessageMessage.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreateMessageMessage.

        The actual message  # noqa: E501

        :param content: The content of this CreateMessageMessage.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def media_type(self):
        """Gets the media_type of this CreateMessageMessage.  # noqa: E501

        The media type of the message  # noqa: E501

        :return: The media_type of this CreateMessageMessage.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this CreateMessageMessage.

        The media type of the message  # noqa: E501

        :param media_type: The media_type of this CreateMessageMessage.  # noqa: E501
        :type: str
        """
        if media_type is None:
            raise ValueError("Invalid value for `media_type`, must not be `None`")  # noqa: E501
        allowed_values = ["text/plain", "text/markdown"]  # noqa: E501
        if media_type not in allowed_values:
            raise ValueError(
                "Invalid value for `media_type` ({0}), must be one of {1}"  # noqa: E501
                .format(media_type, allowed_values)
            )

        self._media_type = media_type

    @property
    def severity(self):
        """Gets the severity of this CreateMessageMessage.  # noqa: E501

        The severity of the message  # noqa: E501

        :return: The severity of this CreateMessageMessage.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this CreateMessageMessage.

        The severity of the message  # noqa: E501

        :param severity: The severity of this CreateMessageMessage.  # noqa: E501
        :type: str
        """
        if severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501
        allowed_values = ["info", "warning", "error"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

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
        if issubclass(CreateMessageMessage, dict):
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
        if not isinstance(other, CreateMessageMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
