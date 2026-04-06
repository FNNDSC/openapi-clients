# PACS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**identifier** | **str** |  | 
**active** | **bool** |  | [optional] [default to True]
**folder_path** | **str** |  | [readonly] 
**folder** | **str** |  | [readonly] 
**query_list** | **str** |  | [readonly] 
**series_list** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.pacs import PACS

# TODO update the JSON string below
json = "{}"
# create an instance of PACS from a JSON string
pacs_instance = PACS.from_json(json)
# print the JSON string representation of the object
print(PACS.to_json())

# convert the object into a dict
pacs_dict = pacs_instance.to_dict()
# create an instance of PACS from a dict
pacs_from_dict = PACS.from_dict(pacs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


