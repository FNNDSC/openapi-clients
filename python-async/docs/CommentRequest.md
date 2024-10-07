# CommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from aiochris_oag.models.comment_request import CommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommentRequest from a JSON string
comment_request_instance = CommentRequest.from_json(json)
# print the JSON string representation of the object
print(CommentRequest.to_json())

# convert the object into a dict
comment_request_dict = comment_request_instance.to_dict()
# create an instance of CommentRequest from a dict
comment_request_from_dict = CommentRequest.from_dict(comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


