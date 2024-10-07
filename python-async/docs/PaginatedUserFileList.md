# PaginatedUserFileList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UserFile]**](UserFile.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_user_file_list import PaginatedUserFileList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserFileList from a JSON string
paginated_user_file_list_instance = PaginatedUserFileList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserFileList.to_json())

# convert the object into a dict
paginated_user_file_list_dict = paginated_user_file_list_instance.to_dict()
# create an instance of PaginatedUserFileList from a dict
paginated_user_file_list_from_dict = PaginatedUserFileList.from_dict(paginated_user_file_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


