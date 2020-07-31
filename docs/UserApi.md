# quay.UserApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_star**](UserApi.md#create_star) | **POST** /api/v1/user/starred | 
[**delete_star**](UserApi.md#delete_star) | **DELETE** /api/v1/user/starred/{repository} | 
[**get_logged_in_user**](UserApi.md#get_logged_in_user) | **GET** /api/v1/user/ | 
[**get_user_information**](UserApi.md#get_user_information) | **GET** /api/v1/users/{username} | 
[**list_starred_repos**](UserApi.md#list_starred_repos) | **GET** /api/v1/user/starred | 

# **create_star**
> create_star(body)



Star a repository.

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
api_instance = quay.UserApi(quay.ApiClient(configuration))
body = quay.NewStarredRepository() # NewStarredRepository | Request body contents.

try:
    api_instance.create_star(body)
except ApiException as e:
    print("Exception when calling UserApi->create_star: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewStarredRepository**](NewStarredRepository.md)| Request body contents. | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_star**
> delete_star(repository)



Removes a star from a repository.

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
api_instance = quay.UserApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.delete_star(repository)
except ApiException as e:
    print("Exception when calling UserApi->delete_star: %s\n" % e)
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

# **get_logged_in_user**
> UserView get_logged_in_user()



Get user information for the authenticated user.

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
api_instance = quay.UserApi(quay.ApiClient(configuration))

try:
    api_response = api_instance.get_logged_in_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_logged_in_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserView**](UserView.md)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_information**
> get_user_information(username)



Get user information for the specified user.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = quay.UserApi()
username = 'username_example' # str | 

try:
    api_instance.get_user_information(username)
except ApiException as e:
    print("Exception when calling UserApi->get_user_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_starred_repos**
> list_starred_repos(next_page=next_page)



List all starred repositories.

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
api_instance = quay.UserApi(quay.ApiClient(configuration))
next_page = 'next_page_example' # str | The page token for the next page (optional)

try:
    api_instance.list_starred_repos(next_page=next_page)
except ApiException as e:
    print("Exception when calling UserApi->list_starred_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | **str**| The page token for the next page | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

