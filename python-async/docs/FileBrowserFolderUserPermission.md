# FileBrowserFolderUserPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**permission** | [**PermissionEnum**](PermissionEnum.md) |  | [optional] 
**folder_id** | **int** |  | [readonly] 
**folder_path** | **str** |  | [readonly] 
**user_id** | **int** |  | [readonly] 
**user_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**folder** | **str** |  | [readonly] 
**user** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.file_browser_folder_user_permission import FileBrowserFolderUserPermission

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserFolderUserPermission from a JSON string
file_browser_folder_user_permission_instance = FileBrowserFolderUserPermission.from_json(json)
# print the JSON string representation of the object
print(FileBrowserFolderUserPermission.to_json())

# convert the object into a dict
file_browser_folder_user_permission_dict = file_browser_folder_user_permission_instance.to_dict()
# create an instance of FileBrowserFolderUserPermission from a dict
file_browser_folder_user_permission_from_dict = FileBrowserFolderUserPermission.from_dict(file_browser_folder_user_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


