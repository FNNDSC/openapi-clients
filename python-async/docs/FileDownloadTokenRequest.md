# FileDownloadTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 

## Example

```python
from aiochris_oag.models.file_download_token_request import FileDownloadTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileDownloadTokenRequest from a JSON string
file_download_token_request_instance = FileDownloadTokenRequest.from_json(json)
# print the JSON string representation of the object
print(FileDownloadTokenRequest.to_json())

# convert the object into a dict
file_download_token_request_dict = file_download_token_request_instance.to_dict()
# create an instance of FileDownloadTokenRequest from a dict
file_download_token_request_from_dict = FileDownloadTokenRequest.from_dict(file_download_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


