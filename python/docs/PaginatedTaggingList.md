# PaginatedTaggingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Tagging]**](Tagging.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_tagging_list import PaginatedTaggingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTaggingList from a JSON string
paginated_tagging_list_instance = PaginatedTaggingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTaggingList.to_json())

# convert the object into a dict
paginated_tagging_list_dict = paginated_tagging_list_instance.to_dict()
# create an instance of PaginatedTaggingList from a dict
paginated_tagging_list_from_dict = PaginatedTaggingList.from_dict(paginated_tagging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


