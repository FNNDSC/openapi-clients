# StrParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**param_name** | **str** |  | [readonly] 
**value** | **str** |  | [optional] 
**type** | [**PluginParameterType**](PluginParameterType.md) |  | [readonly] 
**plugin_inst** | **str** |  | [readonly] 
**plugin_param** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.str_parameter import StrParameter

# TODO update the JSON string below
json = "{}"
# create an instance of StrParameter from a JSON string
str_parameter_instance = StrParameter.from_json(json)
# print the JSON string representation of the object
print(StrParameter.to_json())

# convert the object into a dict
str_parameter_dict = str_parameter_instance.to_dict()
# create an instance of StrParameter from a dict
str_parameter_from_dict = StrParameter.from_dict(str_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


