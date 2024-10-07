# FileBrowserFolderGroupPermissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | [**PermissionEnum**](PermissionEnum.md) |  | [optional] 
**grp_name** | **str** |  | [optional] 

## Example

```python
from aiochris_oag.models.file_browser_folder_group_permission_request import FileBrowserFolderGroupPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserFolderGroupPermissionRequest from a JSON string
file_browser_folder_group_permission_request_instance = FileBrowserFolderGroupPermissionRequest.from_json(json)
# print the JSON string representation of the object
print(FileBrowserFolderGroupPermissionRequest.to_json())

# convert the object into a dict
file_browser_folder_group_permission_request_dict = file_browser_folder_group_permission_request_instance.to_dict()
# create an instance of FileBrowserFolderGroupPermissionRequest from a dict
file_browser_folder_group_permission_request_from_dict = FileBrowserFolderGroupPermissionRequest.from_dict(file_browser_folder_group_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


