# FileBrowserFileUserPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**permission** | [**PermissionEnum**](PermissionEnum.md) |  | [optional] 
**file_id** | **int** |  | [readonly] 
**file_fname** | **str** |  | [readonly] 
**user_id** | **int** |  | [readonly] 
**user_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**file** | **str** |  | [readonly] 
**user** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.file_browser_file_user_permission import FileBrowserFileUserPermission

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserFileUserPermission from a JSON string
file_browser_file_user_permission_instance = FileBrowserFileUserPermission.from_json(json)
# print the JSON string representation of the object
print(FileBrowserFileUserPermission.to_json())

# convert the object into a dict
file_browser_file_user_permission_dict = file_browser_file_user_permission_instance.to_dict()
# create an instance of FileBrowserFileUserPermission from a dict
file_browser_file_user_permission_from_dict = FileBrowserFileUserPermission.from_dict(file_browser_file_user_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


