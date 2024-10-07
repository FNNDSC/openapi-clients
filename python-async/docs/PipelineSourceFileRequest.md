# PipelineSourceFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fname** | **bytearray** |  | 
**public** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from aiochris_oag.models.pipeline_source_file_request import PipelineSourceFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineSourceFileRequest from a JSON string
pipeline_source_file_request_instance = PipelineSourceFileRequest.from_json(json)
# print the JSON string representation of the object
print(PipelineSourceFileRequest.to_json())

# convert the object into a dict
pipeline_source_file_request_dict = pipeline_source_file_request_instance.to_dict()
# create an instance of PipelineSourceFileRequest from a dict
pipeline_source_file_request_from_dict = PipelineSourceFileRequest.from_dict(pipeline_source_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


