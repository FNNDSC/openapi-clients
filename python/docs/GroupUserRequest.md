# GroupUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 

## Example

```python
from chris_oag.models.group_user_request import GroupUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupUserRequest from a JSON string
group_user_request_instance = GroupUserRequest.from_json(json)
# print the JSON string representation of the object
print(GroupUserRequest.to_json())

# convert the object into a dict
group_user_request_dict = group_user_request_instance.to_dict()
# create an instance of GroupUserRequest from a dict
group_user_request_from_dict = GroupUserRequest.from_dict(group_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


