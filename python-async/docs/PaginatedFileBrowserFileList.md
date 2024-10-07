# PaginatedFileBrowserFileList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FileBrowserFile]**](FileBrowserFile.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_file_browser_file_list import PaginatedFileBrowserFileList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFileBrowserFileList from a JSON string
paginated_file_browser_file_list_instance = PaginatedFileBrowserFileList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFileBrowserFileList.to_json())

# convert the object into a dict
paginated_file_browser_file_list_dict = paginated_file_browser_file_list_instance.to_dict()
# create an instance of PaginatedFileBrowserFileList from a dict
paginated_file_browser_file_list_from_dict = PaginatedFileBrowserFileList.from_dict(paginated_file_browser_file_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


