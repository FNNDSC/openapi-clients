# PaginatedPluginParameterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PluginParameter]**](PluginParameter.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_plugin_parameter_list import PaginatedPluginParameterList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPluginParameterList from a JSON string
paginated_plugin_parameter_list_instance = PaginatedPluginParameterList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPluginParameterList.to_json())

# convert the object into a dict
paginated_plugin_parameter_list_dict = paginated_plugin_parameter_list_instance.to_dict()
# create an instance of PaginatedPluginParameterList from a dict
paginated_plugin_parameter_list_from_dict = PaginatedPluginParameterList.from_dict(paginated_plugin_parameter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


