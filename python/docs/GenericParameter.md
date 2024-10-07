# GenericParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Custom method to get the correct url for the serialized object regardless of its type. | [readonly] 
**id** | **int** |  | [readonly] 
**param_name** | **str** |  | [readonly] 
**value** | [**GenericDefaultPipingParameterValue**](GenericDefaultPipingParameterValue.md) |  | 
**type** | [**PluginParameterType**](PluginParameterType.md) |  | [readonly] 
**plugin_inst** | **str** |  | [readonly] 
**plugin_param** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.generic_parameter import GenericParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GenericParameter from a JSON string
generic_parameter_instance = GenericParameter.from_json(json)
# print the JSON string representation of the object
print(GenericParameter.to_json())

# convert the object into a dict
generic_parameter_dict = generic_parameter_instance.to_dict()
# create an instance of GenericParameter from a dict
generic_parameter_from_dict = GenericParameter.from_dict(generic_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


