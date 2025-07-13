# FileBrowserLinkFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **String** |  | [readonly]
**id** | **i32** |  | [readonly]
**creation_date** | **String** |  | [readonly]
**path** | Option<**String**> |  | [optional]
**fname** | Option<**String**> |  | [optional]
**fsize** | **i32** | Get the size of the file in bytes. | [readonly]
**public** | Option<**bool**> |  | [optional]
**owner_username** | **String** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly]
**file_resource** | **String** | Custom method to get the hyperlink to the actual file resource. | [readonly]
**linked_folder** | **String** | Custom method to get the hyperlink to the linked folder if the ChRIS link points to a folder. | [readonly]
**linked_file** | **String** | Custom method to get the hyperlink to the linked file if the ChRIS link points to a file. | [readonly]
**parent_folder** | **String** |  | [readonly]
**group_permissions** | **String** |  | [readonly]
**user_permissions** | **String** |  | [readonly]
**owner** | **String** |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


