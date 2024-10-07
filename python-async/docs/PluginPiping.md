# PluginPiping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**previous_id** | **int** |  | [readonly] 
**title** | **str** |  | 
**plugin_id** | **int** |  | [readonly] 
**plugin_name** | **str** |  | [readonly] 
**plugin_version** | **str** |  | [readonly] 
**pipeline_id** | **int** |  | [readonly] 
**previous** | **str** |  | [readonly] 
**plugin** | **str** |  | [readonly] 
**pipeline** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.plugin_piping import PluginPiping

# TODO update the JSON string below
json = "{}"
# create an instance of PluginPiping from a JSON string
plugin_piping_instance = PluginPiping.from_json(json)
# print the JSON string representation of the object
print(PluginPiping.to_json())

# convert the object into a dict
plugin_piping_dict = plugin_piping_instance.to_dict()
# create an instance of PluginPiping from a dict
plugin_piping_from_dict = PluginPiping.from_dict(plugin_piping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


