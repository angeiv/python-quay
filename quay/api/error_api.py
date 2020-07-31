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


class ErrorApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_error_description(self, error_type, **kwargs):  # noqa: E501
        """get_error_description  # noqa: E501

        Get a detailed description of the error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_error_description(error_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str error_type: The error code identifying the type of error. (required)
        :return: ApiErrorDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_error_description_with_http_info(error_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_error_description_with_http_info(error_type, **kwargs)  # noqa: E501
            return data

    def get_error_description_with_http_info(self, error_type, **kwargs):  # noqa: E501
        """get_error_description  # noqa: E501

        Get a detailed description of the error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_error_description_with_http_info(error_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str error_type: The error code identifying the type of error. (required)
        :return: ApiErrorDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['error_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_error_description" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'error_type' is set
        if ('error_type' not in params or
                params['error_type'] is None):
            raise ValueError("Missing the required parameter `error_type` when calling `get_error_description`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'error_type' in params:
            path_params['error_type'] = params['error_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/error/{error_type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiErrorDescription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
