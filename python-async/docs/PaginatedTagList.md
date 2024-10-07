# PaginatedTagList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Tag]**](Tag.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_tag_list import PaginatedTagList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTagList from a JSON string
paginated_tag_list_instance = PaginatedTagList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTagList.to_json())

# convert the object into a dict
paginated_tag_list_dict = paginated_tag_list_instance.to_dict()
# create an instance of PaginatedTagList from a dict
paginated_tag_list_from_dict = PaginatedTagList.from_dict(paginated_tag_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


