# quay.TriggerApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_build_trigger**](TriggerApi.md#activate_build_trigger) | **POST** /api/v1/repository/{repository}/trigger/{trigger_uuid}/activate | 
[**delete_build_trigger**](TriggerApi.md#delete_build_trigger) | **DELETE** /api/v1/repository/{repository}/trigger/{trigger_uuid} | 
[**get_build_trigger**](TriggerApi.md#get_build_trigger) | **GET** /api/v1/repository/{repository}/trigger/{trigger_uuid} | 
[**list_build_triggers**](TriggerApi.md#list_build_triggers) | **GET** /api/v1/repository/{repository}/trigger/ | 
[**list_trigger_recent_builds**](TriggerApi.md#list_trigger_recent_builds) | **GET** /api/v1/repository/{repository}/trigger/{trigger_uuid}/builds | 
[**manually_start_build_trigger**](TriggerApi.md#manually_start_build_trigger) | **POST** /api/v1/repository/{repository}/trigger/{trigger_uuid}/start | 
[**update_build_trigger**](TriggerApi.md#update_build_trigger) | **PUT** /api/v1/repository/{repository}/trigger/{trigger_uuid} | 

# **activate_build_trigger**
> activate_build_trigger(body, trigger_uuid, repository)



Activate the specified build trigger.

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
api_instance = quay.TriggerApi(quay.ApiClient(configuration))
body = quay.BuildTriggerActivateRequest() # BuildTriggerActivateRequest | Request body contents.
trigger_uuid = 'trigger_uuid_example' # str | The UUID of the build trigger
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.activate_build_trigger(body, trigger_uuid, repository)
except ApiException as e:
    print("Exception when calling TriggerApi->activate_build_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BuildTriggerActivateRequest**](BuildTriggerActivateRequest.md)| Request body contents. | 
 **trigger_uuid** | **str**| The UUID of the build trigger | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_build_trigger**
> delete_build_trigger(trigger_uuid, repository)



Delete the specified build trigger.

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
api_instance = quay.TriggerApi(quay.ApiClient(configuration))
trigger_uuid = 'trigger_uuid_example' # str | The UUID of the build trigger
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.delete_build_trigger(trigger_uuid, repository)
except ApiException as e:
    print("Exception when calling TriggerApi->delete_build_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_uuid** | **str**| The UUID of the build trigger | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_trigger**
> get_build_trigger(trigger_uuid, repository)



Get information for the specified build trigger.

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
api_instance = quay.TriggerApi(quay.ApiClient(configuration))
trigger_uuid = 'trigger_uuid_example' # str | The UUID of the build trigger
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.get_build_trigger(trigger_uuid, repository)
except ApiException as e:
    print("Exception when calling TriggerApi->get_build_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_uuid** | **str**| The UUID of the build trigger | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_build_triggers**
> list_build_triggers(repository)



List the triggers for the specified repository.

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
api_instance = quay.TriggerApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.list_build_triggers(repository)
except ApiException as e:
    print("Exception when calling TriggerApi->list_build_triggers: %s\n" % e)
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

# **list_trigger_recent_builds**
> list_trigger_recent_builds(trigger_uuid, repository, limit=limit)



List the builds started by the specified trigger.

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
api_instance = quay.TriggerApi(quay.ApiClient(configuration))
trigger_uuid = 'trigger_uuid_example' # str | The UUID of the build trigger
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
limit = 56 # int | The maximum number of builds to return (optional)

try:
    api_instance.list_trigger_recent_builds(trigger_uuid, repository, limit=limit)
except ApiException as e:
    print("Exception when calling TriggerApi->list_trigger_recent_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_uuid** | **str**| The UUID of the build trigger | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **limit** | **int**| The maximum number of builds to return | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manually_start_build_trigger**
> manually_start_build_trigger(body, trigger_uuid, repository)



Manually start a build from the specified trigger.

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
api_instance = quay.TriggerApi(quay.ApiClient(configuration))
body = quay.RunParameters() # RunParameters | Request body contents.
trigger_uuid = 'trigger_uuid_example' # str | The UUID of the build trigger
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.manually_start_build_trigger(body, trigger_uuid, repository)
except ApiException as e:
    print("Exception when calling TriggerApi->manually_start_build_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RunParameters**](RunParameters.md)| Request body contents. | 
 **trigger_uuid** | **str**| The UUID of the build trigger | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_build_trigger**
> update_build_trigger(body, trigger_uuid, repository)



Updates the specified build trigger.

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
api_instance = quay.TriggerApi(quay.ApiClient(configuration))
body = quay.UpdateTrigger() # UpdateTrigger | Request body contents.
trigger_uuid = 'trigger_uuid_example' # str | The UUID of the build trigger
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.update_build_trigger(body, trigger_uuid, repository)
except ApiException as e:
    print("Exception when calling TriggerApi->update_build_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTrigger**](UpdateTrigger.md)| Request body contents. | 
 **trigger_uuid** | **str**| The UUID of the build trigger | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

