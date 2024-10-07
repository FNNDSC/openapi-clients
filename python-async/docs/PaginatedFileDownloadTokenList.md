# PaginatedFileDownloadTokenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FileDownloadToken]**](FileDownloadToken.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_file_download_token_list import PaginatedFileDownloadTokenList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFileDownloadTokenList from a JSON string
paginated_file_download_token_list_instance = PaginatedFileDownloadTokenList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFileDownloadTokenList.to_json())

# convert the object into a dict
paginated_file_download_token_list_dict = paginated_file_download_token_list_instance.to_dict()
# create an instance of PaginatedFileDownloadTokenList from a dict
paginated_file_download_token_list_from_dict = PaginatedFileDownloadTokenList.from_dict(paginated_file_download_token_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


