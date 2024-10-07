# ComputeResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**modification_date** | **datetime** |  | [readonly] 
**name** | **str** |  | 
**compute_url** | **str** |  | 
**compute_auth_url** | **str** |  | [optional] 
**compute_innetwork** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**max_job_exec_seconds** | **int** |  | [optional] 

## Example

```python
from chris_oag.models.compute_resource import ComputeResource

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeResource from a JSON string
compute_resource_instance = ComputeResource.from_json(json)
# print the JSON string representation of the object
print(ComputeResource.to_json())

# convert the object into a dict
compute_resource_dict = compute_resource_instance.to_dict()
# create an instance of ComputeResource from a dict
compute_resource_from_dict = ComputeResource.from_dict(compute_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


