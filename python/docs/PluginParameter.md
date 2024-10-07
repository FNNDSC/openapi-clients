# PluginParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**type** | [**PluginParameterType**](PluginParameterType.md) |  | [optional] 
**optional** | **bool** |  | [optional] 
**default** | [**PluginParameterDefault**](PluginParameterDefault.md) |  | 
**flag** | **str** |  | 
**short_flag** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**help** | **str** |  | [optional] 
**ui_exposed** | **bool** |  | [optional] 
**plugin** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.plugin_parameter import PluginParameter

# TODO update the JSON string below
json = "{}"
# create an instance of PluginParameter from a JSON string
plugin_parameter_instance = PluginParameter.from_json(json)
# print the JSON string representation of the object
print(PluginParameter.to_json())

# convert the object into a dict
plugin_parameter_dict = plugin_parameter_instance.to_dict()
# create an instance of PluginParameter from a dict
plugin_parameter_from_dict = PluginParameter.from_dict(plugin_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


