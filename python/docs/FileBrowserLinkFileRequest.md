# FileBrowserLinkFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**fname** | **bytearray** |  | [optional] 
**public** | **bool** |  | [optional] 
**new_link_file_path** | **str** |  | [optional] 

## Example

```python
from chris_oag.models.file_browser_link_file_request import FileBrowserLinkFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserLinkFileRequest from a JSON string
file_browser_link_file_request_instance = FileBrowserLinkFileRequest.from_json(json)
# print the JSON string representation of the object
print(FileBrowserLinkFileRequest.to_json())

# convert the object into a dict
file_browser_link_file_request_dict = file_browser_link_file_request_instance.to_dict()
# create an instance of FileBrowserLinkFileRequest from a dict
file_browser_link_file_request_from_dict = FileBrowserLinkFileRequest.from_dict(file_browser_link_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


