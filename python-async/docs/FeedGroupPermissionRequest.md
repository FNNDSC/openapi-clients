# FeedGroupPermissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grp_name** | **str** |  | 

## Example

```python
from aiochris_oag.models.feed_group_permission_request import FeedGroupPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeedGroupPermissionRequest from a JSON string
feed_group_permission_request_instance = FeedGroupPermissionRequest.from_json(json)
# print the JSON string representation of the object
print(FeedGroupPermissionRequest.to_json())

# convert the object into a dict
feed_group_permission_request_dict = feed_group_permission_request_instance.to_dict()
# create an instance of FeedGroupPermissionRequest from a dict
feed_group_permission_request_from_dict = FeedGroupPermissionRequest.from_dict(feed_group_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


