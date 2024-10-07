# WorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**previous_plugin_inst_id** | **int** |  | [optional] 
**nodes_info** | **object** |  | [optional] 

## Example

```python
from chris_oag.models.workflow_request import WorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRequest from a JSON string
workflow_request_instance = WorkflowRequest.from_json(json)
# print the JSON string representation of the object
print(WorkflowRequest.to_json())

# convert the object into a dict
workflow_request_dict = workflow_request_instance.to_dict()
# create an instance of WorkflowRequest from a dict
workflow_request_from_dict = WorkflowRequest.from_dict(workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


