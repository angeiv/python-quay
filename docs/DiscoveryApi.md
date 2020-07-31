# quay.DiscoveryApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discovery**](DiscoveryApi.md#discovery) | **GET** /api/v1/discovery | 

# **discovery**
> discovery(internal=internal)



List all of the API endpoints available in the swagger API format.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = quay.DiscoveryApi()
internal = true # bool | Whether to include internal APIs. (optional)

try:
    api_instance.discovery(internal=internal)
except ApiException as e:
    print("Exception when calling DiscoveryApi->discovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal** | **bool**| Whether to include internal APIs. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

