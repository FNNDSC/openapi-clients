# PaginatedPartialPluginInstanceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PartialPluginInstance]**](PartialPluginInstance.md) |  | 

## Example

```python
from aiochris_oag.models.paginated_partial_plugin_instance_list import PaginatedPartialPluginInstanceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPartialPluginInstanceList from a JSON string
paginated_partial_plugin_instance_list_instance = PaginatedPartialPluginInstanceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPartialPluginInstanceList.to_json())

# convert the object into a dict
paginated_partial_plugin_instance_list_dict = paginated_partial_plugin_instance_list_instance.to_dict()
# create an instance of PaginatedPartialPluginInstanceList from a dict
paginated_partial_plugin_instance_list_from_dict = PaginatedPartialPluginInstanceList.from_dict(paginated_partial_plugin_instance_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


