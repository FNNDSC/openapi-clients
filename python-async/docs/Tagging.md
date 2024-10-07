# Tagging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**tag_id** | **int** |  | [readonly] 
**feed_id** | **int** |  | [readonly] 
**tag** | **str** |  | [readonly] 
**feed** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.tagging import Tagging

# TODO update the JSON string below
json = "{}"
# create an instance of Tagging from a JSON string
tagging_instance = Tagging.from_json(json)
# print the JSON string representation of the object
print(Tagging.to_json())

# convert the object into a dict
tagging_dict = tagging_instance.to_dict()
# create an instance of Tagging from a dict
tagging_from_dict = Tagging.from_dict(tagging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


