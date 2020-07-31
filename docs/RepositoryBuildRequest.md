# RepositoryBuildRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subdirectory** | **str** | Subdirectory in which the Dockerfile can be found. You can only specify this or dockerfile_path | [optional] 
**archive_url** | **str** | The URL of the .tar.gz to build. Must start with \&quot;http\&quot; or \&quot;https\&quot;. | [optional] 
**docker_tags** | **list[str]** | The tags to which the built images will be pushed. If none specified, \&quot;latest\&quot; is used. | [optional] 
**pull_robot** | **str** | Username of a Quay robot account to use as pull credentials | [optional] 
**file_id** | **str** | The file id that was generated when the build spec was uploaded | [optional] 
**context** | **str** | Pass in the context for the dockerfile. This is optional. | [optional] 
**dockerfile_path** | **str** | Path to a dockerfile. You can only specify this or subdirectory. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

