# FileBrowserFolderGroupPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**permission** | [**PermissionEnum**](PermissionEnum.md) |  | [optional] 
**folder_id** | **int** |  | [readonly] 
**folder_path** | **str** |  | [readonly] 
**group_id** | **int** |  | [readonly] 
**group_name** | **str** |  | [readonly] 
**folder** | **str** |  | [readonly] 
**group** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.file_browser_folder_group_permission import FileBrowserFolderGroupPermission

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserFolderGroupPermission from a JSON string
file_browser_folder_group_permission_instance = FileBrowserFolderGroupPermission.from_json(json)
# print the JSON string representation of the object
print(FileBrowserFolderGroupPermission.to_json())

# convert the object into a dict
file_browser_folder_group_permission_dict = file_browser_folder_group_permission_instance.to_dict()
# create an instance of FileBrowserFolderGroupPermission from a dict
file_browser_folder_group_permission_from_dict = FileBrowserFolderGroupPermission.from_dict(file_browser_folder_group_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


