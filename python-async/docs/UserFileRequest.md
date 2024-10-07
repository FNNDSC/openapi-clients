# UserFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_path** | **str** |  | [optional] 
**fname** | **bytearray** |  | [optional] 
**public** | **bool** |  | [optional] 

## Example

```python
from aiochris_oag.models.user_file_request import UserFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserFileRequest from a JSON string
user_file_request_instance = UserFileRequest.from_json(json)
# print the JSON string representation of the object
print(UserFileRequest.to_json())

# convert the object into a dict
user_file_request_dict = user_file_request_instance.to_dict()
# create an instance of UserFileRequest from a dict
user_file_request_from_dict = UserFileRequest.from_dict(user_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


