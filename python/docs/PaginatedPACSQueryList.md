# PaginatedPACSQueryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PACSQuery]**](PACSQuery.md) |  | 

## Example

```python
from chris_oag.models.paginated_pacs_query_list import PaginatedPACSQueryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPACSQueryList from a JSON string
paginated_pacs_query_list_instance = PaginatedPACSQueryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPACSQueryList.to_json())

# convert the object into a dict
paginated_pacs_query_list_dict = paginated_pacs_query_list_instance.to_dict()
# create an instance of PaginatedPACSQueryList from a dict
paginated_pacs_query_list_from_dict = PaginatedPACSQueryList.from_dict(paginated_pacs_query_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


