# PaginatedFeedList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Feed]**](Feed.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_feed_list import PaginatedFeedList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFeedList from a JSON string
paginated_feed_list_instance = PaginatedFeedList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFeedList.to_json())

# convert the object into a dict
paginated_feed_list_dict = paginated_feed_list_instance.to_dict()
# create an instance of PaginatedFeedList from a dict
paginated_feed_list_from_dict = PaginatedFeedList.from_dict(paginated_feed_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


