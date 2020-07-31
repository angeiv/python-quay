# quay.TagApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_tag**](TagApi.md#change_tag) | **PUT** /api/v1/repository/{repository}/tag/{tag} | 
[**delete_full_tag**](TagApi.md#delete_full_tag) | **DELETE** /api/v1/repository/{repository}/tag/{tag} | 
[**list_repo_tags**](TagApi.md#list_repo_tags) | **GET** /api/v1/repository/{repository}/tag/ | 
[**list_tag_images**](TagApi.md#list_tag_images) | **GET** /api/v1/repository/{repository}/tag/{tag}/images | 
[**restore_tag**](TagApi.md#restore_tag) | **POST** /api/v1/repository/{repository}/tag/{tag}/restore | 

# **change_tag**
> change_tag(body, tag, repository)



Change which image a tag points to or create a new tag.

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
api_instance = quay.TagApi(quay.ApiClient(configuration))
body = quay.ChangeTag() # ChangeTag | Request body contents.
tag = 'tag_example' # str | The name of the tag
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.change_tag(body, tag, repository)
except ApiException as e:
    print("Exception when calling TagApi->change_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeTag**](ChangeTag.md)| Request body contents. | 
 **tag** | **str**| The name of the tag | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_full_tag**
> delete_full_tag(tag, repository)



Delete the specified repository tag.

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
api_instance = quay.TagApi(quay.ApiClient(configuration))
tag = 'tag_example' # str | The name of the tag
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.delete_full_tag(tag, repository)
except ApiException as e:
    print("Exception when calling TagApi->delete_full_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| The name of the tag | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repo_tags**
> list_repo_tags(repository, only_active_tags=only_active_tags, page=page, limit=limit, specific_tag=specific_tag)



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
api_instance = quay.TagApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
only_active_tags = true # bool | Filter to only active tags. (optional)
page = 56 # int | Page index for the results. Default 1. (optional)
limit = 56 # int | Limit to the number of results to return per page. Max 100. (optional)
specific_tag = 'specific_tag_example' # str | Filters the tags to the specific tag. (optional)

try:
    api_instance.list_repo_tags(repository, only_active_tags=only_active_tags, page=page, limit=limit, specific_tag=specific_tag)
except ApiException as e:
    print("Exception when calling TagApi->list_repo_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **only_active_tags** | **bool**| Filter to only active tags. | [optional] 
 **page** | **int**| Page index for the results. Default 1. | [optional] 
 **limit** | **int**| Limit to the number of results to return per page. Max 100. | [optional] 
 **specific_tag** | **str**| Filters the tags to the specific tag. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tag_images**
> list_tag_images(tag, repository, owned=owned)



List the images for the specified repository tag.

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
api_instance = quay.TagApi(quay.ApiClient(configuration))
tag = 'tag_example' # str | The name of the tag
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
owned = true # bool | If specified, only images wholely owned by this tag are returned. (optional)

try:
    api_instance.list_tag_images(tag, repository, owned=owned)
except ApiException as e:
    print("Exception when calling TagApi->list_tag_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| The name of the tag | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **owned** | **bool**| If specified, only images wholely owned by this tag are returned. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_tag**
> restore_tag(body, tag, repository)



Restores a repository tag back to a previous image in the repository.

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
api_instance = quay.TagApi(quay.ApiClient(configuration))
body = quay.RestoreTag() # RestoreTag | Request body contents.
tag = 'tag_example' # str | The name of the tag
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.restore_tag(body, tag, repository)
except ApiException as e:
    print("Exception when calling TagApi->restore_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestoreTag**](RestoreTag.md)| Request body contents. | 
 **tag** | **str**| The name of the tag | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

