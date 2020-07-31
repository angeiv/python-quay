# quay.SuperuserApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_service_key**](SuperuserApi.md#approve_service_key) | **POST** /api/v1/superuser/approvedkeys/{kid} | 
[**change_organization**](SuperuserApi.md#change_organization) | **PUT** /api/v1/superuser/organizations/{name} | 
[**create_install_user**](SuperuserApi.md#create_install_user) | **POST** /api/v1/superuser/users/ | 
[**create_service_key**](SuperuserApi.md#create_service_key) | **POST** /api/v1/superuser/keys | 
[**delete_organization**](SuperuserApi.md#delete_organization) | **DELETE** /api/v1/superuser/organizations/{name} | 
[**delete_service_key**](SuperuserApi.md#delete_service_key) | **DELETE** /api/v1/superuser/keys/{kid} | 
[**get_repo_build_logs_super_user**](SuperuserApi.md#get_repo_build_logs_super_user) | **GET** /api/v1/superuser/{build_uuid}/logs | 
[**get_repo_build_status_super_user**](SuperuserApi.md#get_repo_build_status_super_user) | **GET** /api/v1/superuser/{build_uuid}/status | 
[**get_repo_build_super_user**](SuperuserApi.md#get_repo_build_super_user) | **GET** /api/v1/superuser/{build_uuid}/build | 
[**get_service_key**](SuperuserApi.md#get_service_key) | **GET** /api/v1/superuser/keys/{kid} | 
[**list_all_users**](SuperuserApi.md#list_all_users) | **GET** /api/v1/superuser/users/ | 
[**list_service_keys**](SuperuserApi.md#list_service_keys) | **GET** /api/v1/superuser/keys | 
[**update_service_key**](SuperuserApi.md#update_service_key) | **PUT** /api/v1/superuser/keys/{kid} | 

# **approve_service_key**
> approve_service_key(body, kid)



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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))
body = quay.ApproveServiceKey() # ApproveServiceKey | Request body contents.
kid = 'kid_example' # str | The unique identifier for a service key

try:
    api_instance.approve_service_key(body, kid)
except ApiException as e:
    print("Exception when calling SuperuserApi->approve_service_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApproveServiceKey**](ApproveServiceKey.md)| Request body contents. | 
 **kid** | **str**| The unique identifier for a service key | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_organization**
> change_organization(body, name)



Updates information about the specified user.

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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))
body = quay.UpdateOrg() # UpdateOrg | Request body contents.
name = 'name_example' # str | The name of the organizaton being managed

try:
    api_instance.change_organization(body, name)
except ApiException as e:
    print("Exception when calling SuperuserApi->change_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOrg**](UpdateOrg.md)| Request body contents. | 
 **name** | **str**| The name of the organizaton being managed | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_install_user**
> create_install_user(body)



Creates a new user.

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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))
body = quay.CreateInstallUser() # CreateInstallUser | Request body contents.

try:
    api_instance.create_install_user(body)
except ApiException as e:
    print("Exception when calling SuperuserApi->create_install_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInstallUser**](CreateInstallUser.md)| Request body contents. | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_key**
> create_service_key(body)



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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))
body = quay.CreateServiceKey() # CreateServiceKey | Request body contents.

try:
    api_instance.create_service_key(body)
except ApiException as e:
    print("Exception when calling SuperuserApi->create_service_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateServiceKey**](CreateServiceKey.md)| Request body contents. | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization**
> delete_organization(name)



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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))
name = 'name_example' # str | The name of the organizaton being managed

try:
    api_instance.delete_organization(name)
except ApiException as e:
    print("Exception when calling SuperuserApi->delete_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the organizaton being managed | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_key**
> delete_service_key(kid)



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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))
kid = 'kid_example' # str | The unique identifier for a service key

try:
    api_instance.delete_service_key(kid)
except ApiException as e:
    print("Exception when calling SuperuserApi->delete_service_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kid** | **str**| The unique identifier for a service key | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_build_logs_super_user**
> get_repo_build_logs_super_user(build_uuid)



Return the build logs for the build specified by the build uuid.

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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))
build_uuid = 'build_uuid_example' # str | The UUID of the build

try:
    api_instance.get_repo_build_logs_super_user(build_uuid)
except ApiException as e:
    print("Exception when calling SuperuserApi->get_repo_build_logs_super_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_uuid** | **str**| The UUID of the build | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_build_status_super_user**
> get_repo_build_status_super_user(repository, build_uuid)



Return the status for the builds specified by the build uuids.

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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
build_uuid = 'build_uuid_example' # str | The UUID of the build

try:
    api_instance.get_repo_build_status_super_user(repository, build_uuid)
except ApiException as e:
    print("Exception when calling SuperuserApi->get_repo_build_status_super_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **build_uuid** | **str**| The UUID of the build | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_build_super_user**
> get_repo_build_super_user(repository, build_uuid)



Returns information about a build.

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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
build_uuid = 'build_uuid_example' # str | The UUID of the build

try:
    api_instance.get_repo_build_super_user(repository, build_uuid)
except ApiException as e:
    print("Exception when calling SuperuserApi->get_repo_build_super_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **build_uuid** | **str**| The UUID of the build | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_key**
> get_service_key(kid)



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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))
kid = 'kid_example' # str | The unique identifier for a service key

try:
    api_instance.get_service_key(kid)
except ApiException as e:
    print("Exception when calling SuperuserApi->get_service_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kid** | **str**| The unique identifier for a service key | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_users**
> list_all_users(disabled=disabled)



Returns a list of all users in the system.

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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))
disabled = true # bool | If false, only enabled users will be returned. (optional)

try:
    api_instance.list_all_users(disabled=disabled)
except ApiException as e:
    print("Exception when calling SuperuserApi->list_all_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disabled** | **bool**| If false, only enabled users will be returned. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_keys**
> list_service_keys()



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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))

try:
    api_instance.list_service_keys()
except ApiException as e:
    print("Exception when calling SuperuserApi->list_service_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_key**
> update_service_key(body, kid)



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
api_instance = quay.SuperuserApi(quay.ApiClient(configuration))
body = quay.PutServiceKey() # PutServiceKey | Request body contents.
kid = 'kid_example' # str | The unique identifier for a service key

try:
    api_instance.update_service_key(body, kid)
except ApiException as e:
    print("Exception when calling SuperuserApi->update_service_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutServiceKey**](PutServiceKey.md)| Request body contents. | 
 **kid** | **str**| The unique identifier for a service key | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

