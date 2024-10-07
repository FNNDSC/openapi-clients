# PaginatedFeedUserPermissionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FeedUserPermission]**](FeedUserPermission.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_feed_user_permission_list import PaginatedFeedUserPermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFeedUserPermissionList from a JSON string
paginated_feed_user_permission_list_instance = PaginatedFeedUserPermissionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFeedUserPermissionList.to_json())

# convert the object into a dict
paginated_feed_user_permission_list_dict = paginated_feed_user_permission_list_instance.to_dict()
# create an instance of PaginatedFeedUserPermissionList from a dict
paginated_feed_user_permission_list_from_dict = PaginatedFeedUserPermissionList.from_dict(paginated_feed_user_permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


