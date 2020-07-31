# quay.RepositoryApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_repo_state**](RepositoryApi.md#change_repo_state) | **PUT** /api/v1/repository/{repository}/changestate | 
[**change_repo_visibility**](RepositoryApi.md#change_repo_visibility) | **POST** /api/v1/repository/{repository}/changevisibility | 
[**create_repo**](RepositoryApi.md#create_repo) | **POST** /api/v1/repository | 
[**delete_repository**](RepositoryApi.md#delete_repository) | **DELETE** /api/v1/repository/{repository} | 
[**get_repo**](RepositoryApi.md#get_repo) | **GET** /api/v1/repository/{repository} | 
[**list_repos**](RepositoryApi.md#list_repos) | **GET** /api/v1/repository | 
[**update_repo**](RepositoryApi.md#update_repo) | **PUT** /api/v1/repository/{repository} | 

# **change_repo_state**
> change_repo_state(body, repository)



Change the state of a repository.

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
api_instance = quay.RepositoryApi(quay.ApiClient(configuration))
body = quay.ChangeRepoState() # ChangeRepoState | Request body contents.
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.change_repo_state(body, repository)
except ApiException as e:
    print("Exception when calling RepositoryApi->change_repo_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeRepoState**](ChangeRepoState.md)| Request body contents. | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_repo_visibility**
> change_repo_visibility(body, repository)



Change the visibility of a repository.

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
api_instance = quay.RepositoryApi(quay.ApiClient(configuration))
body = quay.ChangeVisibility() # ChangeVisibility | Request body contents.
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.change_repo_visibility(body, repository)
except ApiException as e:
    print("Exception when calling RepositoryApi->change_repo_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeVisibility**](ChangeVisibility.md)| Request body contents. | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repo**
> create_repo(body)



Create a new repository.

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
api_instance = quay.RepositoryApi(quay.ApiClient(configuration))
body = quay.NewRepo() # NewRepo | Request body contents.

try:
    api_instance.create_repo(body)
except ApiException as e:
    print("Exception when calling RepositoryApi->create_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewRepo**](NewRepo.md)| Request body contents. | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repository**
> delete_repository(repository)



Delete a repository.

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
api_instance = quay.RepositoryApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.delete_repository(repository)
except ApiException as e:
    print("Exception when calling RepositoryApi->delete_repository: %s\n" % e)
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

# **get_repo**
> get_repo(repository, include_tags=include_tags, include_stats=include_stats)



Fetch the specified repository.

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
api_instance = quay.RepositoryApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
include_tags = true # bool | Whether to include repository tags (optional)
include_stats = true # bool | Whether to include action statistics (optional)

try:
    api_instance.get_repo(repository, include_tags=include_tags, include_stats=include_stats)
except ApiException as e:
    print("Exception when calling RepositoryApi->get_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **include_tags** | **bool**| Whether to include repository tags | [optional] 
 **include_stats** | **bool**| Whether to include action statistics | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repos**
> list_repos(next_page=next_page, repo_kind=repo_kind, popularity=popularity, last_modified=last_modified, public=public, starred=starred, namespace=namespace)



Fetch the list of repositories visible to the current user under a variety of situations.

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
api_instance = quay.RepositoryApi(quay.ApiClient(configuration))
next_page = 'next_page_example' # str | The page token for the next page (optional)
repo_kind = 'repo_kind_example' # str | The kind of repositories to return (optional)
popularity = true # bool | Whether to include the repository's popularity metric. (optional)
last_modified = true # bool | Whether to include when the repository was last modified. (optional)
public = true # bool | Adds any repositories visible to the user by virtue of being public (optional)
starred = true # bool | Filters the repositories returned to those starred by the user (optional)
namespace = 'namespace_example' # str | Filters the repositories returned to this namespace (optional)

try:
    api_instance.list_repos(next_page=next_page, repo_kind=repo_kind, popularity=popularity, last_modified=last_modified, public=public, starred=starred, namespace=namespace)
except ApiException as e:
    print("Exception when calling RepositoryApi->list_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | **str**| The page token for the next page | [optional] 
 **repo_kind** | **str**| The kind of repositories to return | [optional] 
 **popularity** | **bool**| Whether to include the repository&#x27;s popularity metric. | [optional] 
 **last_modified** | **bool**| Whether to include when the repository was last modified. | [optional] 
 **public** | **bool**| Adds any repositories visible to the user by virtue of being public | [optional] 
 **starred** | **bool**| Filters the repositories returned to those starred by the user | [optional] 
 **namespace** | **str**| Filters the repositories returned to this namespace | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repo**
> update_repo(body, repository)



Update the description in the specified repository.

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
api_instance = quay.RepositoryApi(quay.ApiClient(configuration))
body = quay.RepoUpdate() # RepoUpdate | Request body contents.
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.update_repo(body, repository)
except ApiException as e:
    print("Exception when calling RepositoryApi->update_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepoUpdate**](RepoUpdate.md)| Request body contents. | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

