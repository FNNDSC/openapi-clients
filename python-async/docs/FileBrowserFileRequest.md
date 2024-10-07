# FileBrowserFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fname** | **bytearray** |  | [optional] 
**public** | **bool** |  | [optional] 
**new_file_path** | **str** |  | [optional] 

## Example

```python
from aiochris_oag.models.file_browser_file_request import FileBrowserFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileBrowserFileRequest from a JSON string
file_browser_file_request_instance = FileBrowserFileRequest.from_json(json)
# print the JSON string representation of the object
print(FileBrowserFileRequest.to_json())

# convert the object into a dict
file_browser_file_request_dict = file_browser_file_request_instance.to_dict()
# create an instance of FileBrowserFileRequest from a dict
file_browser_file_request_from_dict = FileBrowserFileRequest.from_dict(file_browser_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


