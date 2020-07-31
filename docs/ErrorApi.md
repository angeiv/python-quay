# quay.ErrorApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_error_description**](ErrorApi.md#get_error_description) | **GET** /api/v1/error/{error_type} | 

# **get_error_description**
> ApiErrorDescription get_error_description(error_type)



Get a detailed description of the error.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = quay.ErrorApi()
error_type = 'error_type_example' # str | The error code identifying the type of error.

try:
    api_response = api_instance.get_error_description(error_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ErrorApi->get_error_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_type** | **str**| The error code identifying the type of error. | 

### Return type

[**ApiErrorDescription**](ApiErrorDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

