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


class UserView(object):
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
        'organizations': 'list[object]',
        'verified': 'bool',
        'avatar': 'object',
        'anonymous': 'bool',
        'logins': 'list[object]',
        'can_create_repo': 'bool',
        'preferred_namespace': 'bool',
        'email': 'str'
    }

    attribute_map = {
        'organizations': 'organizations',
        'verified': 'verified',
        'avatar': 'avatar',
        'anonymous': 'anonymous',
        'logins': 'logins',
        'can_create_repo': 'can_create_repo',
        'preferred_namespace': 'preferred_namespace',
        'email': 'email'
    }

    def __init__(self, organizations=None, verified=None, avatar=None, anonymous=None, logins=None, can_create_repo=None, preferred_namespace=None, email=None):  # noqa: E501
        """UserView - a model defined in Swagger"""  # noqa: E501
        self._organizations = None
        self._verified = None
        self._avatar = None
        self._anonymous = None
        self._logins = None
        self._can_create_repo = None
        self._preferred_namespace = None
        self._email = None
        self.discriminator = None
        if organizations is not None:
            self.organizations = organizations
        if verified is not None:
            self.verified = verified
        self.avatar = avatar
        self.anonymous = anonymous
        if logins is not None:
            self.logins = logins
        if can_create_repo is not None:
            self.can_create_repo = can_create_repo
        if preferred_namespace is not None:
            self.preferred_namespace = preferred_namespace
        if email is not None:
            self.email = email

    @property
    def organizations(self):
        """Gets the organizations of this UserView.  # noqa: E501

        Information about the organizations in which the user is a member  # noqa: E501

        :return: The organizations of this UserView.  # noqa: E501
        :rtype: list[object]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this UserView.

        Information about the organizations in which the user is a member  # noqa: E501

        :param organizations: The organizations of this UserView.  # noqa: E501
        :type: list[object]
        """

        self._organizations = organizations

    @property
    def verified(self):
        """Gets the verified of this UserView.  # noqa: E501

        Whether the user's email address has been verified  # noqa: E501

        :return: The verified of this UserView.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this UserView.

        Whether the user's email address has been verified  # noqa: E501

        :param verified: The verified of this UserView.  # noqa: E501
        :type: bool
        """

        self._verified = verified

    @property
    def avatar(self):
        """Gets the avatar of this UserView.  # noqa: E501

        Avatar data representing the user's icon  # noqa: E501

        :return: The avatar of this UserView.  # noqa: E501
        :rtype: object
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this UserView.

        Avatar data representing the user's icon  # noqa: E501

        :param avatar: The avatar of this UserView.  # noqa: E501
        :type: object
        """
        if avatar is None:
            raise ValueError("Invalid value for `avatar`, must not be `None`")  # noqa: E501

        self._avatar = avatar

    @property
    def anonymous(self):
        """Gets the anonymous of this UserView.  # noqa: E501

        true if this user data represents a guest user  # noqa: E501

        :return: The anonymous of this UserView.  # noqa: E501
        :rtype: bool
        """
        return self._anonymous

    @anonymous.setter
    def anonymous(self, anonymous):
        """Sets the anonymous of this UserView.

        true if this user data represents a guest user  # noqa: E501

        :param anonymous: The anonymous of this UserView.  # noqa: E501
        :type: bool
        """
        if anonymous is None:
            raise ValueError("Invalid value for `anonymous`, must not be `None`")  # noqa: E501

        self._anonymous = anonymous

    @property
    def logins(self):
        """Gets the logins of this UserView.  # noqa: E501

        The list of external login providers against which the user has authenticated  # noqa: E501

        :return: The logins of this UserView.  # noqa: E501
        :rtype: list[object]
        """
        return self._logins

    @logins.setter
    def logins(self, logins):
        """Sets the logins of this UserView.

        The list of external login providers against which the user has authenticated  # noqa: E501

        :param logins: The logins of this UserView.  # noqa: E501
        :type: list[object]
        """

        self._logins = logins

    @property
    def can_create_repo(self):
        """Gets the can_create_repo of this UserView.  # noqa: E501

        Whether the user has permission to create repositories  # noqa: E501

        :return: The can_create_repo of this UserView.  # noqa: E501
        :rtype: bool
        """
        return self._can_create_repo

    @can_create_repo.setter
    def can_create_repo(self, can_create_repo):
        """Sets the can_create_repo of this UserView.

        Whether the user has permission to create repositories  # noqa: E501

        :param can_create_repo: The can_create_repo of this UserView.  # noqa: E501
        :type: bool
        """

        self._can_create_repo = can_create_repo

    @property
    def preferred_namespace(self):
        """Gets the preferred_namespace of this UserView.  # noqa: E501

        If true, the user's namespace is the preferred namespace to display  # noqa: E501

        :return: The preferred_namespace of this UserView.  # noqa: E501
        :rtype: bool
        """
        return self._preferred_namespace

    @preferred_namespace.setter
    def preferred_namespace(self, preferred_namespace):
        """Sets the preferred_namespace of this UserView.

        If true, the user's namespace is the preferred namespace to display  # noqa: E501

        :param preferred_namespace: The preferred_namespace of this UserView.  # noqa: E501
        :type: bool
        """

        self._preferred_namespace = preferred_namespace

    @property
    def email(self):
        """Gets the email of this UserView.  # noqa: E501

        The user's email address  # noqa: E501

        :return: The email of this UserView.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserView.

        The user's email address  # noqa: E501

        :param email: The email of this UserView.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(UserView, dict):
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
        if not isinstance(other, UserView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
