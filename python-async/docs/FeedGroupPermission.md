# FeedGroupPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**feed_id** | **int** |  | [readonly] 
**feed_name** | **str** |  | [readonly] 
**group_id** | **int** |  | [readonly] 
**group_name** | **str** |  | [readonly] 
**feed** | **str** |  | [readonly] 
**group** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.feed_group_permission import FeedGroupPermission

# TODO update the JSON string below
json = "{}"
# create an instance of FeedGroupPermission from a JSON string
feed_group_permission_instance = FeedGroupPermission.from_json(json)
# print the JSON string representation of the object
print(FeedGroupPermission.to_json())

# convert the object into a dict
feed_group_permission_dict = feed_group_permission_instance.to_dict()
# create an instance of FeedGroupPermission from a dict
feed_group_permission_from_dict = FeedGroupPermission.from_dict(feed_group_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


