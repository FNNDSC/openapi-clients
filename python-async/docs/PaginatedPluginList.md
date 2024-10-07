# PaginatedPluginList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Plugin]**](Plugin.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_plugin_list import PaginatedPluginList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPluginList from a JSON string
paginated_plugin_list_instance = PaginatedPluginList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPluginList.to_json())

# convert the object into a dict
paginated_plugin_list_dict = paginated_plugin_list_instance.to_dict()
# create an instance of PaginatedPluginList from a dict
paginated_plugin_list_from_dict = PaginatedPluginList.from_dict(paginated_plugin_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


