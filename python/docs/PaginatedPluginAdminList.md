# PaginatedPluginAdminList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PluginAdmin]**](PluginAdmin.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_plugin_admin_list import PaginatedPluginAdminList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPluginAdminList from a JSON string
paginated_plugin_admin_list_instance = PaginatedPluginAdminList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPluginAdminList.to_json())

# convert the object into a dict
paginated_plugin_admin_list_dict = paginated_plugin_admin_list_instance.to_dict()
# create an instance of PaginatedPluginAdminList from a dict
paginated_plugin_admin_list_from_dict = PaginatedPluginAdminList.from_dict(paginated_plugin_admin_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


