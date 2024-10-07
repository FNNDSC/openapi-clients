# PaginatedGenericDefaultPipingParameterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GenericDefaultPipingParameter]**](GenericDefaultPipingParameter.md) |  | [optional] 

## Example

```python
from aiochris_oag.models.paginated_generic_default_piping_parameter_list import PaginatedGenericDefaultPipingParameterList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGenericDefaultPipingParameterList from a JSON string
paginated_generic_default_piping_parameter_list_instance = PaginatedGenericDefaultPipingParameterList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGenericDefaultPipingParameterList.to_json())

# convert the object into a dict
paginated_generic_default_piping_parameter_list_dict = paginated_generic_default_piping_parameter_list_instance.to_dict()
# create an instance of PaginatedGenericDefaultPipingParameterList from a dict
paginated_generic_default_piping_parameter_list_from_dict = PaginatedGenericDefaultPipingParameterList.from_dict(paginated_generic_default_piping_parameter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


