# FileBrowserFolderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 

## Example

```python
from chris_oag.models.file_browser_folder_request import FileBrowserFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserFolderRequest from a JSON string
file_browser_folder_request_instance = FileBrowserFolderRequest.from_json(json)
# print the JSON string representation of the object
print(FileBrowserFolderRequest.to_json())

# convert the object into a dict
file_browser_folder_request_dict = file_browser_folder_request_instance.to_dict()
# create an instance of FileBrowserFolderRequest from a dict
file_browser_folder_request_from_dict = FileBrowserFolderRequest.from_dict(file_browser_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


