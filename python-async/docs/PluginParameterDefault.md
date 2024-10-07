# PluginParameterDefault

Overriden to get the default parameter value regardless of type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from aiochris_oag.models.plugin_parameter_default import PluginParameterDefault

# TODO update the JSON string below
json = "{}"
# create an instance of PluginParameterDefault from a JSON string
plugin_parameter_default_instance = PluginParameterDefault.from_json(json)
# print the JSON string representation of the object
print(PluginParameterDefault.to_json())

# convert the object into a dict
plugin_parameter_default_dict = plugin_parameter_default_instance.to_dict()
# create an instance of PluginParameterDefault from a dict
plugin_parameter_default_from_dict = PluginParameterDefault.from_dict(plugin_parameter_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


