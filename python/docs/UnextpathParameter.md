# UnextpathParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**param_name** | **str** |  | [readonly] 
**value** | **str** |  | 
**type** | [**PluginParameterType**](PluginParameterType.md) |  | [readonly] 
**plugin_inst** | **str** |  | [readonly] 
**plugin_param** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.unextpath_parameter import UnextpathParameter

# TODO update the JSON string below
json = "{}"
# create an instance of UnextpathParameter from a JSON string
unextpath_parameter_instance = UnextpathParameter.from_json(json)
# print the JSON string representation of the object
print(UnextpathParameter.to_json())

# convert the object into a dict
unextpath_parameter_dict = unextpath_parameter_instance.to_dict()
# create an instance of UnextpathParameter from a dict
unextpath_parameter_from_dict = UnextpathParameter.from_dict(unextpath_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


