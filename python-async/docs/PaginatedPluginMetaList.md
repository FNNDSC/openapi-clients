# PaginatedPluginMetaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PluginMeta]**](PluginMeta.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_plugin_meta_list import PaginatedPluginMetaList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPluginMetaList from a JSON string
paginated_plugin_meta_list_instance = PaginatedPluginMetaList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPluginMetaList.to_json())

# convert the object into a dict
paginated_plugin_meta_list_dict = paginated_plugin_meta_list_instance.to_dict()
# create an instance of PaginatedPluginMetaList from a dict
paginated_plugin_meta_list_from_dict = PaginatedPluginMetaList.from_dict(paginated_plugin_meta_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


