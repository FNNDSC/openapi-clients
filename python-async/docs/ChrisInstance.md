# ChrisInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**name** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**job_id_prefix** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from aiochris_oag.models.chris_instance import ChrisInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ChrisInstance from a JSON string
chris_instance_instance = ChrisInstance.from_json(json)
# print the JSON string representation of the object
print(ChrisInstance.to_json())

# convert the object into a dict
chris_instance_dict = chris_instance_instance.to_dict()
# create an instance of ChrisInstance from a dict
chris_instance_from_dict = ChrisInstance.from_dict(chris_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


