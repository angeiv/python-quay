# quay.RepositorynotificationApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repo_notification**](RepositorynotificationApi.md#create_repo_notification) | **POST** /api/v1/repository/{repository}/notification/ | 
[**delete_repo_notification**](RepositorynotificationApi.md#delete_repo_notification) | **DELETE** /api/v1/repository/{repository}/notification/{uuid} | 
[**get_repo_notification**](RepositorynotificationApi.md#get_repo_notification) | **GET** /api/v1/repository/{repository}/notification/{uuid} | 
[**list_repo_notifications**](RepositorynotificationApi.md#list_repo_notifications) | **GET** /api/v1/repository/{repository}/notification/ | 
[**reset_repository_notification_failures**](RepositorynotificationApi.md#reset_repository_notification_failures) | **POST** /api/v1/repository/{repository}/notification/{uuid} | 
[**test_repo_notification**](RepositorynotificationApi.md#test_repo_notification) | **POST** /api/v1/repository/{repository}/notification/{uuid}/test | 

# **create_repo_notification**
> create_repo_notification(body, repository)



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
api_instance = quay.RepositorynotificationApi(quay.ApiClient(configuration))
body = quay.NotificationCreateRequest() # NotificationCreateRequest | Request body contents.
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.create_repo_notification(body, repository)
except ApiException as e:
    print("Exception when calling RepositorynotificationApi->create_repo_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationCreateRequest**](NotificationCreateRequest.md)| Request body contents. | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repo_notification**
> delete_repo_notification(uuid, repository)



Deletes the specified notification.

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
api_instance = quay.RepositorynotificationApi(quay.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the notification
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.delete_repo_notification(uuid, repository)
except ApiException as e:
    print("Exception when calling RepositorynotificationApi->delete_repo_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the notification | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_notification**
> get_repo_notification(uuid, repository)



Get information for the specified notification.

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
api_instance = quay.RepositorynotificationApi(quay.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the notification
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.get_repo_notification(uuid, repository)
except ApiException as e:
    print("Exception when calling RepositorynotificationApi->get_repo_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the notification | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repo_notifications**
> list_repo_notifications(repository)



List the notifications for the specified repository.

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
api_instance = quay.RepositorynotificationApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.list_repo_notifications(repository)
except ApiException as e:
    print("Exception when calling RepositorynotificationApi->list_repo_notifications: %s\n" % e)
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

# **reset_repository_notification_failures**
> reset_repository_notification_failures(uuid, repository)



Resets repository notification to 0 failures.

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
api_instance = quay.RepositorynotificationApi(quay.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the notification
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.reset_repository_notification_failures(uuid, repository)
except ApiException as e:
    print("Exception when calling RepositorynotificationApi->reset_repository_notification_failures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the notification | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_repo_notification**
> test_repo_notification(uuid, repository)



Queues a test notification for this repository.

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
api_instance = quay.RepositorynotificationApi(quay.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the notification
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name

try:
    api_instance.test_repo_notification(uuid, repository)
except ApiException as e:
    print("Exception when calling RepositorynotificationApi->test_repo_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the notification | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

