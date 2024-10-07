# PathParameter


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
from chris_oag.models.path_parameter import PathParameter

# TODO update the JSON string below
json = "{}"
# create an instance of PathParameter from a JSON string
path_parameter_instance = PathParameter.from_json(json)
# print the JSON string representation of the object
print(PathParameter.to_json())

# convert the object into a dict
path_parameter_dict = path_parameter_instance.to_dict()
# create an instance of PathParameter from a dict
path_parameter_from_dict = PathParameter.from_dict(path_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


