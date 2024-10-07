# FeedUserPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**feed_id** | **int** |  | [readonly] 
**feed_name** | **str** |  | [readonly] 
**user_id** | **int** |  | [readonly] 
**user_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**feed** | **str** |  | [readonly] 
**user** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.feed_user_permission import FeedUserPermission

# TODO update the JSON string below
json = "{}"
# create an instance of FeedUserPermission from a JSON string
feed_user_permission_instance = FeedUserPermission.from_json(json)
# print the JSON string representation of the object
print(FeedUserPermission.to_json())

# convert the object into a dict
feed_user_permission_dict = feed_user_permission_instance.to_dict()
# create an instance of FeedUserPermission from a dict
feed_user_permission_from_dict = FeedUserPermission.from_dict(feed_user_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


