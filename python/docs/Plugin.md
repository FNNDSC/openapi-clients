# Plugin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**name** | **str** |  | [readonly] 
**version** | **str** |  | 
**dock_image** | **str** |  | 
**public_repo** | **str** |  | [readonly] 
**icon** | **str** |  | [readonly] 
**type** | [**PluginType**](PluginType.md) |  | [readonly] 
**stars** | **int** |  | [readonly] 
**authors** | **str** |  | [readonly] 
**title** | **str** |  | [readonly] 
**category** | **str** |  | [readonly] 
**description** | **str** |  | [optional] 
**documentation** | **str** |  | [readonly] 
**license** | **str** |  | [readonly] 
**execshell** | **str** |  | 
**selfpath** | **str** |  | 
**selfexec** | **str** |  | 
**min_number_of_workers** | **int** |  | [optional] 
**max_number_of_workers** | **int** |  | [optional] 
**min_cpu_limit** | **int** |  | [optional] 
**max_cpu_limit** | **int** |  | [optional] 
**min_memory_limit** | **int** |  | [optional] 
**max_memory_limit** | **int** |  | [optional] 
**min_gpu_limit** | **int** |  | [optional] 
**max_gpu_limit** | **int** |  | [optional] 
**meta** | **str** |  | [readonly] 
**parameters** | **str** |  | [readonly] 
**instances** | **str** |  | [readonly] 
**compute_resources** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.plugin import Plugin

# TODO update the JSON string below
json = "{}"
# create an instance of Plugin from a JSON string
plugin_instance = Plugin.from_json(json)
# print the JSON string representation of the object
print(Plugin.to_json())

# convert the object into a dict
plugin_dict = plugin_instance.to_dict()
# create an instance of Plugin from a dict
plugin_from_dict = Plugin.from_dict(plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


