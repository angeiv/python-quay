# quay.SearchApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conduct_repo_search**](SearchApi.md#conduct_repo_search) | **GET** /api/v1/find/repositories | 
[**conduct_search**](SearchApi.md#conduct_search) | **GET** /api/v1/find/all | 
[**get_matching_entities**](SearchApi.md#get_matching_entities) | **GET** /api/v1/entities/{prefix} | 

# **conduct_repo_search**
> conduct_repo_search(page=page, query=query)



Get a list of apps and repositories that match the specified query.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = quay.SearchApi()
page = 56 # int | The page. (optional)
query = 'query_example' # str | The search query. (optional)

try:
    api_instance.conduct_repo_search(page=page, query=query)
except ApiException as e:
    print("Exception when calling SearchApi->conduct_repo_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page. | [optional] 
 **query** | **str**| The search query. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conduct_search**
> conduct_search(query=query)



Get a list of entities and resources that match the specified query.

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
api_instance = quay.SearchApi(quay.ApiClient(configuration))
query = 'query_example' # str | The search query. (optional)

try:
    api_instance.conduct_search(query=query)
except ApiException as e:
    print("Exception when calling SearchApi->conduct_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_matching_entities**
> get_matching_entities(prefix, include_orgs=include_orgs, include_teams=include_teams, namespace=namespace)



Get a list of entities that match the specified prefix.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = quay.SearchApi()
prefix = 'prefix_example' # str | 
include_orgs = true # bool | Whether to include orgs names. (optional)
include_teams = true # bool | Whether to include team names. (optional)
namespace = 'namespace_example' # str | Namespace to use when querying for org entities. (optional)

try:
    api_instance.get_matching_entities(prefix, include_orgs=include_orgs, include_teams=include_teams, namespace=namespace)
except ApiException as e:
    print("Exception when calling SearchApi->get_matching_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**|  | 
 **include_orgs** | **bool**| Whether to include orgs names. | [optional] 
 **include_teams** | **bool**| Whether to include team names. | [optional] 
 **namespace** | **str**| Namespace to use when querying for org entities. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

