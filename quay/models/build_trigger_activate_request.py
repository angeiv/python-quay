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


class BuildTriggerActivateRequest(object):
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
        'pull_robot': 'str',
        'config': 'object'
    }

    attribute_map = {
        'pull_robot': 'pull_robot',
        'config': 'config'
    }

    def __init__(self, pull_robot=None, config=None):  # noqa: E501
        """BuildTriggerActivateRequest - a model defined in Swagger"""  # noqa: E501
        self._pull_robot = None
        self._config = None
        self.discriminator = None
        if pull_robot is not None:
            self.pull_robot = pull_robot
        self.config = config

    @property
    def pull_robot(self):
        """Gets the pull_robot of this BuildTriggerActivateRequest.  # noqa: E501

        The name of the robot that will be used to pull images.  # noqa: E501

        :return: The pull_robot of this BuildTriggerActivateRequest.  # noqa: E501
        :rtype: str
        """
        return self._pull_robot

    @pull_robot.setter
    def pull_robot(self, pull_robot):
        """Sets the pull_robot of this BuildTriggerActivateRequest.

        The name of the robot that will be used to pull images.  # noqa: E501

        :param pull_robot: The pull_robot of this BuildTriggerActivateRequest.  # noqa: E501
        :type: str
        """

        self._pull_robot = pull_robot

    @property
    def config(self):
        """Gets the config of this BuildTriggerActivateRequest.  # noqa: E501

        Arbitrary json.  # noqa: E501

        :return: The config of this BuildTriggerActivateRequest.  # noqa: E501
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this BuildTriggerActivateRequest.

        Arbitrary json.  # noqa: E501

        :param config: The config of this BuildTriggerActivateRequest.  # noqa: E501
        :type: object
        """
        if config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

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
        if issubclass(BuildTriggerActivateRequest, dict):
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
        if not isinstance(other, BuildTriggerActivateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
