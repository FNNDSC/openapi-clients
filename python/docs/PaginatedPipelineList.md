# PaginatedPipelineList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Pipeline]**](Pipeline.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_pipeline_list import PaginatedPipelineList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPipelineList from a JSON string
paginated_pipeline_list_instance = PaginatedPipelineList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPipelineList.to_json())

# convert the object into a dict
paginated_pipeline_list_dict = paginated_pipeline_list_instance.to_dict()
# create an instance of PaginatedPipelineList from a dict
paginated_pipeline_list_from_dict = PaginatedPipelineList.from_dict(paginated_pipeline_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


