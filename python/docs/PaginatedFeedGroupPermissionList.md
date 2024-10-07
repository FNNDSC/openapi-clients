# PaginatedFeedGroupPermissionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FeedGroupPermission]**](FeedGroupPermission.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_feed_group_permission_list import PaginatedFeedGroupPermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFeedGroupPermissionList from a JSON string
paginated_feed_group_permission_list_instance = PaginatedFeedGroupPermissionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFeedGroupPermissionList.to_json())

# convert the object into a dict
paginated_feed_group_permission_list_dict = paginated_feed_group_permission_list_instance.to_dict()
# create an instance of PaginatedFeedGroupPermissionList from a dict
paginated_feed_group_permission_list_from_dict = PaginatedFeedGroupPermissionList.from_dict(paginated_feed_group_permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


