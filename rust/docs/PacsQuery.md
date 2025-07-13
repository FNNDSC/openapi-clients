# PacsQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **String** |  | [readonly]
**id** | **i32** |  | [readonly]
**creation_date** | **String** |  | [readonly]
**title** | **String** |  | 
**query** | Option<[**serde_json::Value**](.md)> |  | [optional]
**description** | Option<**String**> |  | [optional]
**status** | [**models::StatusEc0Enum**](StatusEc0Enum.md) |  | [readonly]
**pacs_identifier** | **String** |  | [readonly]
**owner_username** | **String** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly]
**result** | **String** |  | [readonly]
**retrieve_list** | **String** |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


