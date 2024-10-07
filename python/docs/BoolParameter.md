# BoolParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**param_name** | **str** |  | [readonly] 
**value** | **bool** |  | 
**type** | [**PluginParameterType**](PluginParameterType.md) |  | [readonly] 
**plugin_inst** | **str** |  | [readonly] 
**plugin_param** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.bool_parameter import BoolParameter

# TODO update the JSON string below
json = "{}"
# create an instance of BoolParameter from a JSON string
bool_parameter_instance = BoolParameter.from_json(json)
# print the JSON string representation of the object
print(BoolParameter.to_json())

# convert the object into a dict
bool_parameter_dict = bool_parameter_instance.to_dict()
# create an instance of BoolParameter from a dict
bool_parameter_from_dict = BoolParameter.from_dict(bool_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


