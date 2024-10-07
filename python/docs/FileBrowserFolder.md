# FileBrowserFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**path** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**parent** | **str** |  | [readonly] 
**children** | **str** |  | [readonly] 
**files** | **str** |  | [readonly] 
**link_files** | **str** |  | [readonly] 
**group_permissions** | **str** |  | [readonly] 
**user_permissions** | **str** |  | [readonly] 
**owner** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.file_browser_folder import FileBrowserFolder

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserFolder from a JSON string
file_browser_folder_instance = FileBrowserFolder.from_json(json)
# print the JSON string representation of the object
print(FileBrowserFolder.to_json())

# convert the object into a dict
file_browser_folder_dict = file_browser_folder_instance.to_dict()
# create an instance of FileBrowserFolder from a dict
file_browser_folder_from_dict = FileBrowserFolder.from_dict(file_browser_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


