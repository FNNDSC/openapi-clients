# PaginatedPACSFileList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PACSFile]**](PACSFile.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_pacs_file_list import PaginatedPACSFileList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPACSFileList from a JSON string
paginated_pacs_file_list_instance = PaginatedPACSFileList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPACSFileList.to_json())

# convert the object into a dict
paginated_pacs_file_list_dict = paginated_pacs_file_list_instance.to_dict()
# create an instance of PaginatedPACSFileList from a dict
paginated_pacs_file_list_from_dict = PaginatedPACSFileList.from_dict(paginated_pacs_file_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


