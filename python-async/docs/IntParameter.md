# IntParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**param_name** | **str** |  | [readonly] 
**value** | **int** |  | 
**type** | [**PluginParameterType**](PluginParameterType.md) |  | [readonly] 
**plugin_inst** | **str** |  | [readonly] 
**plugin_param** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.int_parameter import IntParameter

# TODO update the JSON string below
json = "{}"
# create an instance of IntParameter from a JSON string
int_parameter_instance = IntParameter.from_json(json)
# print the JSON string representation of the object
print(IntParameter.to_json())

# convert the object into a dict
int_parameter_dict = int_parameter_instance.to_dict()
# create an instance of IntParameter from a dict
int_parameter_from_dict = IntParameter.from_dict(int_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


