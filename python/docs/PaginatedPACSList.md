# PaginatedPACSList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PACS]**](PACS.md) |  | 

## Example

```python
from chris_oag.models.paginated_pacs_list import PaginatedPACSList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPACSList from a JSON string
paginated_pacs_list_instance = PaginatedPACSList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPACSList.to_json())

# convert the object into a dict
paginated_pacs_list_dict = paginated_pacs_list_instance.to_dict()
# create an instance of PaginatedPACSList from a dict
paginated_pacs_list_from_dict = PaginatedPACSList.from_dict(paginated_pacs_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


