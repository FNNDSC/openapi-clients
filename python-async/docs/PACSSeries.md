# PACSSeries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**creation_date** | **datetime** |  | [readonly] 
**patient_id** | **str** |  | 
**patient_name** | **str** |  | [optional] 
**patient_birth_date** | **date** |  | [optional] 
**patient_age** | **int** |  | [optional] 
**patient_sex** | [**PACSSeriesPatientSex**](PACSSeriesPatientSex.md) |  | [optional] 
**study_date** | **date** |  | 
**accession_number** | **str** |  | [optional] 
**modality** | **str** |  | [optional] 
**protocol_name** | **str** |  | [optional] 
**study_instance_uid** | **str** |  | 
**study_description** | **str** |  | [optional] 
**series_instance_uid** | **str** |  | 
**series_description** | **str** |  | [optional] 
**pacs_identifier** | **str** |  | [readonly] 
**folder** | **str** |  | [readonly] 

## Example

```python
from aiochris_oag.models.pacs_series import PACSSeries

# TODO update the JSON string below
json = "{}"
# create an instance of PACSSeries from a JSON string
pacs_series_instance = PACSSeries.from_json(json)
# print the JSON string representation of the object
print(PACSSeries.to_json())

# convert the object into a dict
pacs_series_dict = pacs_series_instance.to_dict()
# create an instance of PACSSeries from a dict
pacs_series_from_dict = PACSSeries.from_dict(pacs_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


