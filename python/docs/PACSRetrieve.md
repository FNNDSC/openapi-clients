# PACSRetrieve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**pacs_query_id** | **int** |  | [readonly] 
**pacs_query_title** | **str** |  | [readonly] 
**query** | **object** |  | [readonly] 
**pacs_identifier** | **str** |  | [readonly] 
**status** | [**PacsQueryStatus**](PacsQueryStatus.md) |  | [readonly] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**result** | **str** |  | [readonly] 
**pacs_query** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.pacs_retrieve import PACSRetrieve

# TODO update the JSON string below
json = "{}"
# create an instance of PACSRetrieve from a JSON string
pacs_retrieve_instance = PACSRetrieve.from_json(json)
# print the JSON string representation of the object
print(PACSRetrieve.to_json())

# convert the object into a dict
pacs_retrieve_dict = pacs_retrieve_instance.to_dict()
# create an instance of PACSRetrieve from a dict
pacs_retrieve_from_dict = PACSRetrieve.from_dict(pacs_retrieve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


