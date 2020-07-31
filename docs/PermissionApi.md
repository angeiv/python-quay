# quay.PermissionApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_team_permissions**](PermissionApi.md#change_team_permissions) | **PUT** /api/v1/repository/{repository}/permissions/team/{teamname} | 
[**change_user_permissions**](PermissionApi.md#change_user_permissions) | **PUT** /api/v1/repository/{repository}/permissions/user/{username} | 
[**delete_team_permissions**](PermissionApi.md#delete_team_permissions) | **DELETE** /api/v1/repository/{repository}/permissions/team/{teamname} | 
[**delete_user_permissions**](PermissionApi.md#delete_user_permissions) | **DELETE** /api/v1/repository/{repository}/permissions/user/{username} | 
[**get_team_permissions**](PermissionApi.md#get_team_permissions) | **GET** /api/v1/repository/{repository}/permissions/team/{teamname} | 
[**get_user_permissions**](PermissionApi.md#get_user_permissions) | **GET** /api/v1/repository/{repository}/permissions/user/{username} | 
[**get_user_transitive_permission**](PermissionApi.md#get_user_transitive_permission) | **GET** /api/v1/repository/{repository}/permissions/user/{username}/transitive | 
[**list_repo_team_permissions**](PermissionApi.md#list_repo_team_permissions) | **GET** /api/v1/repository/{repository}/permissions/team/ | 
[**list_repo_user_permissions**](PermissionApi.md#list_repo_user_permissions) | **GET** /api/v1/repository/{repository}/permissions/user/ | 

# **change_team_permissions**
> change_team_permissions(body, teamname, repository)



Update the existing team permission.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_implicit
configuration = quay.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = quay.PermissionApi(quay.ApiClient(configuration))
body = quay.TeamPermission() # TeamPermission | Request body contents.
teamname = 'teamname_example' # str | The name of the team to which the permission applies
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.change_team_permissions(body, teamname, repository)
except ApiException as e:
    print("Exception when calling PermissionApi->change_team_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamPermission**](TeamPermission.md)| Request body contents. | 
 **teamname** | **str**| The name of the team to which the permission applies | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_permissions**
> change_user_permissions(body, username, repository)



Update the perimssions for an existing repository.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_implicit
configuration = quay.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = quay.PermissionApi(quay.ApiClient(configuration))
body = quay.UserPermission() # UserPermission | Request body contents.
username = 'username_example' # str | The username of the user to which the permission applies
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.change_user_permissions(body, username, repository)
except ApiException as e:
    print("Exception when calling PermissionApi->change_user_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserPermission**](UserPermission.md)| Request body contents. | 
 **username** | **str**| The username of the user to which the permission applies | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_permissions**
> delete_team_permissions(teamname, repository)



Delete the permission for the specified team.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_implicit
configuration = quay.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = quay.PermissionApi(quay.ApiClient(configuration))
teamname = 'teamname_example' # str | The name of the team to which the permission applies
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.delete_team_permissions(teamname, repository)
except ApiException as e:
    print("Exception when calling PermissionApi->delete_team_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamname** | **str**| The name of the team to which the permission applies | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_permissions**
> delete_user_permissions(username, repository)



Delete the permission for the user.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_implicit
configuration = quay.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = quay.PermissionApi(quay.ApiClient(configuration))
username = 'username_example' # str | The username of the user to which the permission applies
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.delete_user_permissions(username, repository)
except ApiException as e:
    print("Exception when calling PermissionApi->delete_user_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user to which the permission applies | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_permissions**
> get_team_permissions(teamname, repository)



Fetch the permission for the specified team.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_implicit
configuration = quay.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = quay.PermissionApi(quay.ApiClient(configuration))
teamname = 'teamname_example' # str | The name of the team to which the permission applies
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.get_team_permissions(teamname, repository)
except ApiException as e:
    print("Exception when calling PermissionApi->get_team_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamname** | **str**| The name of the team to which the permission applies | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_permissions**
> get_user_permissions(username, repository)



Get the permission for the specified user.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_implicit
configuration = quay.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = quay.PermissionApi(quay.ApiClient(configuration))
username = 'username_example' # str | The username of the user to which the permission applies
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.get_user_permissions(username, repository)
except ApiException as e:
    print("Exception when calling PermissionApi->get_user_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user to which the permission applies | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_transitive_permission**
> get_user_transitive_permission(username, repository)



Get the fetch the permission for the specified user.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_implicit
configuration = quay.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = quay.PermissionApi(quay.ApiClient(configuration))
username = 'username_example' # str | The username of the user to which the permissions apply
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.get_user_transitive_permission(username, repository)
except ApiException as e:
    print("Exception when calling PermissionApi->get_user_transitive_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user to which the permissions apply | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repo_team_permissions**
> list_repo_team_permissions(repository)



List all team permission.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_implicit
configuration = quay.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = quay.PermissionApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.list_repo_team_permissions(repository)
except ApiException as e:
    print("Exception when calling PermissionApi->list_repo_team_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repo_user_permissions**
> list_repo_user_permissions(repository)



List all user permissions.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_implicit
configuration = quay.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = quay.PermissionApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.list_repo_user_permissions(repository)
except ApiException as e:
    print("Exception when calling PermissionApi->list_repo_user_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

