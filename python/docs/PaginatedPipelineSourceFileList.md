# PaginatedPipelineSourceFileList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PipelineSourceFile]**](PipelineSourceFile.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_pipeline_source_file_list import PaginatedPipelineSourceFileList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPipelineSourceFileList from a JSON string
paginated_pipeline_source_file_list_instance = PaginatedPipelineSourceFileList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPipelineSourceFileList.to_json())

# convert the object into a dict
paginated_pipeline_source_file_list_dict = paginated_pipeline_source_file_list_instance.to_dict()
# create an instance of PaginatedPipelineSourceFileList from a dict
paginated_pipeline_source_file_list_from_dict = PaginatedPipelineSourceFileList.from_dict(paginated_pipeline_source_file_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


