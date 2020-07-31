# quay.LogsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_org_logs**](LogsApi.md#export_org_logs) | **POST** /api/v1/organization/{orgname}/exportlogs | 
[**export_repo_logs**](LogsApi.md#export_repo_logs) | **POST** /api/v1/repository/{repository}/exportlogs | 
[**export_user_logs**](LogsApi.md#export_user_logs) | **POST** /api/v1/user/exportlogs | 
[**get_aggregate_org_logs**](LogsApi.md#get_aggregate_org_logs) | **GET** /api/v1/organization/{orgname}/aggregatelogs | 
[**get_aggregate_repo_logs**](LogsApi.md#get_aggregate_repo_logs) | **GET** /api/v1/repository/{repository}/aggregatelogs | 
[**get_aggregate_user_logs**](LogsApi.md#get_aggregate_user_logs) | **GET** /api/v1/user/aggregatelogs | 
[**list_org_logs**](LogsApi.md#list_org_logs) | **GET** /api/v1/organization/{orgname}/logs | 
[**list_repo_logs**](LogsApi.md#list_repo_logs) | **GET** /api/v1/repository/{repository}/logs | 
[**list_user_logs**](LogsApi.md#list_user_logs) | **GET** /api/v1/user/logs | 

# **export_org_logs**
> export_org_logs(body, orgname, endtime=endtime, starttime=starttime)



Exports the logs for the specified organization.

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
api_instance = quay.LogsApi(quay.ApiClient(configuration))
body = quay.ExportLogs() # ExportLogs | Request body contents.
orgname = 'orgname_example' # str | The name of the organization
endtime = 'endtime_example' # str | Latest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)
starttime = 'starttime_example' # str | Earliest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)

try:
    api_instance.export_org_logs(body, orgname, endtime=endtime, starttime=starttime)
except ApiException as e:
    print("Exception when calling LogsApi->export_org_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportLogs**](ExportLogs.md)| Request body contents. | 
 **orgname** | **str**| The name of the organization | 
 **endtime** | **str**| Latest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 
 **starttime** | **str**| Earliest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_repo_logs**
> export_repo_logs(body, repository, endtime=endtime, starttime=starttime)



Queues an export of the logs for the specified repository.

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
api_instance = quay.LogsApi(quay.ApiClient(configuration))
body = quay.ExportLogs() # ExportLogs | Request body contents.
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
endtime = 'endtime_example' # str | Latest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)
starttime = 'starttime_example' # str | Earliest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)

try:
    api_instance.export_repo_logs(body, repository, endtime=endtime, starttime=starttime)
except ApiException as e:
    print("Exception when calling LogsApi->export_repo_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportLogs**](ExportLogs.md)| Request body contents. | 
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **endtime** | **str**| Latest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 
 **starttime** | **str**| Earliest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_user_logs**
> export_user_logs(body, endtime=endtime, starttime=starttime)



Returns the aggregated logs for the current user.

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
api_instance = quay.LogsApi(quay.ApiClient(configuration))
body = quay.ExportLogs() # ExportLogs | Request body contents.
endtime = 'endtime_example' # str | Latest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)
starttime = 'starttime_example' # str | Earliest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)

try:
    api_instance.export_user_logs(body, endtime=endtime, starttime=starttime)
except ApiException as e:
    print("Exception when calling LogsApi->export_user_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportLogs**](ExportLogs.md)| Request body contents. | 
 **endtime** | **str**| Latest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 
 **starttime** | **str**| Earliest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregate_org_logs**
> get_aggregate_org_logs(orgname, performer=performer, endtime=endtime, starttime=starttime)



Gets the aggregated logs for the specified organization.

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
api_instance = quay.LogsApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
performer = 'performer_example' # str | Username for which to filter logs. (optional)
endtime = 'endtime_example' # str | Latest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)
starttime = 'starttime_example' # str | Earliest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)

try:
    api_instance.get_aggregate_org_logs(orgname, performer=performer, endtime=endtime, starttime=starttime)
except ApiException as e:
    print("Exception when calling LogsApi->get_aggregate_org_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **performer** | **str**| Username for which to filter logs. | [optional] 
 **endtime** | **str**| Latest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 
 **starttime** | **str**| Earliest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregate_repo_logs**
> get_aggregate_repo_logs(repository, endtime=endtime, starttime=starttime)



Returns the aggregated logs for the specified repository.

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
api_instance = quay.LogsApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
endtime = 'endtime_example' # str | Latest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)
starttime = 'starttime_example' # str | Earliest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)

try:
    api_instance.get_aggregate_repo_logs(repository, endtime=endtime, starttime=starttime)
except ApiException as e:
    print("Exception when calling LogsApi->get_aggregate_repo_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **endtime** | **str**| Latest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 
 **starttime** | **str**| Earliest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregate_user_logs**
> get_aggregate_user_logs(performer=performer, endtime=endtime, starttime=starttime)



Returns the aggregated logs for the current user.

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
api_instance = quay.LogsApi(quay.ApiClient(configuration))
performer = 'performer_example' # str | Username for which to filter logs. (optional)
endtime = 'endtime_example' # str | Latest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)
starttime = 'starttime_example' # str | Earliest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)

try:
    api_instance.get_aggregate_user_logs(performer=performer, endtime=endtime, starttime=starttime)
except ApiException as e:
    print("Exception when calling LogsApi->get_aggregate_user_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performer** | **str**| Username for which to filter logs. | [optional] 
 **endtime** | **str**| Latest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 
 **starttime** | **str**| Earliest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_org_logs**
> list_org_logs(orgname, next_page=next_page, performer=performer, endtime=endtime, starttime=starttime)



List the logs for the specified organization.

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
api_instance = quay.LogsApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
next_page = 'next_page_example' # str | The page token for the next page (optional)
performer = 'performer_example' # str | Username for which to filter logs. (optional)
endtime = 'endtime_example' # str | Latest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)
starttime = 'starttime_example' # str | Earliest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)

try:
    api_instance.list_org_logs(orgname, next_page=next_page, performer=performer, endtime=endtime, starttime=starttime)
except ApiException as e:
    print("Exception when calling LogsApi->list_org_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **next_page** | **str**| The page token for the next page | [optional] 
 **performer** | **str**| Username for which to filter logs. | [optional] 
 **endtime** | **str**| Latest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 
 **starttime** | **str**| Earliest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repo_logs**
> list_repo_logs(repository, next_page=next_page, endtime=endtime, starttime=starttime)



List the logs for the specified repository.

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
api_instance = quay.LogsApi(quay.ApiClient(configuration))
repository = 'repository_example' # str | The full path of the repository. e.g. namespace/name
next_page = 'next_page_example' # str | The page token for the next page (optional)
endtime = 'endtime_example' # str | Latest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)
starttime = 'starttime_example' # str | Earliest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)

try:
    api_instance.list_repo_logs(repository, next_page=next_page, endtime=endtime, starttime=starttime)
except ApiException as e:
    print("Exception when calling LogsApi->list_repo_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| The full path of the repository. e.g. namespace/name | 
 **next_page** | **str**| The page token for the next page | [optional] 
 **endtime** | **str**| Latest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 
 **starttime** | **str**| Earliest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_logs**
> list_user_logs(next_page=next_page, performer=performer, endtime=endtime, starttime=starttime)



List the logs for the current user.

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
api_instance = quay.LogsApi(quay.ApiClient(configuration))
next_page = 'next_page_example' # str | The page token for the next page (optional)
performer = 'performer_example' # str | Username for which to filter logs. (optional)
endtime = 'endtime_example' # str | Latest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)
starttime = 'starttime_example' # str | Earliest time for logs. Format: \"%m/%d/%Y\" in UTC. (optional)

try:
    api_instance.list_user_logs(next_page=next_page, performer=performer, endtime=endtime, starttime=starttime)
except ApiException as e:
    print("Exception when calling LogsApi->list_user_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | **str**| The page token for the next page | [optional] 
 **performer** | **str**| Username for which to filter logs. | [optional] 
 **endtime** | **str**| Latest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 
 **starttime** | **str**| Earliest time for logs. Format: \&quot;%m/%d/%Y\&quot; in UTC. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

