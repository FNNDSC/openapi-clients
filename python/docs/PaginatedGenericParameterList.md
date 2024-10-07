# PaginatedGenericParameterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GenericParameter]**](GenericParameter.md) |  | [optional] 

## Example

```python
from chris_oag.models.paginated_generic_parameter_list import PaginatedGenericParameterList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGenericParameterList from a JSON string
paginated_generic_parameter_list_instance = PaginatedGenericParameterList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGenericParameterList.to_json())

# convert the object into a dict
paginated_generic_parameter_list_dict = paginated_generic_parameter_list_instance.to_dict()
# create an instance of PaginatedGenericParameterList from a dict
paginated_generic_parameter_list_from_dict = PaginatedGenericParameterList.from_dict(paginated_generic_parameter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


