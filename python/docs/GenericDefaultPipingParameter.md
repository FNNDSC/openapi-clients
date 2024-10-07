# GenericDefaultPipingParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Custom method to get the correct url for the serialized object regardless of its type. | [readonly] 
**id** | **int** |  | [readonly] 
**value** | [**GenericDefaultPipingParameterValue**](GenericDefaultPipingParameterValue.md) |  | 
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
from chris_oag.models.generic_default_piping_parameter import GenericDefaultPipingParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GenericDefaultPipingParameter from a JSON string
generic_default_piping_parameter_instance = GenericDefaultPipingParameter.from_json(json)
# print the JSON string representation of the object
print(GenericDefaultPipingParameter.to_json())

# convert the object into a dict
generic_default_piping_parameter_dict = generic_default_piping_parameter_instance.to_dict()
# create an instance of GenericDefaultPipingParameter from a dict
generic_default_piping_parameter_from_dict = GenericDefaultPipingParameter.from_dict(generic_default_piping_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


