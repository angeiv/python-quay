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


class CreateMirrorConfig(object):
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
        'is_enabled': 'bool',
        'external_registry_config': 'UpdateMirrorConfigExternalRegistryConfig',
        'sync_start_date': 'str',
        'external_reference': 'str',
        'root_rule': 'UpdateMirrorConfigRootRule',
        'sync_interval': 'int',
        'robot_username': 'str'
    }

    attribute_map = {
        'is_enabled': 'is_enabled',
        'external_registry_config': 'external_registry_config',
        'sync_start_date': 'sync_start_date',
        'external_reference': 'external_reference',
        'root_rule': 'root_rule',
        'sync_interval': 'sync_interval',
        'robot_username': 'robot_username'
    }

    def __init__(self, is_enabled=None, external_registry_config=None, sync_start_date=None, external_reference=None, root_rule=None, sync_interval=None, robot_username=None):  # noqa: E501
        """CreateMirrorConfig - a model defined in Swagger"""  # noqa: E501
        self._is_enabled = None
        self._external_registry_config = None
        self._sync_start_date = None
        self._external_reference = None
        self._root_rule = None
        self._sync_interval = None
        self._robot_username = None
        self.discriminator = None
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if external_registry_config is not None:
            self.external_registry_config = external_registry_config
        self.sync_start_date = sync_start_date
        self.external_reference = external_reference
        self.root_rule = root_rule
        self.sync_interval = sync_interval
        if robot_username is not None:
            self.robot_username = robot_username

    @property
    def is_enabled(self):
        """Gets the is_enabled of this CreateMirrorConfig.  # noqa: E501

        Used to enable or disable synchronizations.  # noqa: E501

        :return: The is_enabled of this CreateMirrorConfig.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this CreateMirrorConfig.

        Used to enable or disable synchronizations.  # noqa: E501

        :param is_enabled: The is_enabled of this CreateMirrorConfig.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def external_registry_config(self):
        """Gets the external_registry_config of this CreateMirrorConfig.  # noqa: E501


        :return: The external_registry_config of this CreateMirrorConfig.  # noqa: E501
        :rtype: UpdateMirrorConfigExternalRegistryConfig
        """
        return self._external_registry_config

    @external_registry_config.setter
    def external_registry_config(self, external_registry_config):
        """Sets the external_registry_config of this CreateMirrorConfig.


        :param external_registry_config: The external_registry_config of this CreateMirrorConfig.  # noqa: E501
        :type: UpdateMirrorConfigExternalRegistryConfig
        """

        self._external_registry_config = external_registry_config

    @property
    def sync_start_date(self):
        """Gets the sync_start_date of this CreateMirrorConfig.  # noqa: E501

        Determines the next time this repository is ready for synchronization.  # noqa: E501

        :return: The sync_start_date of this CreateMirrorConfig.  # noqa: E501
        :rtype: str
        """
        return self._sync_start_date

    @sync_start_date.setter
    def sync_start_date(self, sync_start_date):
        """Sets the sync_start_date of this CreateMirrorConfig.

        Determines the next time this repository is ready for synchronization.  # noqa: E501

        :param sync_start_date: The sync_start_date of this CreateMirrorConfig.  # noqa: E501
        :type: str
        """
        if sync_start_date is None:
            raise ValueError("Invalid value for `sync_start_date`, must not be `None`")  # noqa: E501

        self._sync_start_date = sync_start_date

    @property
    def external_reference(self):
        """Gets the external_reference of this CreateMirrorConfig.  # noqa: E501

        Location of the external repository.  # noqa: E501

        :return: The external_reference of this CreateMirrorConfig.  # noqa: E501
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this CreateMirrorConfig.

        Location of the external repository.  # noqa: E501

        :param external_reference: The external_reference of this CreateMirrorConfig.  # noqa: E501
        :type: str
        """
        if external_reference is None:
            raise ValueError("Invalid value for `external_reference`, must not be `None`")  # noqa: E501

        self._external_reference = external_reference

    @property
    def root_rule(self):
        """Gets the root_rule of this CreateMirrorConfig.  # noqa: E501


        :return: The root_rule of this CreateMirrorConfig.  # noqa: E501
        :rtype: UpdateMirrorConfigRootRule
        """
        return self._root_rule

    @root_rule.setter
    def root_rule(self, root_rule):
        """Sets the root_rule of this CreateMirrorConfig.


        :param root_rule: The root_rule of this CreateMirrorConfig.  # noqa: E501
        :type: UpdateMirrorConfigRootRule
        """
        if root_rule is None:
            raise ValueError("Invalid value for `root_rule`, must not be `None`")  # noqa: E501

        self._root_rule = root_rule

    @property
    def sync_interval(self):
        """Gets the sync_interval of this CreateMirrorConfig.  # noqa: E501

        Number of seconds after next_start_date to begin synchronizing.  # noqa: E501

        :return: The sync_interval of this CreateMirrorConfig.  # noqa: E501
        :rtype: int
        """
        return self._sync_interval

    @sync_interval.setter
    def sync_interval(self, sync_interval):
        """Sets the sync_interval of this CreateMirrorConfig.

        Number of seconds after next_start_date to begin synchronizing.  # noqa: E501

        :param sync_interval: The sync_interval of this CreateMirrorConfig.  # noqa: E501
        :type: int
        """
        if sync_interval is None:
            raise ValueError("Invalid value for `sync_interval`, must not be `None`")  # noqa: E501

        self._sync_interval = sync_interval

    @property
    def robot_username(self):
        """Gets the robot_username of this CreateMirrorConfig.  # noqa: E501

        Username of robot which will be used for image pushes.  # noqa: E501

        :return: The robot_username of this CreateMirrorConfig.  # noqa: E501
        :rtype: str
        """
        return self._robot_username

    @robot_username.setter
    def robot_username(self, robot_username):
        """Sets the robot_username of this CreateMirrorConfig.

        Username of robot which will be used for image pushes.  # noqa: E501

        :param robot_username: The robot_username of this CreateMirrorConfig.  # noqa: E501
        :type: str
        """

        self._robot_username = robot_username

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
        if issubclass(CreateMirrorConfig, dict):
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
        if not isinstance(other, CreateMirrorConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other