# quay.RepotokenApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_token**](RepotokenApi.md#change_token) | **PUT** /api/v1/repository/{repository}/tokens/{code} | 
[**create_token**](RepotokenApi.md#create_token) | **POST** /api/v1/repository/{repository}/tokens/ | 
[**delete_token**](RepotokenApi.md#delete_token) | **DELETE** /api/v1/repository/{repository}/tokens/{code} | 
[**get_tokens**](RepotokenApi.md#get_tokens) | **GET** /api/v1/repository/{repository}/tokens/{code} | 
[**list_repo_tokens**](RepotokenApi.md#list_repo_tokens) | **GET** /api/v1/repository/{repository}/tokens/ | 

# **change_token**
> change_token(body, code, repository)



Update the permissions for the specified repository token.

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
api_instance = quay.RepotokenApi(quay.ApiClient(configuration))
body = quay.TokenPermission() # TokenPermission | Request body contents.
code = 'code_example' # str | The token code
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.change_token(body, code, repository)
except ApiException as e:
    print("Exception when calling RepotokenApi->change_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenPermission**](TokenPermission.md)| Request body contents. | 
 **code** | **str**| The token code | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token**
> create_token(body, repository)



Create a new repository token.

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
api_instance = quay.RepotokenApi(quay.ApiClient(configuration))
body = quay.NewToken() # NewToken | Request body contents.
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.create_token(body, repository)
except ApiException as e:
    print("Exception when calling RepotokenApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewToken**](NewToken.md)| Request body contents. | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> delete_token(code, repository)



Delete the repository token.

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
api_instance = quay.RepotokenApi(quay.ApiClient(configuration))
code = 'code_example' # str | The token code
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.delete_token(code, repository)
except ApiException as e:
    print("Exception when calling RepotokenApi->delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The token code | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens**
> get_tokens(code, repository)



Fetch the specified repository token information.

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
api_instance = quay.RepotokenApi(quay.ApiClient(configuration))
code = 'code_example' # str | The token code
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.get_tokens(code, repository)
except ApiException as e:
    print("Exception when calling RepotokenApi->get_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The token code | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repo_tokens**
> list_repo_tokens(repository)



List the tokens for the specified repository.

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
api_instance = quay.RepotokenApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.list_repo_tokens(repository)
except ApiException as e:
    print("Exception when calling RepotokenApi->list_repo_tokens: %s\n" % e)
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

