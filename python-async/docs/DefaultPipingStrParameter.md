# DefaultPipingStrParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**value** | **str** |  | [optional] 
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
from aiochris_oag.models.default_piping_str_parameter import DefaultPipingStrParameter

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultPipingStrParameter from a JSON string
default_piping_str_parameter_instance = DefaultPipingStrParameter.from_json(json)
# print the JSON string representation of the object
print(DefaultPipingStrParameter.to_json())

# convert the object into a dict
default_piping_str_parameter_dict = default_piping_str_parameter_instance.to_dict()
# create an instance of DefaultPipingStrParameter from a dict
default_piping_str_parameter_from_dict = DefaultPipingStrParameter.from_dict(default_piping_str_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


