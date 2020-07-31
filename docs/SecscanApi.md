# quay.SecscanApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_repo_image_security**](SecscanApi.md#get_repo_image_security) | **GET** /api/v1/repository/{repository}/image/{imageid}/security | 
[**get_repo_manifest_security**](SecscanApi.md#get_repo_manifest_security) | **GET** /api/v1/repository/{repository}/manifest/{manifestref}/security | 

# **get_repo_image_security**
> get_repo_image_security(repository, imageid, vulnerabilities=vulnerabilities)



Fetches the features and vulnerabilities (if any) for a repository image.

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
api_instance = quay.SecscanApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
imageid = 'imageid_example' # str | The image ID
vulnerabilities = true # bool | Include vulnerabilities information (optional)

try:
    api_instance.get_repo_image_security(repository, imageid, vulnerabilities=vulnerabilities)
except ApiException as e:
    print("Exception when calling SecscanApi->get_repo_image_security: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **imageid** | **str**| The image ID | 
 **vulnerabilities** | **bool**| Include vulnerabilities information | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_manifest_security**
> get_repo_manifest_security(manifestref, repository, vulnerabilities=vulnerabilities)



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
api_instance = quay.SecscanApi(quay.ApiClient(configuration))
manifestref = 'manifestref_example' # str | The digest of the manifest
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
vulnerabilities = true # bool | Include vulnerabilities informations (optional)

try:
    api_instance.get_repo_manifest_security(manifestref, repository, vulnerabilities=vulnerabilities)
except ApiException as e:
    print("Exception when calling SecscanApi->get_repo_manifest_security: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifestref** | **str**| The digest of the manifest | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **vulnerabilities** | **bool**| Include vulnerabilities informations | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

