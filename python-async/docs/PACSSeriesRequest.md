# PACSSeriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**ndicom** | **int** |  | 
**patient_id** | **str** |  | 
**patient_name** | **str** |  | [optional] 
**patient_birth_date** | **date** |  | [optional] 
**patient_age** | **int** |  | [optional] 
**patient_sex** | **str** |  | [optional] 
**study_date** | **date** |  | 
**accession_number** | **str** |  | [optional] 
**modality** | **str** |  | [optional] 
**protocol_name** | **str** |  | [optional] 
**study_instance_uid** | **str** |  | 
**study_description** | **str** |  | [optional] 
**series_instance_uid** | **str** |  | 
**series_description** | **str** |  | [optional] 
**pacs_name** | **str** |  | 
**deletion_status** | [**DeletionStatusEnum**](DeletionStatusEnum.md) |  | [optional] 
**deletion_requested_at** | **datetime** |  | [optional] 
**deletion_error** | **str** |  | [optional] 

## Example

```python
from aiochris_oag.models.pacs_series_request import PACSSeriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PACSSeriesRequest from a JSON string
pacs_series_request_instance = PACSSeriesRequest.from_json(json)
# print the JSON string representation of the object
print(PACSSeriesRequest.to_json())

# convert the object into a dict
pacs_series_request_dict = pacs_series_request_instance.to_dict()
# create an instance of PACSSeriesRequest from a dict
pacs_series_request_from_dict = PACSSeriesRequest.from_dict(pacs_series_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


