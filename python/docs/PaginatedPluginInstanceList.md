# PaginatedPluginInstanceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PluginInstance]**](PluginInstance.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_plugin_instance_list import PaginatedPluginInstanceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPluginInstanceList from a JSON string
paginated_plugin_instance_list_instance = PaginatedPluginInstanceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPluginInstanceList.to_json())

# convert the object into a dict
paginated_plugin_instance_list_dict = paginated_plugin_instance_list_instance.to_dict()
# create an instance of PaginatedPluginInstanceList from a dict
paginated_plugin_instance_list_from_dict = PaginatedPluginInstanceList.from_dict(paginated_plugin_instance_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


