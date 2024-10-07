# PipelineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**locked** | **bool** |  | [optional] 
**authors** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**plugin_tree** | **object** |  | [optional] 
**plugin_inst_id** | **int** |  | [optional] 

## Example

```python
from chris_oag.models.pipeline_request import PipelineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineRequest from a JSON string
pipeline_request_instance = PipelineRequest.from_json(json)
# print the JSON string representation of the object
print(PipelineRequest.to_json())

# convert the object into a dict
pipeline_request_dict = pipeline_request_instance.to_dict()
# create an instance of PipelineRequest from a dict
pipeline_request_from_dict = PipelineRequest.from_dict(pipeline_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


