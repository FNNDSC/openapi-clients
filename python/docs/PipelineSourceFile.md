# PipelineSourceFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**fname** | **str** |  | 
**fsize** | **int** | Get the size of the file in bytes. | [readonly] 
**public** | **bool** |  | [optional] 
**ftype** | [**PipelineSourceFileFtype**](PipelineSourceFileFtype.md) |  | 
**uploader_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**pipeline_id** | **int** |  | [readonly] 
**pipeline_name** | **str** |  | [readonly] 
**file_resource** | **str** | Custom method to get the hyperlink to the actual file resource. | [readonly] 
**parent_folder** | **str** |  | [readonly] 
**owner** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.pipeline_source_file import PipelineSourceFile

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineSourceFile from a JSON string
pipeline_source_file_instance = PipelineSourceFile.from_json(json)
# print the JSON string representation of the object
print(PipelineSourceFile.to_json())

# convert the object into a dict
pipeline_source_file_dict = pipeline_source_file_instance.to_dict()
# create an instance of PipelineSourceFile from a dict
pipeline_source_file_from_dict = PipelineSourceFile.from_dict(pipeline_source_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


