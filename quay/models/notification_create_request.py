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


class NotificationCreateRequest(object):
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
        'event_config': 'object',
        'title': 'str',
        'config': 'object',
        'event': 'str',
        'method': 'str'
    }

    attribute_map = {
        'event_config': 'eventConfig',
        'title': 'title',
        'config': 'config',
        'event': 'event',
        'method': 'method'
    }

    def __init__(self, event_config=None, title=None, config=None, event=None, method=None):  # noqa: E501
        """NotificationCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._event_config = None
        self._title = None
        self._config = None
        self._event = None
        self._method = None
        self.discriminator = None
        self.event_config = event_config
        if title is not None:
            self.title = title
        self.config = config
        self.event = event
        self.method = method

    @property
    def event_config(self):
        """Gets the event_config of this NotificationCreateRequest.  # noqa: E501

        JSON config information for the specific event of notification  # noqa: E501

        :return: The event_config of this NotificationCreateRequest.  # noqa: E501
        :rtype: object
        """
        return self._event_config

    @event_config.setter
    def event_config(self, event_config):
        """Sets the event_config of this NotificationCreateRequest.

        JSON config information for the specific event of notification  # noqa: E501

        :param event_config: The event_config of this NotificationCreateRequest.  # noqa: E501
        :type: object
        """
        if event_config is None:
            raise ValueError("Invalid value for `event_config`, must not be `None`")  # noqa: E501

        self._event_config = event_config

    @property
    def title(self):
        """Gets the title of this NotificationCreateRequest.  # noqa: E501

        The human-readable title of the notification  # noqa: E501

        :return: The title of this NotificationCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NotificationCreateRequest.

        The human-readable title of the notification  # noqa: E501

        :param title: The title of this NotificationCreateRequest.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def config(self):
        """Gets the config of this NotificationCreateRequest.  # noqa: E501

        JSON config information for the specific method of notification  # noqa: E501

        :return: The config of this NotificationCreateRequest.  # noqa: E501
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this NotificationCreateRequest.

        JSON config information for the specific method of notification  # noqa: E501

        :param config: The config of this NotificationCreateRequest.  # noqa: E501
        :type: object
        """
        if config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def event(self):
        """Gets the event of this NotificationCreateRequest.  # noqa: E501

        The event on which the notification will respond  # noqa: E501

        :return: The event of this NotificationCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this NotificationCreateRequest.

        The event on which the notification will respond  # noqa: E501

        :param event: The event of this NotificationCreateRequest.  # noqa: E501
        :type: str
        """
        if event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def method(self):
        """Gets the method of this NotificationCreateRequest.  # noqa: E501

        The method of notification (such as email or web callback)  # noqa: E501

        :return: The method of this NotificationCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this NotificationCreateRequest.

        The method of notification (such as email or web callback)  # noqa: E501

        :param method: The method of this NotificationCreateRequest.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

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
        if issubclass(NotificationCreateRequest, dict):
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
        if not isinstance(other, NotificationCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
