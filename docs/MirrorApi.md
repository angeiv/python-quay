# quay.MirrorApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_repo_mirror_config**](MirrorApi.md#change_repo_mirror_config) | **PUT** /api/v1/repository/{repository}/mirror | 
[**create_repo_mirror_config**](MirrorApi.md#create_repo_mirror_config) | **POST** /api/v1/repository/{repository}/mirror | 
[**get_repo_mirror_config**](MirrorApi.md#get_repo_mirror_config) | **GET** /api/v1/repository/{repository}/mirror | 
[**sync_cancel**](MirrorApi.md#sync_cancel) | **POST** /api/v1/repository/{repository}/mirror/sync-cancel | 
[**sync_now**](MirrorApi.md#sync_now) | **POST** /api/v1/repository/{repository}/mirror/sync-now | 

# **change_repo_mirror_config**
> change_repo_mirror_config(body, repository)



Allow users to modifying the repository's mirroring configuration.

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
api_instance = quay.MirrorApi(quay.ApiClient(configuration))
body = quay.UpdateMirrorConfig() # UpdateMirrorConfig | Request body contents.
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.change_repo_mirror_config(body, repository)
except ApiException as e:
    print("Exception when calling MirrorApi->change_repo_mirror_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateMirrorConfig**](UpdateMirrorConfig.md)| Request body contents. | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repo_mirror_config**
> create_repo_mirror_config(body, repository)



Create a RepoMirrorConfig for a given Repository.

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
api_instance = quay.MirrorApi(quay.ApiClient(configuration))
body = quay.CreateMirrorConfig() # CreateMirrorConfig | Request body contents.
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.create_repo_mirror_config(body, repository)
except ApiException as e:
    print("Exception when calling MirrorApi->create_repo_mirror_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMirrorConfig**](CreateMirrorConfig.md)| Request body contents. | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_mirror_config**
> ViewMirrorConfig get_repo_mirror_config(repository)



Return the Mirror configuration for a given Repository.

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
api_instance = quay.MirrorApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_response = api_instance.get_repo_mirror_config(repository)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MirrorApi->get_repo_mirror_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

[**ViewMirrorConfig**](ViewMirrorConfig.md)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_cancel**
> sync_cancel(repository)



Update the sync_status for a given Repository's mirroring configuration.

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
api_instance = quay.MirrorApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.sync_cancel(repository)
except ApiException as e:
    print("Exception when calling MirrorApi->sync_cancel: %s\n" % e)
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

# **sync_now**
> sync_now(repository)



Update the sync_status for a given Repository's mirroring configuration.

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
api_instance = quay.MirrorApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.sync_now(repository)
except ApiException as e:
    print("Exception when calling MirrorApi->sync_now: %s\n" % e)
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

