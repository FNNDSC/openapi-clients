# PaginatedCommentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Comment]**](Comment.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_comment_list import PaginatedCommentList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCommentList from a JSON string
paginated_comment_list_instance = PaginatedCommentList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCommentList.to_json())

# convert the object into a dict
paginated_comment_list_dict = paginated_comment_list_instance.to_dict()
# create an instance of PaginatedCommentList from a dict
paginated_comment_list_from_dict = PaginatedCommentList.from_dict(paginated_comment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


