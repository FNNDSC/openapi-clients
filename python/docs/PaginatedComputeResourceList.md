# PaginatedComputeResourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ComputeResource]**](ComputeResource.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_compute_resource_list import PaginatedComputeResourceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedComputeResourceList from a JSON string
paginated_compute_resource_list_instance = PaginatedComputeResourceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedComputeResourceList.to_json())

# convert the object into a dict
paginated_compute_resource_list_dict = paginated_compute_resource_list_instance.to_dict()
# create an instance of PaginatedComputeResourceList from a dict
paginated_compute_resource_list_from_dict = PaginatedComputeResourceList.from_dict(paginated_compute_resource_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


