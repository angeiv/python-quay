# quay.AppspecifictokensApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_token**](AppspecifictokensApi.md#create_app_token) | **POST** /api/v1/user/apptoken | 
[**get_app_token**](AppspecifictokensApi.md#get_app_token) | **GET** /api/v1/user/apptoken/{token_uuid} | 
[**list_app_tokens**](AppspecifictokensApi.md#list_app_tokens) | **GET** /api/v1/user/apptoken | 
[**revoke_app_token**](AppspecifictokensApi.md#revoke_app_token) | **DELETE** /api/v1/user/apptoken/{token_uuid} | 

# **create_app_token**
> create_app_token(body)



Create a new app specific token for user.

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
api_instance = quay.AppspecifictokensApi(quay.ApiClient(configuration))
body = quay.NewToken() # NewToken | Request body contents.

try:
    api_instance.create_app_token(body)
except ApiException as e:
    print("Exception when calling AppspecifictokensApi->create_app_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewToken**](NewToken.md)| Request body contents. | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_token**
> get_app_token(token_uuid)



Returns a specific app token for the user.

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
api_instance = quay.AppspecifictokensApi(quay.ApiClient(configuration))
token_uuid = 'token_uuid_example' # str | The uuid of the app specific token

try:
    api_instance.get_app_token(token_uuid)
except ApiException as e:
    print("Exception when calling AppspecifictokensApi->get_app_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_uuid** | **str**| The uuid of the app specific token | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_tokens**
> list_app_tokens(expiring=expiring)



Lists the app specific tokens for the user.

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
api_instance = quay.AppspecifictokensApi(quay.ApiClient(configuration))
expiring = true # bool | If true, only returns those tokens expiring soon (optional)

try:
    api_instance.list_app_tokens(expiring=expiring)
except ApiException as e:
    print("Exception when calling AppspecifictokensApi->list_app_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expiring** | **bool**| If true, only returns those tokens expiring soon | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_app_token**
> revoke_app_token(token_uuid)



Revokes a specific app token for the user.

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
api_instance = quay.AppspecifictokensApi(quay.ApiClient(configuration))
token_uuid = 'token_uuid_example' # str | The uuid of the app specific token

try:
    api_instance.revoke_app_token(token_uuid)
except ApiException as e:
    print("Exception when calling AppspecifictokensApi->revoke_app_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_uuid** | **str**| The uuid of the app specific token | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

