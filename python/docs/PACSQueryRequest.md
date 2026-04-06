# PACSQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**query** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**execute** | **bool** |  | [optional] [default to True]

## Example

```python
from chris_oag.models.pacs_query_request import PACSQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PACSQueryRequest from a JSON string
pacs_query_request_instance = PACSQueryRequest.from_json(json)
# print the JSON string representation of the object
print(PACSQueryRequest.to_json())

# convert the object into a dict
pacs_query_request_dict = pacs_query_request_instance.to_dict()
# create an instance of PACSQueryRequest from a dict
pacs_query_request_from_dict = PACSQueryRequest.from_dict(pacs_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


