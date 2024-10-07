# PACSFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**fname** | **str** |  | 
**fsize** | **int** | Get the size of the file in bytes. | [readonly] 
**public** | **bool** |  | [optional] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**file_resource** | **str** | Custom method to get the hyperlink to the actual file resource. | [readonly] 
**parent_folder** | **str** |  | [readonly] 
**owner** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.pacs_file import PACSFile

# TODO update the JSON string below
json = "{}"
# create an instance of PACSFile from a JSON string
pacs_file_instance = PACSFile.from_json(json)
# print the JSON string representation of the object
print(PACSFile.to_json())

# convert the object into a dict
pacs_file_dict = pacs_file_instance.to_dict()
# create an instance of PACSFile from a dict
pacs_file_from_dict = PACSFile.from_dict(pacs_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


