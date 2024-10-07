# UserFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**fname** | **str** |  | [optional] 
**fsize** | **int** | Get the size of the file in bytes. | [readonly] 
**public** | **bool** |  | [optional] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**file_resource** | **str** | Custom method to get the hyperlink to the actual file resource. | [readonly] 
**parent_folder** | **str** |  | [readonly] 
**group_permissions** | **str** |  | [readonly] 
**user_permissions** | **str** |  | [readonly] 
**owner** | **str** |  | [readonly] 

## Example

```python
from chris_oag.models.user_file import UserFile

# TODO update the JSON string below
json = "{}"
# create an instance of UserFile from a JSON string
user_file_instance = UserFile.from_json(json)
# print the JSON string representation of the object
print(UserFile.to_json())

# convert the object into a dict
user_file_dict = user_file_instance.to_dict()
# create an instance of UserFile from a dict
user_file_from_dict = UserFile.from_dict(user_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


