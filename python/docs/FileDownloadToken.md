# FileDownloadToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**token** | **str** |  | [optional] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**owner** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.file_download_token import FileDownloadToken

# TODO update the JSON string below
json = "{}"
# create an instance of FileDownloadToken from a JSON string
file_download_token_instance = FileDownloadToken.from_json(json)
# print the JSON string representation of the object
print(FileDownloadToken.to_json())

# convert the object into a dict
file_download_token_dict = file_download_token_instance.to_dict()
# create an instance of FileDownloadToken from a dict
file_download_token_from_dict = FileDownloadToken.from_dict(file_download_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


