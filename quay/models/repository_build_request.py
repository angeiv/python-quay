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


class RepositoryBuildRequest(object):
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
        'subdirectory': 'str',
        'archive_url': 'str',
        'docker_tags': 'list[str]',
        'pull_robot': 'str',
        'file_id': 'str',
        'context': 'str',
        'dockerfile_path': 'str'
    }

    attribute_map = {
        'subdirectory': 'subdirectory',
        'archive_url': 'archive_url',
        'docker_tags': 'docker_tags',
        'pull_robot': 'pull_robot',
        'file_id': 'file_id',
        'context': 'context',
        'dockerfile_path': 'dockerfile_path'
    }

    def __init__(self, subdirectory=None, archive_url=None, docker_tags=None, pull_robot=None, file_id=None, context=None, dockerfile_path=None):  # noqa: E501
        """RepositoryBuildRequest - a model defined in Swagger"""  # noqa: E501
        self._subdirectory = None
        self._archive_url = None
        self._docker_tags = None
        self._pull_robot = None
        self._file_id = None
        self._context = None
        self._dockerfile_path = None
        self.discriminator = None
        if subdirectory is not None:
            self.subdirectory = subdirectory
        if archive_url is not None:
            self.archive_url = archive_url
        if docker_tags is not None:
            self.docker_tags = docker_tags
        if pull_robot is not None:
            self.pull_robot = pull_robot
        if file_id is not None:
            self.file_id = file_id
        if context is not None:
            self.context = context
        if dockerfile_path is not None:
            self.dockerfile_path = dockerfile_path

    @property
    def subdirectory(self):
        """Gets the subdirectory of this RepositoryBuildRequest.  # noqa: E501

        Subdirectory in which the Dockerfile can be found. You can only specify this or dockerfile_path  # noqa: E501

        :return: The subdirectory of this RepositoryBuildRequest.  # noqa: E501
        :rtype: str
        """
        return self._subdirectory

    @subdirectory.setter
    def subdirectory(self, subdirectory):
        """Sets the subdirectory of this RepositoryBuildRequest.

        Subdirectory in which the Dockerfile can be found. You can only specify this or dockerfile_path  # noqa: E501

        :param subdirectory: The subdirectory of this RepositoryBuildRequest.  # noqa: E501
        :type: str
        """

        self._subdirectory = subdirectory

    @property
    def archive_url(self):
        """Gets the archive_url of this RepositoryBuildRequest.  # noqa: E501

        The URL of the .tar.gz to build. Must start with \"http\" or \"https\".  # noqa: E501

        :return: The archive_url of this RepositoryBuildRequest.  # noqa: E501
        :rtype: str
        """
        return self._archive_url

    @archive_url.setter
    def archive_url(self, archive_url):
        """Sets the archive_url of this RepositoryBuildRequest.

        The URL of the .tar.gz to build. Must start with \"http\" or \"https\".  # noqa: E501

        :param archive_url: The archive_url of this RepositoryBuildRequest.  # noqa: E501
        :type: str
        """

        self._archive_url = archive_url

    @property
    def docker_tags(self):
        """Gets the docker_tags of this RepositoryBuildRequest.  # noqa: E501

        The tags to which the built images will be pushed. If none specified, \"latest\" is used.  # noqa: E501

        :return: The docker_tags of this RepositoryBuildRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._docker_tags

    @docker_tags.setter
    def docker_tags(self, docker_tags):
        """Sets the docker_tags of this RepositoryBuildRequest.

        The tags to which the built images will be pushed. If none specified, \"latest\" is used.  # noqa: E501

        :param docker_tags: The docker_tags of this RepositoryBuildRequest.  # noqa: E501
        :type: list[str]
        """

        self._docker_tags = docker_tags

    @property
    def pull_robot(self):
        """Gets the pull_robot of this RepositoryBuildRequest.  # noqa: E501

        Username of a Quay robot account to use as pull credentials  # noqa: E501

        :return: The pull_robot of this RepositoryBuildRequest.  # noqa: E501
        :rtype: str
        """
        return self._pull_robot

    @pull_robot.setter
    def pull_robot(self, pull_robot):
        """Sets the pull_robot of this RepositoryBuildRequest.

        Username of a Quay robot account to use as pull credentials  # noqa: E501

        :param pull_robot: The pull_robot of this RepositoryBuildRequest.  # noqa: E501
        :type: str
        """

        self._pull_robot = pull_robot

    @property
    def file_id(self):
        """Gets the file_id of this RepositoryBuildRequest.  # noqa: E501

        The file id that was generated when the build spec was uploaded  # noqa: E501

        :return: The file_id of this RepositoryBuildRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this RepositoryBuildRequest.

        The file id that was generated when the build spec was uploaded  # noqa: E501

        :param file_id: The file_id of this RepositoryBuildRequest.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def context(self):
        """Gets the context of this RepositoryBuildRequest.  # noqa: E501

        Pass in the context for the dockerfile. This is optional.  # noqa: E501

        :return: The context of this RepositoryBuildRequest.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this RepositoryBuildRequest.

        Pass in the context for the dockerfile. This is optional.  # noqa: E501

        :param context: The context of this RepositoryBuildRequest.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def dockerfile_path(self):
        """Gets the dockerfile_path of this RepositoryBuildRequest.  # noqa: E501

        Path to a dockerfile. You can only specify this or subdirectory.  # noqa: E501

        :return: The dockerfile_path of this RepositoryBuildRequest.  # noqa: E501
        :rtype: str
        """
        return self._dockerfile_path

    @dockerfile_path.setter
    def dockerfile_path(self, dockerfile_path):
        """Sets the dockerfile_path of this RepositoryBuildRequest.

        Path to a dockerfile. You can only specify this or subdirectory.  # noqa: E501

        :param dockerfile_path: The dockerfile_path of this RepositoryBuildRequest.  # noqa: E501
        :type: str
        """

        self._dockerfile_path = dockerfile_path

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
        if issubclass(RepositoryBuildRequest, dict):
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
        if not isinstance(other, RepositoryBuildRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
