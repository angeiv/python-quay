# coding: utf-8

"""
    Quay Frontend

    This API allows you to perform many of the operations required to work with Quay repositories, users, and organizations. You can find out more at <a href=\"https://quay.io\">Quay</a>.  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@quay.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from quay.api_client import ApiClient


class ManifestApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_manifest_label(self, body, manifestref, repository, **kwargs):  # noqa: E501
        """add_manifest_label  # noqa: E501

        Adds a new label into the tag manifest.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_manifest_label(body, manifestref, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddLabel body: Request body contents. (required)
        :param str manifestref: The digest of the manifest (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_manifest_label_with_http_info(body, manifestref, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.add_manifest_label_with_http_info(body, manifestref, repository, **kwargs)  # noqa: E501
            return data

    def add_manifest_label_with_http_info(self, body, manifestref, repository, **kwargs):  # noqa: E501
        """add_manifest_label  # noqa: E501

        Adds a new label into the tag manifest.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_manifest_label_with_http_info(body, manifestref, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddLabel body: Request body contents. (required)
        :param str manifestref: The digest of the manifest (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'manifestref', 'repository']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_manifest_label" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_manifest_label`")  # noqa: E501
        # verify the required parameter 'manifestref' is set
        if ('manifestref' not in params or
                params['manifestref'] is None):
            raise ValueError("Missing the required parameter `manifestref` when calling `add_manifest_label`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `add_manifest_label`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'manifestref' in params:
            path_params['manifestref'] = params['manifestref']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_implicit']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repository/{repository}/manifest/{manifestref}/labels', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_manifest_label(self, labelid, manifestref, repository, **kwargs):  # noqa: E501
        """delete_manifest_label  # noqa: E501

        Deletes an existing label from a manifest.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_manifest_label(labelid, manifestref, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str labelid: The ID of the label (required)
        :param str manifestref: The digest of the manifest (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_manifest_label_with_http_info(labelid, manifestref, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_manifest_label_with_http_info(labelid, manifestref, repository, **kwargs)  # noqa: E501
            return data

    def delete_manifest_label_with_http_info(self, labelid, manifestref, repository, **kwargs):  # noqa: E501
        """delete_manifest_label  # noqa: E501

        Deletes an existing label from a manifest.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_manifest_label_with_http_info(labelid, manifestref, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str labelid: The ID of the label (required)
        :param str manifestref: The digest of the manifest (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['labelid', 'manifestref', 'repository']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_manifest_label" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'labelid' is set
        if ('labelid' not in params or
                params['labelid'] is None):
            raise ValueError("Missing the required parameter `labelid` when calling `delete_manifest_label`")  # noqa: E501
        # verify the required parameter 'manifestref' is set
        if ('manifestref' not in params or
                params['manifestref'] is None):
            raise ValueError("Missing the required parameter `manifestref` when calling `delete_manifest_label`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `delete_manifest_label`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'labelid' in params:
            path_params['labelid'] = params['labelid']  # noqa: E501
        if 'manifestref' in params:
            path_params['manifestref'] = params['manifestref']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_implicit']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repository/{repository}/manifest/{manifestref}/labels/{labelid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_manifest_label(self, labelid, manifestref, repository, **kwargs):  # noqa: E501
        """get_manifest_label  # noqa: E501

        Retrieves the label with the specific ID under the manifest.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manifest_label(labelid, manifestref, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str labelid: The ID of the label (required)
        :param str manifestref: The digest of the manifest (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_manifest_label_with_http_info(labelid, manifestref, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.get_manifest_label_with_http_info(labelid, manifestref, repository, **kwargs)  # noqa: E501
            return data

    def get_manifest_label_with_http_info(self, labelid, manifestref, repository, **kwargs):  # noqa: E501
        """get_manifest_label  # noqa: E501

        Retrieves the label with the specific ID under the manifest.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manifest_label_with_http_info(labelid, manifestref, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str labelid: The ID of the label (required)
        :param str manifestref: The digest of the manifest (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['labelid', 'manifestref', 'repository']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manifest_label" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'labelid' is set
        if ('labelid' not in params or
                params['labelid'] is None):
            raise ValueError("Missing the required parameter `labelid` when calling `get_manifest_label`")  # noqa: E501
        # verify the required parameter 'manifestref' is set
        if ('manifestref' not in params or
                params['manifestref'] is None):
            raise ValueError("Missing the required parameter `manifestref` when calling `get_manifest_label`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `get_manifest_label`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'labelid' in params:
            path_params['labelid'] = params['labelid']  # noqa: E501
        if 'manifestref' in params:
            path_params['manifestref'] = params['manifestref']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_implicit']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repository/{repository}/manifest/{manifestref}/labels/{labelid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_repo_manifest(self, manifestref, repository, **kwargs):  # noqa: E501
        """get_repo_manifest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repo_manifest(manifestref, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str manifestref: The digest of the manifest (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_repo_manifest_with_http_info(manifestref, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.get_repo_manifest_with_http_info(manifestref, repository, **kwargs)  # noqa: E501
            return data

    def get_repo_manifest_with_http_info(self, manifestref, repository, **kwargs):  # noqa: E501
        """get_repo_manifest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repo_manifest_with_http_info(manifestref, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str manifestref: The digest of the manifest (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['manifestref', 'repository']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_repo_manifest" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'manifestref' is set
        if ('manifestref' not in params or
                params['manifestref'] is None):
            raise ValueError("Missing the required parameter `manifestref` when calling `get_repo_manifest`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `get_repo_manifest`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'manifestref' in params:
            path_params['manifestref'] = params['manifestref']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_implicit']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repository/{repository}/manifest/{manifestref}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_manifest_labels(self, manifestref, repository, **kwargs):  # noqa: E501
        """list_manifest_labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_manifest_labels(manifestref, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str manifestref: The digest of the manifest (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :param str filter: If specified, only labels matching the given prefix will be returned
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_manifest_labels_with_http_info(manifestref, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.list_manifest_labels_with_http_info(manifestref, repository, **kwargs)  # noqa: E501
            return data

    def list_manifest_labels_with_http_info(self, manifestref, repository, **kwargs):  # noqa: E501
        """list_manifest_labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_manifest_labels_with_http_info(manifestref, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str manifestref: The digest of the manifest (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :param str filter: If specified, only labels matching the given prefix will be returned
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['manifestref', 'repository', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_manifest_labels" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'manifestref' is set
        if ('manifestref' not in params or
                params['manifestref'] is None):
            raise ValueError("Missing the required parameter `manifestref` when calling `list_manifest_labels`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `list_manifest_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'manifestref' in params:
            path_params['manifestref'] = params['manifestref']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_implicit']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repository/{repository}/manifest/{manifestref}/labels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
