# quay.PrototypeApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_prototype_permission**](PrototypeApi.md#create_organization_prototype_permission) | **POST** /api/v1/organization/{orgname}/prototypes | 
[**delete_organization_prototype_permission**](PrototypeApi.md#delete_organization_prototype_permission) | **DELETE** /api/v1/organization/{orgname}/prototypes/{prototypeid} | 
[**get_organization_prototype_permissions**](PrototypeApi.md#get_organization_prototype_permissions) | **GET** /api/v1/organization/{orgname}/prototypes | 
[**update_organization_prototype_permission**](PrototypeApi.md#update_organization_prototype_permission) | **PUT** /api/v1/organization/{orgname}/prototypes/{prototypeid} | 

# **create_organization_prototype_permission**
> create_organization_prototype_permission(body, orgname)



Create a new permission prototype.

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
api_instance = quay.PrototypeApi(quay.ApiClient(configuration))
body = quay.NewPrototype() # NewPrototype | Request body contents.
orgname = 'orgname_example' # str | The name of the organization

try:
    api_instance.create_organization_prototype_permission(body, orgname)
except ApiException as e:
    print("Exception when calling PrototypeApi->create_organization_prototype_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewPrototype**](NewPrototype.md)| Request body contents. | 
 **orgname** | **str**| The name of the organization | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_prototype_permission**
> delete_organization_prototype_permission(orgname, prototypeid)



Delete an existing permission prototype.

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
api_instance = quay.PrototypeApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
prototypeid = 'prototypeid_example' # str | The ID of the prototype

try:
    api_instance.delete_organization_prototype_permission(orgname, prototypeid)
except ApiException as e:
    print("Exception when calling PrototypeApi->delete_organization_prototype_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **prototypeid** | **str**| The ID of the prototype | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_prototype_permissions**
> get_organization_prototype_permissions(orgname)



List the existing prototypes for this organization.

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
api_instance = quay.PrototypeApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization

try:
    api_instance.get_organization_prototype_permissions(orgname)
except ApiException as e:
    print("Exception when calling PrototypeApi->get_organization_prototype_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_prototype_permission**
> update_organization_prototype_permission(body, orgname, prototypeid)



Update the role of an existing permission prototype.

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
api_instance = quay.PrototypeApi(quay.ApiClient(configuration))
body = quay.PrototypeUpdate() # PrototypeUpdate | Request body contents.
orgname = 'orgname_example' # str | The name of the organization
prototypeid = 'prototypeid_example' # str | The ID of the prototype

try:
    api_instance.update_organization_prototype_permission(body, orgname, prototypeid)
except ApiException as e:
    print("Exception when calling PrototypeApi->update_organization_prototype_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrototypeUpdate**](PrototypeUpdate.md)| Request body contents. | 
 **orgname** | **str**| The name of the organization | 
 **prototypeid** | **str**| The ID of the prototype | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

