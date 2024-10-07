# PluginInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**compute_resource_name** | **str** |  | [optional] 
**status** | [**StatusEnum**](StatusEnum.md) |  | [optional] 
**cpu_limit** | **int** |  | [optional] 
**memory_limit** | **int** |  | [optional] 
**number_of_workers** | **int** |  | [optional] 
**gpu_limit** | **int** |  | [optional] 
**previous_id** | **int** |  | [optional] 

## Example

```python
from chris_oag.models.plugin_instance_request import PluginInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PluginInstanceRequest from a JSON string
plugin_instance_request_instance = PluginInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(PluginInstanceRequest.to_json())

# convert the object into a dict
plugin_instance_request_dict = plugin_instance_request_instance.to_dict()
# create an instance of PluginInstanceRequest from a dict
plugin_instance_request_from_dict = PluginInstanceRequest.from_dict(plugin_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


