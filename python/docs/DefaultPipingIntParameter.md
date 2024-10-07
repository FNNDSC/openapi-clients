# DefaultPipingIntParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**value** | **int** |  | [optional] 
**type** | [**PluginParameterType**](PluginParameterType.md) |  | [readonly] 
**plugin_piping_id** | **int** |  | [readonly] 
**plugin_piping_title** | **str** |  | [readonly] 
**previous_plugin_piping_id** | **int** |  | [readonly] 
**param_name** | **str** |  | [readonly] 
**param_id** | **int** |  | [readonly] 
**plugin_piping** | **str** |  | [readonly] 
**plugin_name** | **str** |  | [readonly] 
**plugin_version** | **str** |  | [readonly] 
**plugin_id** | **int** |  | [readonly] 
**plugin_param** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.default_piping_int_parameter import DefaultPipingIntParameter

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultPipingIntParameter from a JSON string
default_piping_int_parameter_instance = DefaultPipingIntParameter.from_json(json)
# print the JSON string representation of the object
print(DefaultPipingIntParameter.to_json())

# convert the object into a dict
default_piping_int_parameter_dict = default_piping_int_parameter_instance.to_dict()
# create an instance of DefaultPipingIntParameter from a dict
default_piping_int_parameter_from_dict = DefaultPipingIntParameter.from_dict(default_piping_int_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


