# PipelineSourceFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **String** |  | [readonly]
**id** | **i32** |  | [readonly]
**creation_date** | **String** |  | [readonly]
**fname** | **String** |  | 
**fsize** | **i32** | Get the size of the file in bytes. | [readonly]
**public** | Option<**bool**> |  | [optional]
**ftype** | [**models::PipelineSourceFileFtype**](PipelineSourceFile_ftype.md) |  | 
**uploader_username** | **String** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly]
**owner_username** | **String** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [readonly]
**pipeline_id** | **i32** |  | [readonly]
**pipeline_name** | **String** |  | [readonly]
**file_resource** | **String** | Custom method to get the hyperlink to the actual file resource. | [readonly]
**parent_folder** | **String** |  | [readonly]
**owner** | **String** |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


