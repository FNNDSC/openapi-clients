# PartialPluginInstance

A compact serializer exposing only a small subset of PluginInstance fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**title** | **str** |  | [optional] 
**previous_id** | **int** |  | [readonly] 
**compute_resource_name** | **str** |  | [optional] 
**plugin_id** | **int** |  | [readonly] 
**plugin_name** | **str** |  | [readonly] 
**plugin_version** | **str** |  | [readonly] 
**plugin_type** | [**PluginType**](PluginType.md) |  | [readonly] 
**feed_id** | **int** |  | [readonly] 
**start_date** | **datetime** |  | [readonly] 
**end_date** | **datetime** |  | [readonly] 
**output_path** | **str** |  | [readonly] 
**status** | [**PluginInstanceStatus**](PluginInstanceStatus.md) |  | [readonly] 
**active** | **bool** | Overriden to get the \&quot;active\&quot; status of the plugin instance. | [readonly] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**cpu_limit** | **int** |  | [optional] 
**memory_limit** | **int** |  | [optional] 
**number_of_workers** | **int** |  | [optional] 
**gpu_limit** | **int** |  | [optional] 
**size** | **int** |  | [readonly] 
**error_code** | **str** |  | [readonly] 
**deletion_status** | [**DeletionStatusEnum**](DeletionStatusEnum.md) |  | [optional] 
**deletion_error** | **str** |  | [optional] 
**output_folder** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.partial_plugin_instance import PartialPluginInstance

# TODO update the JSON string below
json = "{}"
# create an instance of PartialPluginInstance from a JSON string
partial_plugin_instance_instance = PartialPluginInstance.from_json(json)
# print the JSON string representation of the object
print(PartialPluginInstance.to_json())

# convert the object into a dict
partial_plugin_instance_dict = partial_plugin_instance_instance.to_dict()
# create an instance of PartialPluginInstance from a dict
partial_plugin_instance_from_dict = PartialPluginInstance.from_dict(partial_plugin_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


