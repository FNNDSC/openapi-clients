# PaginatedFileBrowserLinkFileList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FileBrowserLinkFile]**](FileBrowserLinkFile.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_file_browser_link_file_list import PaginatedFileBrowserLinkFileList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFileBrowserLinkFileList from a JSON string
paginated_file_browser_link_file_list_instance = PaginatedFileBrowserLinkFileList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFileBrowserLinkFileList.to_json())

# convert the object into a dict
paginated_file_browser_link_file_list_dict = paginated_file_browser_link_file_list_instance.to_dict()
# create an instance of PaginatedFileBrowserLinkFileList from a dict
paginated_file_browser_link_file_list_from_dict = PaginatedFileBrowserLinkFileList.from_dict(paginated_file_browser_link_file_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


