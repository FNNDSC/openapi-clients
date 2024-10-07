# FileBrowserFolderUserPermissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | [**PermissionEnum**](PermissionEnum.md) |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from aiochris_oag.models.file_browser_folder_user_permission_request import FileBrowserFolderUserPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserFolderUserPermissionRequest from a JSON string
file_browser_folder_user_permission_request_instance = FileBrowserFolderUserPermissionRequest.from_json(json)
# print the JSON string representation of the object
print(FileBrowserFolderUserPermissionRequest.to_json())

# convert the object into a dict
file_browser_folder_user_permission_request_dict = file_browser_folder_user_permission_request_instance.to_dict()
# create an instance of FileBrowserFolderUserPermissionRequest from a dict
file_browser_folder_user_permission_request_from_dict = FileBrowserFolderUserPermissionRequest.from_dict(file_browser_folder_user_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


