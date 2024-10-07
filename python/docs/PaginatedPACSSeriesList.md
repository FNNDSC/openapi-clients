# PaginatedPACSSeriesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PACSSeries]**](PACSSeries.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_pacs_series_list import PaginatedPACSSeriesList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPACSSeriesList from a JSON string
paginated_pacs_series_list_instance = PaginatedPACSSeriesList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPACSSeriesList.to_json())

# convert the object into a dict
paginated_pacs_series_list_dict = paginated_pacs_series_list_instance.to_dict()
# create an instance of PaginatedPACSSeriesList from a dict
paginated_pacs_series_list_from_dict = PaginatedPACSSeriesList.from_dict(paginated_pacs_series_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


