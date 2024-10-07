# PluginInstanceSplitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** |  | [optional] 
**compute_resource_name** | **str** |  | [optional] 

## Example

```python
from aiochris_oag.models.plugin_instance_split_request import PluginInstanceSplitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PluginInstanceSplitRequest from a JSON string
plugin_instance_split_request_instance = PluginInstanceSplitRequest.from_json(json)
# print the JSON string representation of the object
print(PluginInstanceSplitRequest.to_json())

# convert the object into a dict
plugin_instance_split_request_dict = plugin_instance_split_request_instance.to_dict()
# create an instance of PluginInstanceSplitRequest from a dict
plugin_instance_split_request_from_dict = PluginInstanceSplitRequest.from_dict(plugin_instance_split_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


