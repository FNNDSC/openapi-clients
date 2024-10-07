# FeedUserPermissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 

## Example

```python
from chris_oag.models.feed_user_permission_request import FeedUserPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeedUserPermissionRequest from a JSON string
feed_user_permission_request_instance = FeedUserPermissionRequest.from_json(json)
# print the JSON string representation of the object
print(FeedUserPermissionRequest.to_json())

# convert the object into a dict
feed_user_permission_request_dict = feed_user_permission_request_instance.to_dict()
# create an instance of FeedUserPermissionRequest from a dict
feed_user_permission_request_from_dict = FeedUserPermissionRequest.from_dict(feed_user_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


