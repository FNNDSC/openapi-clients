# PACSQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**title** | **str** |  | [optional] 
**query** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | [**PacsQueryStatus**](PacsQueryStatus.md) |  | [readonly] 
**pacs_identifier** | **str** |  | [readonly] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**execute** | **bool** |  | [optional] [default to True]
**result** | **str** |  | [readonly] 
**retrieve_list** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.pacs_query import PACSQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PACSQuery from a JSON string
pacs_query_instance = PACSQuery.from_json(json)
# print the JSON string representation of the object
print(PACSQuery.to_json())

# convert the object into a dict
pacs_query_dict = pacs_query_instance.to_dict()
# create an instance of PACSQuery from a dict
pacs_query_from_dict = PACSQuery.from_dict(pacs_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


