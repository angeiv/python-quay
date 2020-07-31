# quay.RobotApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_org_robot**](RobotApi.md#create_org_robot) | **PUT** /api/v1/organization/{orgname}/robots/{robot_shortname} | 
[**create_user_robot**](RobotApi.md#create_user_robot) | **PUT** /api/v1/user/robots/{robot_shortname} | 
[**delete_org_robot**](RobotApi.md#delete_org_robot) | **DELETE** /api/v1/organization/{orgname}/robots/{robot_shortname} | 
[**delete_user_robot**](RobotApi.md#delete_user_robot) | **DELETE** /api/v1/user/robots/{robot_shortname} | 
[**get_org_robot**](RobotApi.md#get_org_robot) | **GET** /api/v1/organization/{orgname}/robots/{robot_shortname} | 
[**get_org_robot_permissions**](RobotApi.md#get_org_robot_permissions) | **GET** /api/v1/organization/{orgname}/robots/{robot_shortname}/permissions | 
[**get_org_robots**](RobotApi.md#get_org_robots) | **GET** /api/v1/organization/{orgname}/robots | 
[**get_user_robot**](RobotApi.md#get_user_robot) | **GET** /api/v1/user/robots/{robot_shortname} | 
[**get_user_robot_permissions**](RobotApi.md#get_user_robot_permissions) | **GET** /api/v1/user/robots/{robot_shortname}/permissions | 
[**get_user_robots**](RobotApi.md#get_user_robots) | **GET** /api/v1/user/robots | 
[**regenerate_org_robot_token**](RobotApi.md#regenerate_org_robot_token) | **POST** /api/v1/organization/{orgname}/robots/{robot_shortname}/regenerate | 
[**regenerate_user_robot_token**](RobotApi.md#regenerate_user_robot_token) | **POST** /api/v1/user/robots/{robot_shortname}/regenerate | 

# **create_org_robot**
> create_org_robot(body, orgname, robot_shortname)



Create a new robot in the organization.

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
api_instance = quay.RobotApi(quay.ApiClient(configuration))
body = quay.CreateRobot() # CreateRobot | Request body contents.
orgname = 'orgname_example' # str | The name of the organization
robot_shortname = 'robot_shortname_example' # str | The short name for the robot, without any user or organization prefix

try:
    api_instance.create_org_robot(body, orgname, robot_shortname)
except ApiException as e:
    print("Exception when calling RobotApi->create_org_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRobot**](CreateRobot.md)| Request body contents. | 
 **orgname** | **str**| The name of the organization | 
 **robot_shortname** | **str**| The short name for the robot, without any user or organization prefix | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_robot**
> create_user_robot(body, robot_shortname)



Create a new user robot with the specified name.

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
api_instance = quay.RobotApi(quay.ApiClient(configuration))
body = quay.CreateRobot() # CreateRobot | Request body contents.
robot_shortname = 'robot_shortname_example' # str | The short name for the robot, without any user or organization prefix

try:
    api_instance.create_user_robot(body, robot_shortname)
except ApiException as e:
    print("Exception when calling RobotApi->create_user_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRobot**](CreateRobot.md)| Request body contents. | 
 **robot_shortname** | **str**| The short name for the robot, without any user or organization prefix | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_org_robot**
> delete_org_robot(orgname, robot_shortname)



Delete an existing organization robot.

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
api_instance = quay.RobotApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
robot_shortname = 'robot_shortname_example' # str | The short name for the robot, without any user or organization prefix

try:
    api_instance.delete_org_robot(orgname, robot_shortname)
except ApiException as e:
    print("Exception when calling RobotApi->delete_org_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **robot_shortname** | **str**| The short name for the robot, without any user or organization prefix | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_robot**
> delete_user_robot(robot_shortname)



Delete an existing robot.

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
api_instance = quay.RobotApi(quay.ApiClient(configuration))
robot_shortname = 'robot_shortname_example' # str | The short name for the robot, without any user or organization prefix

try:
    api_instance.delete_user_robot(robot_shortname)
except ApiException as e:
    print("Exception when calling RobotApi->delete_user_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_shortname** | **str**| The short name for the robot, without any user or organization prefix | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_robot**
> get_org_robot(orgname, robot_shortname)



Returns the organization's robot with the specified name.

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
api_instance = quay.RobotApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
robot_shortname = 'robot_shortname_example' # str | The short name for the robot, without any user or organization prefix

try:
    api_instance.get_org_robot(orgname, robot_shortname)
except ApiException as e:
    print("Exception when calling RobotApi->get_org_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **robot_shortname** | **str**| The short name for the robot, without any user or organization prefix | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_robot_permissions**
> get_org_robot_permissions(orgname, robot_shortname)



Returns the list of repository permissions for the org's robot.

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
api_instance = quay.RobotApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
robot_shortname = 'robot_shortname_example' # str | The short name for the robot, without any user or organization prefix

try:
    api_instance.get_org_robot_permissions(orgname, robot_shortname)
except ApiException as e:
    print("Exception when calling RobotApi->get_org_robot_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **robot_shortname** | **str**| The short name for the robot, without any user or organization prefix | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_robots**
> get_org_robots(orgname, limit=limit, token=token, permissions=permissions)



List the organization's robots.

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
api_instance = quay.RobotApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
limit = 56 # int | If specified, the number of robots to return. (optional)
token = true # bool | If false, the robot's token is not returned. (optional)
permissions = true # bool | Whether to include repostories and teams in which the robots have permission. (optional)

try:
    api_instance.get_org_robots(orgname, limit=limit, token=token, permissions=permissions)
except ApiException as e:
    print("Exception when calling RobotApi->get_org_robots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **limit** | **int**| If specified, the number of robots to return. | [optional] 
 **token** | **bool**| If false, the robot&#x27;s token is not returned. | [optional] 
 **permissions** | **bool**| Whether to include repostories and teams in which the robots have permission. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_robot**
> get_user_robot(robot_shortname)



Returns the user's robot with the specified name.

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
api_instance = quay.RobotApi(quay.ApiClient(configuration))
robot_shortname = 'robot_shortname_example' # str | The short name for the robot, without any user or organization prefix

try:
    api_instance.get_user_robot(robot_shortname)
except ApiException as e:
    print("Exception when calling RobotApi->get_user_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_shortname** | **str**| The short name for the robot, without any user or organization prefix | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_robot_permissions**
> get_user_robot_permissions(robot_shortname)



Returns the list of repository permissions for the user's robot.

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
api_instance = quay.RobotApi(quay.ApiClient(configuration))
robot_shortname = 'robot_shortname_example' # str | The short name for the robot, without any user or organization prefix

try:
    api_instance.get_user_robot_permissions(robot_shortname)
except ApiException as e:
    print("Exception when calling RobotApi->get_user_robot_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_shortname** | **str**| The short name for the robot, without any user or organization prefix | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_robots**
> get_user_robots(limit=limit, token=token, permissions=permissions)



List the available robots for the user.

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
api_instance = quay.RobotApi(quay.ApiClient(configuration))
limit = 56 # int | If specified, the number of robots to return. (optional)
token = true # bool | If false, the robot's token is not returned. (optional)
permissions = true # bool | Whether to include repositories and teams in which the robots have permission. (optional)

try:
    api_instance.get_user_robots(limit=limit, token=token, permissions=permissions)
except ApiException as e:
    print("Exception when calling RobotApi->get_user_robots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| If specified, the number of robots to return. | [optional] 
 **token** | **bool**| If false, the robot&#x27;s token is not returned. | [optional] 
 **permissions** | **bool**| Whether to include repositories and teams in which the robots have permission. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_org_robot_token**
> regenerate_org_robot_token(orgname, robot_shortname)



Regenerates the token for an organization robot.

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
api_instance = quay.RobotApi(quay.ApiClient(configuration))
orgname = 'orgname_example' # str | The name of the organization
robot_shortname = 'robot_shortname_example' # str | The short name for the robot, without any user or organization prefix

try:
    api_instance.regenerate_org_robot_token(orgname, robot_shortname)
except ApiException as e:
    print("Exception when calling RobotApi->regenerate_org_robot_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| The name of the organization | 
 **robot_shortname** | **str**| The short name for the robot, without any user or organization prefix | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_user_robot_token**
> regenerate_user_robot_token(robot_shortname)



Regenerates the token for a user's robot.

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
api_instance = quay.RobotApi(quay.ApiClient(configuration))
robot_shortname = 'robot_shortname_example' # str | The short name for the robot, without any user or organization prefix

try:
    api_instance.regenerate_user_robot_token(robot_shortname)
except ApiException as e:
    print("Exception when calling RobotApi->regenerate_user_robot_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_shortname** | **str**| The short name for the robot, without any user or organization prefix | 

### Return type

void (empty response body)

### Authorization

[oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

