# quay.BuildApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_repo_build**](BuildApi.md#cancel_repo_build) | **DELETE** /api/v1/repository/{repository}/build/{build_uuid} | 
[**get_repo_build**](BuildApi.md#get_repo_build) | **GET** /api/v1/repository/{repository}/build/{build_uuid} | 
[**get_repo_build_logs**](BuildApi.md#get_repo_build_logs) | **GET** /api/v1/repository/{repository}/build/{build_uuid}/logs | 
[**get_repo_build_status**](BuildApi.md#get_repo_build_status) | **GET** /api/v1/repository/{repository}/build/{build_uuid}/status | 
[**get_repo_builds**](BuildApi.md#get_repo_builds) | **GET** /api/v1/repository/{repository}/build/ | 
[**request_repo_build**](BuildApi.md#request_repo_build) | **POST** /api/v1/repository/{repository}/build/ | 

# **cancel_repo_build**
> cancel_repo_build(build_uuid, repository)



Cancels a repository build.

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
api_instance = quay.BuildApi(quay.ApiClient(configuration))
build_uuid = 'build_uuid_example' # str | The UUID of the build
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.cancel_repo_build(build_uuid, repository)
except ApiException as e:
    print("Exception when calling BuildApi->cancel_repo_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_uuid** | **str**| The UUID of the build | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_build**
> get_repo_build(build_uuid, repository)



Returns information about a build.

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
api_instance = quay.BuildApi(quay.ApiClient(configuration))
build_uuid = 'build_uuid_example' # str | The UUID of the build
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.get_repo_build(build_uuid, repository)
except ApiException as e:
    print("Exception when calling BuildApi->get_repo_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_uuid** | **str**| The UUID of the build | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_build_logs**
> get_repo_build_logs(build_uuid, repository)



Return the build logs for the build specified by the build uuid.

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
api_instance = quay.BuildApi(quay.ApiClient(configuration))
build_uuid = 'build_uuid_example' # str | The UUID of the build
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.get_repo_build_logs(build_uuid, repository)
except ApiException as e:
    print("Exception when calling BuildApi->get_repo_build_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_uuid** | **str**| The UUID of the build | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_build_status**
> get_repo_build_status(build_uuid, repository)



Return the status for the builds specified by the build uuids.

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
api_instance = quay.BuildApi(quay.ApiClient(configuration))
build_uuid = 'build_uuid_example' # str | The UUID of the build
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.get_repo_build_status(build_uuid, repository)
except ApiException as e:
    print("Exception when calling BuildApi->get_repo_build_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_uuid** | **str**| The UUID of the build | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_builds**
> get_repo_builds(repository, since=since, limit=limit)



Get the list of repository builds.

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
api_instance = quay.BuildApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
since = 56 # int | Returns all builds since the given unix timecode (optional)
limit = 56 # int | The maximum number of builds to return (optional)

try:
    api_instance.get_repo_builds(repository, since=since, limit=limit)
except ApiException as e:
    print("Exception when calling BuildApi->get_repo_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **since** | **int**| Returns all builds since the given unix timecode | [optional] 
 **limit** | **int**| The maximum number of builds to return | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_repo_build**
> request_repo_build(body, repository)



Request that a repository be built and pushed from the specified input.

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
api_instance = quay.BuildApi(quay.ApiClient(configuration))
body = quay.RepositoryBuildRequest() # RepositoryBuildRequest | Request body contents.
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.request_repo_build(body, repository)
except ApiException as e:
    print("Exception when calling BuildApi->request_repo_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepositoryBuildRequest**](RepositoryBuildRequest.md)| Request body contents. | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

