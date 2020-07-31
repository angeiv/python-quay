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


class NewApp(object):
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
        'redirect_uri': 'str',
        'avatar_email': 'str',
        'name': 'str',
        'application_uri': 'str',
        'description': 'str'
    }

    attribute_map = {
        'redirect_uri': 'redirect_uri',
        'avatar_email': 'avatar_email',
        'name': 'name',
        'application_uri': 'application_uri',
        'description': 'description'
    }

    def __init__(self, redirect_uri=None, avatar_email=None, name=None, application_uri=None, description=None):  # noqa: E501
        """NewApp - a model defined in Swagger"""  # noqa: E501
        self._redirect_uri = None
        self._avatar_email = None
        self._name = None
        self._application_uri = None
        self._description = None
        self.discriminator = None
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri
        if avatar_email is not None:
            self.avatar_email = avatar_email
        self.name = name
        if application_uri is not None:
            self.application_uri = application_uri
        if description is not None:
            self.description = description

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this NewApp.  # noqa: E501

        The URI for the application's OAuth redirect  # noqa: E501

        :return: The redirect_uri of this NewApp.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this NewApp.

        The URI for the application's OAuth redirect  # noqa: E501

        :param redirect_uri: The redirect_uri of this NewApp.  # noqa: E501
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def avatar_email(self):
        """Gets the avatar_email of this NewApp.  # noqa: E501

        The e-mail address of the avatar to use for the application  # noqa: E501

        :return: The avatar_email of this NewApp.  # noqa: E501
        :rtype: str
        """
        return self._avatar_email

    @avatar_email.setter
    def avatar_email(self, avatar_email):
        """Sets the avatar_email of this NewApp.

        The e-mail address of the avatar to use for the application  # noqa: E501

        :param avatar_email: The avatar_email of this NewApp.  # noqa: E501
        :type: str
        """

        self._avatar_email = avatar_email

    @property
    def name(self):
        """Gets the name of this NewApp.  # noqa: E501

        The name of the application  # noqa: E501

        :return: The name of this NewApp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewApp.

        The name of the application  # noqa: E501

        :param name: The name of this NewApp.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def application_uri(self):
        """Gets the application_uri of this NewApp.  # noqa: E501

        The URI for the application's homepage  # noqa: E501

        :return: The application_uri of this NewApp.  # noqa: E501
        :rtype: str
        """
        return self._application_uri

    @application_uri.setter
    def application_uri(self, application_uri):
        """Sets the application_uri of this NewApp.

        The URI for the application's homepage  # noqa: E501

        :param application_uri: The application_uri of this NewApp.  # noqa: E501
        :type: str
        """

        self._application_uri = application_uri

    @property
    def description(self):
        """Gets the description of this NewApp.  # noqa: E501

        The human-readable description for the application  # noqa: E501

        :return: The description of this NewApp.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NewApp.

        The human-readable description for the application  # noqa: E501

        :param description: The description of this NewApp.  # noqa: E501
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
        if issubclass(NewApp, dict):
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
        if not isinstance(other, NewApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
