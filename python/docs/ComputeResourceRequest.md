# ComputeResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**compute_url** | **str** |  | 
**compute_auth_url** | **str** |  | [optional] 
**compute_innetwork** | **bool** |  | [optional] 
**compute_user** | **str** |  | 
**compute_password** | **str** |  | 
**compute_auth_token** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**max_job_exec_seconds** | **int** |  | [optional] 

## Example

```python
from chris_oag.models.compute_resource_request import ComputeResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeResourceRequest from a JSON string
compute_resource_request_instance = ComputeResourceRequest.from_json(json)
# print the JSON string representation of the object
print(ComputeResourceRequest.to_json())

# convert the object into a dict
compute_resource_request_dict = compute_resource_request_instance.to_dict()
# create an instance of ComputeResourceRequest from a dict
compute_resource_request_from_dict = ComputeResourceRequest.from_dict(compute_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


