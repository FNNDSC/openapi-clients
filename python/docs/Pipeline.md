# Pipeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**locked** | **bool** |  | [optional] 
**authors** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**modification_date** | **datetime** |  | [readonly] 
**plugins** | **str** |  | [readonly] 
**plugin_pipings** | **str** |  | [readonly] 
**default_parameters** | **str** |  | [readonly] 
**workflows** | **str** |  | [readonly] 
**json_repr** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.pipeline import Pipeline

# TODO update the JSON string below
json = "{}"
# create an instance of Pipeline from a JSON string
pipeline_instance = Pipeline.from_json(json)
# print the JSON string representation of the object
print(Pipeline.to_json())

# convert the object into a dict
pipeline_dict = pipeline_instance.to_dict()
# create an instance of Pipeline from a dict
pipeline_from_dict = Pipeline.from_dict(pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


