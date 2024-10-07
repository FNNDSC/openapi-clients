# PaginatedFileBrowserFileGroupPermissionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FileBrowserFileGroupPermission]**](FileBrowserFileGroupPermission.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_file_browser_file_group_permission_list import PaginatedFileBrowserFileGroupPermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFileBrowserFileGroupPermissionList from a JSON string
paginated_file_browser_file_group_permission_list_instance = PaginatedFileBrowserFileGroupPermissionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFileBrowserFileGroupPermissionList.to_json())

# convert the object into a dict
paginated_file_browser_file_group_permission_list_dict = paginated_file_browser_file_group_permission_list_instance.to_dict()
# create an instance of PaginatedFileBrowserFileGroupPermissionList from a dict
paginated_file_browser_file_group_permission_list_from_dict = PaginatedFileBrowserFileGroupPermissionList.from_dict(paginated_file_browser_file_group_permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


