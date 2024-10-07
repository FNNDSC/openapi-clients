# PluginInstanceSplit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**filter** | **str** |  | [optional] 
**plugin_inst_id** | **int** |  | [readonly] 
**created_plugin_inst_ids** | **str** |  | [readonly] 
**plugin_inst** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.plugin_instance_split import PluginInstanceSplit

# TODO update the JSON string below
json = "{}"
# create an instance of PluginInstanceSplit from a JSON string
plugin_instance_split_instance = PluginInstanceSplit.from_json(json)
# print the JSON string representation of the object
print(PluginInstanceSplit.to_json())

# convert the object into a dict
plugin_instance_split_dict = plugin_instance_split_instance.to_dict()
# create an instance of PluginInstanceSplit from a dict
plugin_instance_split_from_dict = PluginInstanceSplit.from_dict(plugin_instance_split_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


