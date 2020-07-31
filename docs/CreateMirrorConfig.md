# CreateMirrorConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Used to enable or disable synchronizations. | [optional] 
**external_registry_config** | [**UpdateMirrorConfigExternalRegistryConfig**](UpdateMirrorConfigExternalRegistryConfig.md) |  | [optional] 
**sync_start_date** | **str** | Determines the next time this repository is ready for synchronization. | 
**external_reference** | **str** | Location of the external repository. | 
**root_rule** | [**UpdateMirrorConfigRootRule**](UpdateMirrorConfigRootRule.md) |  | 
**sync_interval** | **int** | Number of seconds after next_start_date to begin synchronizing. | 
**robot_username** | **str** | Username of robot which will be used for image pushes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

