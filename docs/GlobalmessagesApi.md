# quay.GlobalmessagesApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_message**](GlobalmessagesApi.md#create_global_message) | **POST** /api/v1/messages | 
[**delete_global_message**](GlobalmessagesApi.md#delete_global_message) | **DELETE** /api/v1/message/{uuid} | 
[**get_global_messages**](GlobalmessagesApi.md#get_global_messages) | **GET** /api/v1/messages | 

# **create_global_message**
> create_global_message(body)



Create a message.

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
api_instance = quay.GlobalmessagesApi(quay.ApiClient(configuration))
body = quay.CreateMessage() # CreateMessage | Request body contents.

try:
    api_instance.create_global_message(body)
except ApiException as e:
    print("Exception when calling GlobalmessagesApi->create_global_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMessage**](CreateMessage.md)| Request body contents. | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_global_message**
> delete_global_message(uuid)



Delete a message.

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
api_instance = quay.GlobalmessagesApi(quay.ApiClient(configuration))
uuid = 'uuid_example' # str | 

try:
    api_instance.delete_global_message(uuid)
except ApiException as e:
    print("Exception when calling GlobalmessagesApi->delete_global_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_messages**
> get_global_messages()



Return a super users messages.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = quay.GlobalmessagesApi()

try:
    api_instance.get_global_messages()
except ApiException as e:
    print("Exception when calling GlobalmessagesApi->get_global_messages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

