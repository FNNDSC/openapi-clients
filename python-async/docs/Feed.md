# Feed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**modification_date** | **datetime** |  | [readonly] 
**name** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**owner_username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly] 
**folder_path** | **str** |  | [readonly] 
**created_jobs** | **int** | Overriden to get the number of plugin instances in &#39;created&#39; status. | [readonly] 
**waiting_jobs** | **int** | Overriden to get the number of plugin instances in &#39;waiting&#39; status. | [readonly] 
**scheduled_jobs** | **int** | Overriden to get the number of plugin instances in &#39;scheduled&#39; status. | [readonly] 
**started_jobs** | **int** | Overriden to get the number of plugin instances in &#39;started&#39; status. | [readonly] 
**registering_jobs** | **int** | Overriden to get the number of plugin instances in &#39;registeringFiles&#39; status. | [readonly] 
**finished_jobs** | **int** | Overriden to get the number of plugin instances in &#39;finishedSuccessfully&#39; status. | [readonly] 
**errored_jobs** | **int** | Overriden to get the number of plugin instances in &#39;finishedWithError&#39; status. | [readonly] 
**cancelled_jobs** | **int** | Overriden to get the number of plugin instances in &#39;cancelled&#39; status. | [readonly] 
**folder** | **str** |  | [readonly] 
**note** | **str** |  | [readonly] 
**group_permissions** | **str** |  | [readonly] 
**user_permissions** | **str** |  | [readonly] 
**tags** | **str** |  | [readonly] 
**taggings** | **str** |  | [readonly] 
**comments** | **str** |  | [readonly] 
**plugin_instances** | **str** |  | [readonly] 
**owner** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.feed import Feed

# TODO update the JSON string below
json = "{}"
# create an instance of Feed from a JSON string
feed_instance = Feed.from_json(json)
# print the JSON string representation of the object
print(Feed.to_json())

# convert the object into a dict
feed_dict = feed_instance.to_dict()
# create an instance of Feed from a dict
feed_from_dict = Feed.from_dict(feed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


