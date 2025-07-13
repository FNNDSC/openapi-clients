# Feed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **String** |  | [readonly]
**id** | **i32** |  | [readonly]
**creation_date** | **String** |  | [readonly]
**modification_date** | **String** |  | [readonly]
**name** | Option<**String**> |  | [optional]
**public** | Option<**bool**> |  | [optional]
**owner_username** | **String** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly]
**folder_path** | **String** |  | [readonly]
**created_jobs** | **i32** | Overriden to get the number of plugin instances in 'created' status. | [readonly]
**waiting_jobs** | **i32** | Overriden to get the number of plugin instances in 'waiting' status. | [readonly]
**scheduled_jobs** | **i32** | Overriden to get the number of plugin instances in 'scheduled' status. | [readonly]
**started_jobs** | **i32** | Overriden to get the number of plugin instances in 'started' status. | [readonly]
**registering_jobs** | **i32** | Overriden to get the number of plugin instances in 'registeringFiles' status. | [readonly]
**finished_jobs** | **i32** | Overriden to get the number of plugin instances in 'finishedSuccessfully' status. | [readonly]
**errored_jobs** | **i32** | Overriden to get the number of plugin instances in 'finishedWithError' status. | [readonly]
**cancelled_jobs** | **i32** | Overriden to get the number of plugin instances in 'cancelled' status. | [readonly]
**folder** | **String** |  | [readonly]
**note** | **String** |  | [readonly]
**group_permissions** | **String** |  | [readonly]
**user_permissions** | **String** |  | [readonly]
**tags** | **String** |  | [readonly]
**taggings** | **String** |  | [readonly]
**comments** | **String** |  | [readonly]
**plugin_instances** | **String** |  | [readonly]
**owner** | **String** |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


