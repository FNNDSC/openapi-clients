# FileBrowserLinkFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**path** | **str** |  | [optional] 
**fname** | **str** |  | [optional] 
**fsize** | **int** | Get the size of the file in bytes. | [readonly] 
**public** | **bool** |  | [optional] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**file_resource** | **str** | Custom method to get the hyperlink to the actual file resource. | [readonly] 
**linked_folder** | **str** | Custom method to get the hyperlink to the linked folder if the ChRIS link points to a folder. | [readonly] 
**linked_file** | **str** | Custom method to get the hyperlink to the linked file if the ChRIS link points to a file. | [readonly] 
**parent_folder** | **str** |  | [readonly] 
**group_permissions** | **str** |  | [readonly] 
**user_permissions** | **str** |  | [readonly] 
**owner** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.file_browser_link_file import FileBrowserLinkFile

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserLinkFile from a JSON string
file_browser_link_file_instance = FileBrowserLinkFile.from_json(json)
# print the JSON string representation of the object
print(FileBrowserLinkFile.to_json())

# convert the object into a dict
file_browser_link_file_dict = file_browser_link_file_instance.to_dict()
# create an instance of FileBrowserLinkFile from a dict
file_browser_link_file_from_dict = FileBrowserLinkFile.from_dict(file_browser_link_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


