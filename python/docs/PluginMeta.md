# PluginMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**modification_date** | **datetime** |  | [readonly] 
**name** | **str** |  | 
**title** | **str** |  | [optional] 
**stars** | **int** |  | [optional] 
**public_repo** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**type** | [**PluginType**](PluginType.md) |  | [optional] 
**icon** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**authors** | **str** |  | [optional] 
**documentation** | **str** |  | [optional] 
**plugins** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.plugin_meta import PluginMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PluginMeta from a JSON string
plugin_meta_instance = PluginMeta.from_json(json)
# print the JSON string representation of the object
print(PluginMeta.to_json())

# convert the object into a dict
plugin_meta_dict = plugin_meta_instance.to_dict()
# create an instance of PluginMeta from a dict
plugin_meta_from_dict = PluginMeta.from_dict(plugin_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


