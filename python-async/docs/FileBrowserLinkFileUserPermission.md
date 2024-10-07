# FileBrowserLinkFileUserPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**permission** | [**PermissionEnum**](PermissionEnum.md) |  | [optional] 
**link_file_id** | **int** |  | [readonly] 
**link_file_fname** | **str** |  | [readonly] 
**user_id** | **int** |  | [readonly] 
**user_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**link_file** | **str** |  | [readonly] 
**user** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.file_browser_link_file_user_permission import FileBrowserLinkFileUserPermission

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserLinkFileUserPermission from a JSON string
file_browser_link_file_user_permission_instance = FileBrowserLinkFileUserPermission.from_json(json)
# print the JSON string representation of the object
print(FileBrowserLinkFileUserPermission.to_json())

# convert the object into a dict
file_browser_link_file_user_permission_dict = file_browser_link_file_user_permission_instance.to_dict()
# create an instance of FileBrowserLinkFileUserPermission from a dict
file_browser_link_file_user_permission_from_dict = FileBrowserLinkFileUserPermission.from_dict(file_browser_link_file_user_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


