# PluginInstance


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
**status** | [**StatusEnum**](StatusEnum.md) |  | [optional] 
**pipeline_id** | **int** |  | [readonly] 
**pipeline_name** | **str** |  | [readonly] 
**workflow_id** | **int** |  | [readonly] 
**summary** | **str** |  | [readonly] 
**raw** | **str** |  | [readonly] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**cpu_limit** | **int** |  | [optional] 
**memory_limit** | **int** |  | [optional] 
**number_of_workers** | **int** |  | [optional] 
**gpu_limit** | **int** |  | [optional] 
**size** | **int** |  | [readonly] 
**error_code** | **str** |  | [readonly] 
**output_folder** | **str** |  | [readonly] 
**previous** | **str** |  | [readonly] 
**feed** | **str** |  | [readonly] 
**plugin** | **str** |  | [readonly] 
**workflow** | **str** |  | [readonly] 
**compute_resource** | **str** |  | [readonly] 
**descendants** | **str** |  | [readonly] 
**parameters** | **str** |  | [readonly] 
**splits** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.plugin_instance import PluginInstance

# TODO update the JSON string below
json = "{}"
# create an instance of PluginInstance from a JSON string
plugin_instance_instance = PluginInstance.from_json(json)
# print the JSON string representation of the object
print(PluginInstance.to_json())

# convert the object into a dict
plugin_instance_dict = plugin_instance_instance.to_dict()
# create an instance of PluginInstance from a dict
plugin_instance_from_dict = PluginInstance.from_dict(plugin_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


