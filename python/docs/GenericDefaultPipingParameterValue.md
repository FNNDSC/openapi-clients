# GenericDefaultPipingParameterValue

Overriden to get the default parameter value regardless of its type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from chris_oag.models.generic_default_piping_parameter_value import GenericDefaultPipingParameterValue

# TODO update the JSON string below
json = "{}"
# create an instance of GenericDefaultPipingParameterValue from a JSON string
generic_default_piping_parameter_value_instance = GenericDefaultPipingParameterValue.from_json(json)
# print the JSON string representation of the object
print(GenericDefaultPipingParameterValue.to_json())

# convert the object into a dict
generic_default_piping_parameter_value_dict = generic_default_piping_parameter_value_instance.to_dict()
# create an instance of GenericDefaultPipingParameterValue from a dict
generic_default_piping_parameter_value_from_dict = GenericDefaultPipingParameterValue.from_dict(generic_default_piping_parameter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


