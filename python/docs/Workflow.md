# Workflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**title** | **str** |  | [optional] 
**pipeline_id** | **int** |  | [readonly] 
**pipeline_name** | **str** |  | [readonly] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**created_jobs** | **int** | Overriden to get the number of plugin instances in &#39;created&#39; status. | [readonly] 
**waiting_jobs** | **int** | Overriden to get the number of plugin instances in &#39;waiting&#39; status. | [readonly] 
**scheduled_jobs** | **int** | Overriden to get the number of plugin instances in &#39;scheduled&#39; status. | [readonly] 
**started_jobs** | **int** | Overriden to get the number of plugin instances in &#39;started&#39; status. | [readonly] 
**registering_jobs** | **int** | Overriden to get the number of plugin instances in &#39;registeringFiles&#39; status. | [readonly] 
**finished_jobs** | **int** | Overriden to get the number of plugin instances in &#39;finishedSuccessfully&#39; status. | [readonly] 
**errored_jobs** | **int** | Overriden to get the number of plugin instances in &#39;finishedWithError&#39; status. | [readonly] 
**cancelled_jobs** | **int** | Overriden to get the number of plugin instances in &#39;cancelled&#39; status. | [readonly] 
**pipeline** | **str** |  | [readonly] 
**plugin_instances** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.workflow import Workflow

# TODO update the JSON string below
json = "{}"
# create an instance of Workflow from a JSON string
workflow_instance = Workflow.from_json(json)
# print the JSON string representation of the object
print(Workflow.to_json())

# convert the object into a dict
workflow_dict = workflow_instance.to_dict()
# create an instance of Workflow from a dict
workflow_from_dict = Workflow.from_dict(workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


