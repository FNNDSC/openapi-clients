# PaginatedFileBrowserFolderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FileBrowserFolder]**](FileBrowserFolder.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_file_browser_folder_list import PaginatedFileBrowserFolderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFileBrowserFolderList from a JSON string
paginated_file_browser_folder_list_instance = PaginatedFileBrowserFolderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFileBrowserFolderList.to_json())

# convert the object into a dict
paginated_file_browser_folder_list_dict = paginated_file_browser_folder_list_instance.to_dict()
# create an instance of PaginatedFileBrowserFolderList from a dict
paginated_file_browser_folder_list_from_dict = PaginatedFileBrowserFolderList.from_dict(paginated_file_browser_folder_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


