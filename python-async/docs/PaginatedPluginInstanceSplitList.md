# PaginatedPluginInstanceSplitList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PluginInstanceSplit]**](PluginInstanceSplit.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_plugin_instance_split_list import PaginatedPluginInstanceSplitList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPluginInstanceSplitList from a JSON string
paginated_plugin_instance_split_list_instance = PaginatedPluginInstanceSplitList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPluginInstanceSplitList.to_json())

# convert the object into a dict
paginated_plugin_instance_split_list_dict = paginated_plugin_instance_split_list_instance.to_dict()
# create an instance of PaginatedPluginInstanceSplitList from a dict
paginated_plugin_instance_split_list_from_dict = PaginatedPluginInstanceSplitList.from_dict(paginated_plugin_instance_split_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


