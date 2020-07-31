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


class CreateServiceKey(object):
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
        'notes': 'str',
        'expiration': 'object',
        'name': 'str',
        'service': 'str',
        'metadata': 'object'
    }

    attribute_map = {
        'notes': 'notes',
        'expiration': 'expiration',
        'name': 'name',
        'service': 'service',
        'metadata': 'metadata'
    }

    def __init__(self, notes=None, expiration=None, name=None, service=None, metadata=None):  # noqa: E501
        """CreateServiceKey - a model defined in Swagger"""  # noqa: E501
        self._notes = None
        self._expiration = None
        self._name = None
        self._service = None
        self._metadata = None
        self.discriminator = None
        if notes is not None:
            self.notes = notes
        self.expiration = expiration
        if name is not None:
            self.name = name
        self.service = service
        if metadata is not None:
            self.metadata = metadata

    @property
    def notes(self):
        """Gets the notes of this CreateServiceKey.  # noqa: E501

        If specified, the extra notes for the key  # noqa: E501

        :return: The notes of this CreateServiceKey.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CreateServiceKey.

        If specified, the extra notes for the key  # noqa: E501

        :param notes: The notes of this CreateServiceKey.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def expiration(self):
        """Gets the expiration of this CreateServiceKey.  # noqa: E501

        The expiration date as a unix timestamp  # noqa: E501

        :return: The expiration of this CreateServiceKey.  # noqa: E501
        :rtype: object
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this CreateServiceKey.

        The expiration date as a unix timestamp  # noqa: E501

        :param expiration: The expiration of this CreateServiceKey.  # noqa: E501
        :type: object
        """
        if expiration is None:
            raise ValueError("Invalid value for `expiration`, must not be `None`")  # noqa: E501

        self._expiration = expiration

    @property
    def name(self):
        """Gets the name of this CreateServiceKey.  # noqa: E501

        The friendly name of a service key  # noqa: E501

        :return: The name of this CreateServiceKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateServiceKey.

        The friendly name of a service key  # noqa: E501

        :param name: The name of this CreateServiceKey.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def service(self):
        """Gets the service of this CreateServiceKey.  # noqa: E501

        The service authenticating with this key  # noqa: E501

        :return: The service of this CreateServiceKey.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this CreateServiceKey.

        The service authenticating with this key  # noqa: E501

        :param service: The service of this CreateServiceKey.  # noqa: E501
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def metadata(self):
        """Gets the metadata of this CreateServiceKey.  # noqa: E501

        The key/value pairs of this key's metadata  # noqa: E501

        :return: The metadata of this CreateServiceKey.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateServiceKey.

        The key/value pairs of this key's metadata  # noqa: E501

        :param metadata: The metadata of this CreateServiceKey.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

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
        if issubclass(CreateServiceKey, dict):
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
        if not isinstance(other, CreateServiceKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other