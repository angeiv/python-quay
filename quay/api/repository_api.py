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


class RepositoryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def change_repo_state(self, body, repository, **kwargs):  # noqa: E501
        """change_repo_state  # noqa: E501

        Change the state of a repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_repo_state(body, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChangeRepoState body: Request body contents. (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_repo_state_with_http_info(body, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.change_repo_state_with_http_info(body, repository, **kwargs)  # noqa: E501
            return data

    def change_repo_state_with_http_info(self, body, repository, **kwargs):  # noqa: E501
        """change_repo_state  # noqa: E501

        Change the state of a repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_repo_state_with_http_info(body, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChangeRepoState body: Request body contents. (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'repository']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_repo_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `change_repo_state`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `change_repo_state`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/api/v1/repository/{repository}/changestate', 'PUT',
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

    def change_repo_visibility(self, body, repository, **kwargs):  # noqa: E501
        """change_repo_visibility  # noqa: E501

        Change the visibility of a repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_repo_visibility(body, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChangeVisibility body: Request body contents. (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_repo_visibility_with_http_info(body, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.change_repo_visibility_with_http_info(body, repository, **kwargs)  # noqa: E501
            return data

    def change_repo_visibility_with_http_info(self, body, repository, **kwargs):  # noqa: E501
        """change_repo_visibility  # noqa: E501

        Change the visibility of a repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_repo_visibility_with_http_info(body, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChangeVisibility body: Request body contents. (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'repository']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_repo_visibility" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `change_repo_visibility`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `change_repo_visibility`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/api/v1/repository/{repository}/changevisibility', 'POST',
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

    def create_repo(self, body, **kwargs):  # noqa: E501
        """create_repo  # noqa: E501

        Create a new repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_repo(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewRepo body: Request body contents. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_repo_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_repo_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_repo_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_repo  # noqa: E501

        Create a new repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_repo_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewRepo body: Request body contents. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_repo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_repo`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/api/v1/repository', 'POST',
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

    def delete_repository(self, repository, **kwargs):  # noqa: E501
        """delete_repository  # noqa: E501

        Delete a repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_repository(repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_repository_with_http_info(repository, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_repository_with_http_info(repository, **kwargs)  # noqa: E501
            return data

    def delete_repository_with_http_info(self, repository, **kwargs):  # noqa: E501
        """delete_repository  # noqa: E501

        Delete a repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_repository_with_http_info(repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `delete_repository`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/api/v1/repository/{repository}', 'DELETE',
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

    def get_repo(self, repository, **kwargs):  # noqa: E501
        """get_repo  # noqa: E501

        Fetch the specified repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repo(repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :param bool include_tags: Whether to include repository tags
        :param bool include_stats: Whether to include action statistics
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_repo_with_http_info(repository, **kwargs)  # noqa: E501
        else:
            (data) = self.get_repo_with_http_info(repository, **kwargs)  # noqa: E501
            return data

    def get_repo_with_http_info(self, repository, **kwargs):  # noqa: E501
        """get_repo  # noqa: E501

        Fetch the specified repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repo_with_http_info(repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :param bool include_tags: Whether to include repository tags
        :param bool include_stats: Whether to include action statistics
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'include_tags', 'include_stats']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_repo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `get_repo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'include_tags' in params:
            query_params.append(('includeTags', params['include_tags']))  # noqa: E501
        if 'include_stats' in params:
            query_params.append(('includeStats', params['include_stats']))  # noqa: E501

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
            '/api/v1/repository/{repository}', 'GET',
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

    def list_repos(self, **kwargs):  # noqa: E501
        """list_repos  # noqa: E501

        Fetch the list of repositories visible to the current user under a variety of situations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_repos(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str next_page: The page token for the next page
        :param str repo_kind: The kind of repositories to return
        :param bool popularity: Whether to include the repository's popularity metric.
        :param bool last_modified: Whether to include when the repository was last modified.
        :param bool public: Adds any repositories visible to the user by virtue of being public
        :param bool starred: Filters the repositories returned to those starred by the user
        :param str namespace: Filters the repositories returned to this namespace
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_repos_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_repos_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_repos_with_http_info(self, **kwargs):  # noqa: E501
        """list_repos  # noqa: E501

        Fetch the list of repositories visible to the current user under a variety of situations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_repos_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str next_page: The page token for the next page
        :param str repo_kind: The kind of repositories to return
        :param bool popularity: Whether to include the repository's popularity metric.
        :param bool last_modified: Whether to include when the repository was last modified.
        :param bool public: Adds any repositories visible to the user by virtue of being public
        :param bool starred: Filters the repositories returned to those starred by the user
        :param str namespace: Filters the repositories returned to this namespace
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['next_page', 'repo_kind', 'popularity', 'last_modified', 'public', 'starred', 'namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_repos" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501
        if 'repo_kind' in params:
            query_params.append(('repo_kind', params['repo_kind']))  # noqa: E501
        if 'popularity' in params:
            query_params.append(('popularity', params['popularity']))  # noqa: E501
        if 'last_modified' in params:
            query_params.append(('last_modified', params['last_modified']))  # noqa: E501
        if 'public' in params:
            query_params.append(('public', params['public']))  # noqa: E501
        if 'starred' in params:
            query_params.append(('starred', params['starred']))  # noqa: E501
        if 'namespace' in params:
            query_params.append(('namespace', params['namespace']))  # noqa: E501

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
            '/api/v1/repository', 'GET',
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

    def update_repo(self, body, repository, **kwargs):  # noqa: E501
        """update_repo  # noqa: E501

        Update the description in the specified repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_repo(body, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RepoUpdate body: Request body contents. (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_repo_with_http_info(body, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.update_repo_with_http_info(body, repository, **kwargs)  # noqa: E501
            return data

    def update_repo_with_http_info(self, body, repository, **kwargs):  # noqa: E501
        """update_repo  # noqa: E501

        Update the description in the specified repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_repo_with_http_info(body, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RepoUpdate body: Request body contents. (required)
        :param str repository: The full path of the repository. e.g. namespace/name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'repository']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_repo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_repo`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `update_repo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/api/v1/repository/{repository}', 'PUT',
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
