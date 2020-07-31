# quay.ManifestApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_manifest_label**](ManifestApi.md#add_manifest_label) | **POST** /api/v1/repository/{repository}/manifest/{manifestref}/labels | 
[**delete_manifest_label**](ManifestApi.md#delete_manifest_label) | **DELETE** /api/v1/repository/{repository}/manifest/{manifestref}/labels/{labelid} | 
[**get_manifest_label**](ManifestApi.md#get_manifest_label) | **GET** /api/v1/repository/{repository}/manifest/{manifestref}/labels/{labelid} | 
[**get_repo_manifest**](ManifestApi.md#get_repo_manifest) | **GET** /api/v1/repository/{repository}/manifest/{manifestref} | 
[**list_manifest_labels**](ManifestApi.md#list_manifest_labels) | **GET** /api/v1/repository/{repository}/manifest/{manifestref}/labels | 

# **add_manifest_label**
> add_manifest_label(body, manifestref, repository)



Adds a new label into the tag manifest.

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
api_instance = quay.ManifestApi(quay.ApiClient(configuration))
body = quay.AddLabel() # AddLabel | Request body contents.
manifestref = 'manifestref_example' # str | The digest of the manifest
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.add_manifest_label(body, manifestref, repository)
except ApiException as e:
    print("Exception when calling ManifestApi->add_manifest_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddLabel**](AddLabel.md)| Request body contents. | 
 **manifestref** | **str**| The digest of the manifest | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manifest_label**
> delete_manifest_label(labelid, manifestref, repository)



Deletes an existing label from a manifest.

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
api_instance = quay.ManifestApi(quay.ApiClient(configuration))
labelid = 'labelid_example' # str | The ID of the label
manifestref = 'manifestref_example' # str | The digest of the manifest
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.delete_manifest_label(labelid, manifestref, repository)
except ApiException as e:
    print("Exception when calling ManifestApi->delete_manifest_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labelid** | **str**| The ID of the label | 
 **manifestref** | **str**| The digest of the manifest | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manifest_label**
> get_manifest_label(labelid, manifestref, repository)



Retrieves the label with the specific ID under the manifest.

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
api_instance = quay.ManifestApi(quay.ApiClient(configuration))
labelid = 'labelid_example' # str | The ID of the label
manifestref = 'manifestref_example' # str | The digest of the manifest
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.get_manifest_label(labelid, manifestref, repository)
except ApiException as e:
    print("Exception when calling ManifestApi->get_manifest_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labelid** | **str**| The ID of the label | 
 **manifestref** | **str**| The digest of the manifest | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_manifest**
> get_repo_manifest(manifestref, repository)



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
api_instance = quay.ManifestApi(quay.ApiClient(configuration))
manifestref = 'manifestref_example' # str | The digest of the manifest
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.get_repo_manifest(manifestref, repository)
except ApiException as e:
    print("Exception when calling ManifestApi->get_repo_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifestref** | **str**| The digest of the manifest | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_manifest_labels**
> list_manifest_labels(manifestref, repository, filter=filter)



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
api_instance = quay.ManifestApi(quay.ApiClient(configuration))
manifestref = 'manifestref_example' # str | The digest of the manifest
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
filter = 'filter_example' # str | If specified, only labels matching the given prefix will be returned (optional)

try:
    api_instance.list_manifest_labels(manifestref, repository, filter=filter)
except ApiException as e:
    print("Exception when calling ManifestApi->list_manifest_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifestref** | **str**| The digest of the manifest | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **filter** | **str**| If specified, only labels matching the given prefix will be returned | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

