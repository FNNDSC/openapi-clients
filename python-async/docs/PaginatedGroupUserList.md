# PaginatedGroupUserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GroupUser]**](GroupUser.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_group_user_list import PaginatedGroupUserList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupUserList from a JSON string
paginated_group_user_list_instance = PaginatedGroupUserList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGroupUserList.to_json())

# convert the object into a dict
paginated_group_user_list_dict = paginated_group_user_list_instance.to_dict()
# create an instance of PaginatedGroupUserList from a dict
paginated_group_user_list_from_dict = PaginatedGroupUserList.from_dict(paginated_group_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


