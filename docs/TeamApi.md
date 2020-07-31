# quay.TeamApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_organization_team**](TeamApi.md#delete_organization_team) | **DELETE** /api/v1/organization/{orgname}/team/{teamname} | 
[**delete_organization_team_member**](TeamApi.md#delete_organization_team_member) | **DELETE** /api/v1/organization/{orgname}/team/{teamname}/members/{membername} | 
[**delete_team_member_email_invite**](TeamApi.md#delete_team_member_email_invite) | **DELETE** /api/v1/organization/{orgname}/team/{teamname}/invite/{email} | 
[**get_organization_team_members**](TeamApi.md#get_organization_team_members) | **GET** /api/v1/organization/{orgname}/team/{teamname}/members | 
[**get_organization_team_permissions**](TeamApi.md#get_organization_team_permissions) | **GET** /api/v1/organization/{orgname}/team/{teamname}/permissions | 
[**invite_team_member_email**](TeamApi.md#invite_team_member_email) | **PUT** /api/v1/organization/{orgname}/team/{teamname}/invite/{email} | 
[**update_organization_team**](TeamApi.md#update_organization_team) | **PUT** /api/v1/organization/{orgname}/team/{teamname} | 
[**update_organization_team_member**](TeamApi.md#update_organization_team_member) | **PUT** /api/v1/organization/{orgname}/team/{teamname}/members/{membername} | 

# **delete_organization_team**
> delete_organization_team(orgname, teamname)



Delete the specified team.

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
api_instance = quay.TeamApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
teamname = 'teamname_example' # str | The name of the team

try:
    api_instance.delete_organization_team(orgname, teamname)
except ApiException as e:
    print("Exception when calling TeamApi->delete_organization_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **teamname** | **str**| The name of the team | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_team_member**
> delete_organization_team_member(orgname, membername, teamname)



Delete a member of a team.          If the user is merely invited to join the team, then the invite is removed instead.

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
api_instance = quay.TeamApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
membername = 'membername_example' # str | The username of the team member
teamname = 'teamname_example' # str | The name of the team

try:
    api_instance.delete_organization_team_member(orgname, membername, teamname)
except ApiException as e:
    print("Exception when calling TeamApi->delete_organization_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **membername** | **str**| The username of the team member | 
 **teamname** | **str**| The name of the team | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_member_email_invite**
> delete_team_member_email_invite(orgname, email, teamname)



Delete an invite of an email address to join a team.

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
api_instance = quay.TeamApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | 
email = 'email_example' # str | 
teamname = 'teamname_example' # str | 

try:
    api_instance.delete_team_member_email_invite(orgname, email, teamname)
except ApiException as e:
    print("Exception when calling TeamApi->delete_team_member_email_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**|  | 
 **email** | **str**|  | 
 **teamname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_team_members**
> get_organization_team_members(orgname, teamname, include_pending=include_pending)



Retrieve the list of members for the specified team.

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
api_instance = quay.TeamApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
teamname = 'teamname_example' # str | The name of the team
include_pending = true # bool | Whether to include pending members (optional)

try:
    api_instance.get_organization_team_members(orgname, teamname, include_pending=include_pending)
except ApiException as e:
    print("Exception when calling TeamApi->get_organization_team_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **teamname** | **str**| The name of the team | 
 **include_pending** | **bool**| Whether to include pending members | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_team_permissions**
> get_organization_team_permissions(orgname, teamname)



Returns the list of repository permissions for the org's team.

### Example
```python
from __future__ import print_function
import time
import quay
from quay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = quay.TeamApi()
orgname = 'orgname_example' # str | The name of the organization
teamname = 'teamname_example' # str | The name of the team

try:
    api_instance.get_organization_team_permissions(orgname, teamname)
except ApiException as e:
    print("Exception when calling TeamApi->get_organization_team_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **teamname** | **str**| The name of the team | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_team_member_email**
> invite_team_member_email(orgname, email, teamname)



Invites an email address to an existing team.

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
api_instance = quay.TeamApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | 
email = 'email_example' # str | 
teamname = 'teamname_example' # str | 

try:
    api_instance.invite_team_member_email(orgname, email, teamname)
except ApiException as e:
    print("Exception when calling TeamApi->invite_team_member_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**|  | 
 **email** | **str**|  | 
 **teamname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_team**
> update_organization_team(body, orgname, teamname)



Update the org-wide permission for the specified team.

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
api_instance = quay.TeamApi(quay.ApiClient(configuration))
body = quay.TeamDescription() # TeamDescription | Request body contents.
orgname = 'orgname_example' # str | The name of the organization
teamname = 'teamname_example' # str | The name of the team

try:
    api_instance.update_organization_team(body, orgname, teamname)
except ApiException as e:
    print("Exception when calling TeamApi->update_organization_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamDescription**](TeamDescription.md)| Request body contents. | 
 **orgname** | **str**| The name of the organization | 
 **teamname** | **str**| The name of the team | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_team_member**
> update_organization_team_member(orgname, membername, teamname)



Adds or invites a member to an existing team.

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
api_instance = quay.TeamApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
membername = 'membername_example' # str | The username of the team member
teamname = 'teamname_example' # str | The name of the team

try:
    api_instance.update_organization_team_member(orgname, membername, teamname)
except ApiException as e:
    print("Exception when calling TeamApi->update_organization_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **membername** | **str**| The username of the team member | 
 **teamname** | **str**| The name of the team | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

