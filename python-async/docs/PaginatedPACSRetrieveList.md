# PaginatedPACSRetrieveList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PACSRetrieve]**](PACSRetrieve.md) |  | 

## Example

```python
from aiochris_oag.models.paginated_pacs_retrieve_list import PaginatedPACSRetrieveList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPACSRetrieveList from a JSON string
paginated_pacs_retrieve_list_instance = PaginatedPACSRetrieveList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPACSRetrieveList.to_json())

# convert the object into a dict
paginated_pacs_retrieve_list_dict = paginated_pacs_retrieve_list_instance.to_dict()
# create an instance of PaginatedPACSRetrieveList from a dict
paginated_pacs_retrieve_list_from_dict = PaginatedPACSRetrieveList.from_dict(paginated_pacs_retrieve_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


