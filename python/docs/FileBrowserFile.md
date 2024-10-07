# FileBrowserFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**fname** | **str** |  | [optional] 
**fsize** | **int** | Get the size of the file in bytes. | [readonly] 
**public** | **bool** |  | [optional] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**file_resource** | **str** | Custom method to get the hyperlink to the actual file resource. | [readonly] 
**parent_folder** | **str** |  | [readonly] 
**group_permissions** | **str** |  | [readonly] 
**user_permissions** | **str** |  | [readonly] 
**owner** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.file_browser_file import FileBrowserFile

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserFile from a JSON string
file_browser_file_instance = FileBrowserFile.from_json(json)
# print the JSON string representation of the object
print(FileBrowserFile.to_json())

# convert the object into a dict
file_browser_file_dict = file_browser_file_instance.to_dict()
# create an instance of FileBrowserFile from a dict
file_browser_file_from_dict = FileBrowserFile.from_dict(file_browser_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


