# PluginAdminRequest

A Plugin serializer for the PluginAdminList JSON view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**dock_image** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**execshell** | **str** |  | [optional] 
**selfpath** | **str** |  | [optional] 
**selfexec** | **str** |  | [optional] 
**min_number_of_workers** | **int** |  | [optional] 
**max_number_of_workers** | **int** |  | [optional] 
**min_cpu_limit** | **int** |  | [optional] 
**max_cpu_limit** | **int** |  | [optional] 
**min_memory_limit** | **int** |  | [optional] 
**max_memory_limit** | **int** |  | [optional] 
**min_gpu_limit** | **int** |  | [optional] 
**max_gpu_limit** | **int** |  | [optional] 
**fname** | **bytearray** |  | [optional] 
**plugin_store_url** | **str** |  | [optional] 
**compute_names** | **str** |  | 

## Example

```python
from aiochris_oag.models.plugin_admin_request import PluginAdminRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PluginAdminRequest from a JSON string
plugin_admin_request_instance = PluginAdminRequest.from_json(json)
# print the JSON string representation of the object
print(PluginAdminRequest.to_json())

# convert the object into a dict
plugin_admin_request_dict = plugin_admin_request_instance.to_dict()
# create an instance of PluginAdminRequest from a dict
plugin_admin_request_from_dict = PluginAdminRequest.from_dict(plugin_admin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


