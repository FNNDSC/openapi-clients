# PaginatedFileBrowserLinkFileUserPermissionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FileBrowserLinkFileUserPermission]**](FileBrowserLinkFileUserPermission.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_file_browser_link_file_user_permission_list import PaginatedFileBrowserLinkFileUserPermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFileBrowserLinkFileUserPermissionList from a JSON string
paginated_file_browser_link_file_user_permission_list_instance = PaginatedFileBrowserLinkFileUserPermissionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFileBrowserLinkFileUserPermissionList.to_json())

# convert the object into a dict
paginated_file_browser_link_file_user_permission_list_dict = paginated_file_browser_link_file_user_permission_list_instance.to_dict()
# create an instance of PaginatedFileBrowserLinkFileUserPermissionList from a dict
paginated_file_browser_link_file_user_permission_list_from_dict = PaginatedFileBrowserLinkFileUserPermissionList.from_dict(paginated_file_browser_link_file_user_permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


