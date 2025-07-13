# PluginInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **String** |  | [readonly]
**id** | **i32** |  | [readonly]
**title** | Option<**String**> |  | [optional]
**previous_id** | **i32** |  | [readonly]
**compute_resource_name** | Option<**String**> |  | [optional]
**plugin_id** | **i32** |  | [readonly]
**plugin_name** | **String** |  | [readonly]
**plugin_version** | **String** |  | [readonly]
**plugin_type** | [**models::PluginType**](PluginType.md) |  | [readonly]
**feed_id** | **i32** |  | [readonly]
**start_date** | **String** |  | [readonly]
**end_date** | **String** |  | [readonly]
**output_path** | **String** |  | [readonly]
**status** | [**models::PluginInstanceStatusEnum**](PluginInstanceStatusEnum.md) |  | [readonly]
**pipeline_id** | **i32** |  | [readonly]
**pipeline_name** | **String** |  | [readonly]
**workflow_id** | **i32** |  | [readonly]
**summary** | **String** |  | [readonly]
**raw** | **String** |  | [readonly]
**owner_username** | **String** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly]
**cpu_limit** | Option<**i32**> |  | [optional]
**memory_limit** | Option<**i32**> |  | [optional]
**number_of_workers** | Option<**i32**> |  | [optional]
**gpu_limit** | Option<**i32**> |  | [optional]
**size** | **i64** |  | [readonly]
**error_code** | **String** |  | [readonly]
**output_folder** | **String** |  | [readonly]
**previous** | **String** |  | [readonly]
**feed** | **String** |  | [readonly]
**plugin** | **String** |  | [readonly]
**workflow** | **String** |  | [readonly]
**compute_resource** | **String** |  | [readonly]
**descendants** | **String** |  | [readonly]
**parameters** | **String** |  | [readonly]
**splits** | **String** |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


