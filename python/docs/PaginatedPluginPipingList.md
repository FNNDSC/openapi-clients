# PaginatedPluginPipingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PluginPiping]**](PluginPiping.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_plugin_piping_list import PaginatedPluginPipingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPluginPipingList from a JSON string
paginated_plugin_piping_list_instance = PaginatedPluginPipingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPluginPipingList.to_json())

# convert the object into a dict
paginated_plugin_piping_list_dict = paginated_plugin_piping_list_instance.to_dict()
# create an instance of PaginatedPluginPipingList from a dict
paginated_plugin_piping_list_from_dict = PaginatedPluginPipingList.from_dict(paginated_plugin_piping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


