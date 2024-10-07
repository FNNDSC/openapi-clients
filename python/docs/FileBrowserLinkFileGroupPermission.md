# FileBrowserLinkFileGroupPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**permission** | [**PermissionEnum**](PermissionEnum.md) |  | [optional] 
**link_file_id** | **int** |  | [readonly] 
**link_file_fname** | **str** |  | [readonly] 
**group_id** | **int** |  | [readonly] 
**group_name** | **str** |  | [readonly] 
**link_file** | **str** |  | [readonly] 
**group** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.file_browser_link_file_group_permission import FileBrowserLinkFileGroupPermission

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserLinkFileGroupPermission from a JSON string
file_browser_link_file_group_permission_instance = FileBrowserLinkFileGroupPermission.from_json(json)
# print the JSON string representation of the object
print(FileBrowserLinkFileGroupPermission.to_json())

# convert the object into a dict
file_browser_link_file_group_permission_dict = file_browser_link_file_group_permission_instance.to_dict()
# create an instance of FileBrowserLinkFileGroupPermission from a dict
file_browser_link_file_group_permission_from_dict = FileBrowserLinkFileGroupPermission.from_dict(file_browser_link_file_group_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


