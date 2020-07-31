# quay.OrganizationApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_organization_details**](OrganizationApi.md#change_organization_details) | **PUT** /api/v1/organization/{orgname} | 
[**create_organization**](OrganizationApi.md#create_organization) | **POST** /api/v1/organization/ | 
[**create_organization_application**](OrganizationApi.md#create_organization_application) | **POST** /api/v1/organization/{orgname}/applications | 
[**delete_admined_organization**](OrganizationApi.md#delete_admined_organization) | **DELETE** /api/v1/organization/{orgname} | 
[**delete_organization_application**](OrganizationApi.md#delete_organization_application) | **DELETE** /api/v1/organization/{orgname}/applications/{client_id} | 
[**get_application_information**](OrganizationApi.md#get_application_information) | **GET** /api/v1/app/{client_id} | 
[**get_organization**](OrganizationApi.md#get_organization) | **GET** /api/v1/organization/{orgname} | 
[**get_organization_application**](OrganizationApi.md#get_organization_application) | **GET** /api/v1/organization/{orgname}/applications/{client_id} | 
[**get_organization_applications**](OrganizationApi.md#get_organization_applications) | **GET** /api/v1/organization/{orgname}/applications | 
[**get_organization_collaborators**](OrganizationApi.md#get_organization_collaborators) | **GET** /api/v1/organization/{orgname}/collaborators | 
[**get_organization_member**](OrganizationApi.md#get_organization_member) | **GET** /api/v1/organization/{orgname}/members/{membername} | 
[**get_organization_members**](OrganizationApi.md#get_organization_members) | **GET** /api/v1/organization/{orgname}/members | 
[**remove_organization_member**](OrganizationApi.md#remove_organization_member) | **DELETE** /api/v1/organization/{orgname}/members/{membername} | 
[**update_organization_application**](OrganizationApi.md#update_organization_application) | **PUT** /api/v1/organization/{orgname}/applications/{client_id} | 

# **change_organization_details**
> change_organization_details(body, orgname)



Change the details for the specified organization.

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
api_instance = quay.OrganizationApi(quay.ApiClient(configuration))
body = quay.UpdateOrg() # UpdateOrg | Request body contents.
orgname = 'orgname_example' # str | The name of the organization

try:
    api_instance.change_organization_details(body, orgname)
except ApiException as e:
    print("Exception when calling OrganizationApi->change_organization_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOrg**](UpdateOrg.md)| Request body contents. | 
 **orgname** | **str**| The name of the organization | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization**
> create_organization(body)



Create a new organization.

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
api_instance = quay.OrganizationApi(quay.ApiClient(configuration))
body = quay.NewOrg() # NewOrg | Request body contents.

try:
    api_instance.create_organization(body)
except ApiException as e:
    print("Exception when calling OrganizationApi->create_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewOrg**](NewOrg.md)| Request body contents. | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_application**
> create_organization_application(body, orgname)



Creates a new application under this organization.

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
api_instance = quay.OrganizationApi(quay.ApiClient(configuration))
body = quay.NewApp() # NewApp | Request body contents.
orgname = 'orgname_example' # str | The name of the organization

try:
    api_instance.create_organization_application(body, orgname)
except ApiException as e:
    print("Exception when calling OrganizationApi->create_organization_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewApp**](NewApp.md)| Request body contents. | 
 **orgname** | **str**| The name of the organization | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_admined_organization**
> delete_admined_organization(orgname)



Deletes the specified organization.

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
api_instance = quay.OrganizationApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization

try:
    api_instance.delete_admined_organization(orgname)
except ApiException as e:
    print("Exception when calling OrganizationApi->delete_admined_organization: %s\n" % e)
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

# **delete_organization_application**
> delete_organization_application(orgname, client_id)



Deletes the application under this organization.

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
api_instance = quay.OrganizationApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
client_id = 'client_id_example' # str | The OAuth client ID

try:
    api_instance.delete_organization_application(orgname, client_id)
except ApiException as e:
    print("Exception when calling OrganizationApi->delete_organization_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **client_id** | **str**| The OAuth client ID | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_information**
> get_application_information(client_id)



Get information on the specified application.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = quay.OrganizationApi()
client_id = 'client_id_example' # str | The OAuth client ID

try:
    api_instance.get_application_information(client_id)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_application_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The OAuth client ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> get_organization(orgname)



Get the details for the specified organization.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = quay.OrganizationApi()
orgname = 'orgname_example' # str | The name of the organization

try:
    api_instance.get_organization(orgname)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_application**
> get_organization_application(orgname, client_id)



Retrieves the application with the specified client_id under the specified organization.

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
api_instance = quay.OrganizationApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
client_id = 'client_id_example' # str | The OAuth client ID

try:
    api_instance.get_organization_application(orgname, client_id)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organization_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **client_id** | **str**| The OAuth client ID | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_applications**
> get_organization_applications(orgname)



List the applications for the specified organization.

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
api_instance = quay.OrganizationApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization

try:
    api_instance.get_organization_applications(orgname)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organization_applications: %s\n" % e)
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

# **get_organization_collaborators**
> get_organization_collaborators(orgname)



List outside collaborators of the specified organization.

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
api_instance = quay.OrganizationApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization

try:
    api_instance.get_organization_collaborators(orgname)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organization_collaborators: %s\n" % e)
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

# **get_organization_member**
> get_organization_member(orgname, membername)



Retrieves the details of a member of the organization.

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
api_instance = quay.OrganizationApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
membername = 'membername_example' # str | The username of the organization member

try:
    api_instance.get_organization_member(orgname, membername)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organization_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **membername** | **str**| The username of the organization member | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_members**
> get_organization_members(orgname)



List the human members of the specified organization.

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
api_instance = quay.OrganizationApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization

try:
    api_instance.get_organization_members(orgname)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organization_members: %s\n" % e)
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

# **remove_organization_member**
> remove_organization_member(orgname, membername)



Removes a member from an organization, revoking all its repository priviledges and removing         it from all teams in the organization.

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
api_instance = quay.OrganizationApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
membername = 'membername_example' # str | The username of the organization member

try:
    api_instance.remove_organization_member(orgname, membername)
except ApiException as e:
    print("Exception when calling OrganizationApi->remove_organization_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **membername** | **str**| The username of the organization member | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_application**
> update_organization_application(body, orgname, client_id)



Updates an application under this organization.

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
api_instance = quay.OrganizationApi(quay.ApiClient(configuration))
body = quay.UpdateApp() # UpdateApp | Request body contents.
orgname = 'orgname_example' # str | The name of the organization
client_id = 'client_id_example' # str | The OAuth client ID

try:
    api_instance.update_organization_application(body, orgname, client_id)
except ApiException as e:
    print("Exception when calling OrganizationApi->update_organization_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateApp**](UpdateApp.md)| Request body contents. | 
 **orgname** | **str**| The name of the organization | 
 **client_id** | **str**| The OAuth client ID | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

