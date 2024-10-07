# PipelineCustomJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**name** | **str** |  | 
**locked** | **bool** |  | [optional] 
**authors** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**plugin_tree** | **str** | Overriden to get the plugin_tree JSON string. | [readonly] 

## Example

```python
from chris_oag.models.pipeline_custom_json import PipelineCustomJson

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineCustomJson from a JSON string
pipeline_custom_json_instance = PipelineCustomJson.from_json(json)
# print the JSON string representation of the object
print(PipelineCustomJson.to_json())

# convert the object into a dict
pipeline_custom_json_dict = pipeline_custom_json_instance.to_dict()
# create an instance of PipelineCustomJson from a dict
pipeline_custom_json_from_dict = PipelineCustomJson.from_dict(pipeline_custom_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


