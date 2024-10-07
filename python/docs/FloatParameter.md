# FloatParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**param_name** | **str** |  | [readonly] 
**value** | **float** |  | 
**type** | [**PluginParameterType**](PluginParameterType.md) |  | [readonly] 
**plugin_inst** | **str** |  | [readonly] 
**plugin_param** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.float_parameter import FloatParameter

# TODO update the JSON string below
json = "{}"
# create an instance of FloatParameter from a JSON string
float_parameter_instance = FloatParameter.from_json(json)
# print the JSON string representation of the object
print(FloatParameter.to_json())

# convert the object into a dict
float_parameter_dict = float_parameter_instance.to_dict()
# create an instance of FloatParameter from a dict
float_parameter_from_dict = FloatParameter.from_dict(float_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


