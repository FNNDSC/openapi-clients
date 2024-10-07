# aiochris_oag.PacsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pacs_files_list**](PacsApi.md#pacs_files_list) | **GET** /api/v1/pacs/files/ | 
[**pacs_files_retrieve**](PacsApi.md#pacs_files_retrieve) | **GET** /api/v1/pacs/files/{id}/ | 
[**pacs_files_retrieve_0**](PacsApi.md#pacs_files_retrieve_0) | **GET** /api/v1/pacs/files/{id}/. | 
[**pacs_files_search_list**](PacsApi.md#pacs_files_search_list) | **GET** /api/v1/pacs/files/search/ | 
[**pacs_series_list**](PacsApi.md#pacs_series_list) | **GET** /api/v1/pacs/series/ | 
[**pacs_series_retrieve**](PacsApi.md#pacs_series_retrieve) | **GET** /api/v1/pacs/series/{id}/ | 
[**pacs_series_search_list**](PacsApi.md#pacs_series_search_list) | **GET** /api/v1/pacs/series/search/ | 


# **pacs_files_list**
> PaginatedPACSFileList pacs_files_list(limit=limit, offset=offset)



A view for the collection of PACS files.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_pacs_file_list import PaginatedPACSFileList
from aiochris_oag.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aiochris_oag.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aiochris_oag.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with aiochris_oag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiochris_oag.PacsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.pacs_files_list(limit=limit, offset=offset)
        print("The response of PacsApi->pacs_files_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PacsApi->pacs_files_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPACSFileList**](PaginatedPACSFileList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pacs_files_retrieve**
> PACSFile pacs_files_retrieve(id)



A PACS file view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.pacs_file import PACSFile
from aiochris_oag.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aiochris_oag.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aiochris_oag.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with aiochris_oag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiochris_oag.PacsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.pacs_files_retrieve(id)
        print("The response of PacsApi->pacs_files_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PacsApi->pacs_files_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PACSFile**](PACSFile.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pacs_files_retrieve_0**
> bytearray pacs_files_retrieve_0(id)



Overriden to be able to make a GET request to an actual file resource.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (DownloadTokenInQueryString):

```python
import aiochris_oag
from aiochris_oag.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aiochris_oag.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aiochris_oag.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: DownloadTokenInQueryString
configuration.api_key['DownloadTokenInQueryString'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['DownloadTokenInQueryString'] = 'Bearer'

# Enter a context with an instance of the API client
async with aiochris_oag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiochris_oag.PacsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.pacs_files_retrieve_0(id)
        print("The response of PacsApi->pacs_files_retrieve_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PacsApi->pacs_files_retrieve_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bytearray**

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [DownloadTokenInQueryString](../README.md#DownloadTokenInQueryString)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pacs_files_search_list**
> PaginatedPACSFileList pacs_files_search_list(fname=fname, fname_exact=fname_exact, fname_icontains=fname_icontains, fname_icontains_topdir_unique=fname_icontains_topdir_unique, fname_nslashes=fname_nslashes, id=id, limit=limit, max_creation_date=max_creation_date, min_creation_date=min_creation_date, offset=offset)



A view for the collection of PACS files resulting from a query search.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_pacs_file_list import PaginatedPACSFileList
from aiochris_oag.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aiochris_oag.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aiochris_oag.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with aiochris_oag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiochris_oag.PacsApi(api_client)
    fname = 'fname_example' # str |  (optional)
    fname_exact = 'fname_exact_example' # str |  (optional)
    fname_icontains = 'fname_icontains_example' # str |  (optional)
    fname_icontains_topdir_unique = 'fname_icontains_topdir_unique_example' # str |  (optional)
    fname_nslashes = 'fname_nslashes_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    max_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    min_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.pacs_files_search_list(fname=fname, fname_exact=fname_exact, fname_icontains=fname_icontains, fname_icontains_topdir_unique=fname_icontains_topdir_unique, fname_nslashes=fname_nslashes, id=id, limit=limit, max_creation_date=max_creation_date, min_creation_date=min_creation_date, offset=offset)
        print("The response of PacsApi->pacs_files_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PacsApi->pacs_files_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fname** | **str**|  | [optional] 
 **fname_exact** | **str**|  | [optional] 
 **fname_icontains** | **str**|  | [optional] 
 **fname_icontains_topdir_unique** | **str**|  | [optional] 
 **fname_nslashes** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **max_creation_date** | **datetime**|  | [optional] 
 **min_creation_date** | **datetime**|  | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPACSFileList**](PaginatedPACSFileList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pacs_series_list**
> PaginatedPACSSeriesList pacs_series_list(limit=limit, offset=offset)



A view for the collection of PACS Series.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_pacs_series_list import PaginatedPACSSeriesList
from aiochris_oag.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aiochris_oag.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aiochris_oag.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with aiochris_oag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiochris_oag.PacsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.pacs_series_list(limit=limit, offset=offset)
        print("The response of PacsApi->pacs_series_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PacsApi->pacs_series_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPACSSeriesList**](PaginatedPACSSeriesList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pacs_series_retrieve**
> PACSSeries pacs_series_retrieve(id)



A PACS Series view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.pacs_series import PACSSeries
from aiochris_oag.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aiochris_oag.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aiochris_oag.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with aiochris_oag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiochris_oag.PacsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.pacs_series_retrieve(id)
        print("The response of PacsApi->pacs_series_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PacsApi->pacs_series_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PACSSeries**](PACSSeries.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pacs_series_search_list**
> PaginatedPACSSeriesList pacs_series_search_list(accession_number=accession_number, patient_age=patient_age, patient_birth_date=patient_birth_date, patient_id=patient_id, patient_name=patient_name, patient_sex=patient_sex, protocol_name=protocol_name, series_description=series_description, series_instance_uid=series_instance_uid, study_date=study_date, study_description=study_description, study_instance_uid=study_instance_uid, id=id, limit=limit, max_patient_age=max_patient_age, max_creation_date=max_creation_date, min_patient_age=min_patient_age, min_creation_date=min_creation_date, offset=offset, pacs_identifier=pacs_identifier)



A view for the collection of PACS Series resulting from a query search.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_pacs_series_list import PaginatedPACSSeriesList
from aiochris_oag.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aiochris_oag.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = aiochris_oag.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with aiochris_oag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiochris_oag.PacsApi(api_client)
    accession_number = 'accession_number_example' # str |  (optional)
    patient_age = 56 # int |  (optional)
    patient_birth_date = '2013-10-20' # date |  (optional)
    patient_id = 'patient_id_example' # str |  (optional)
    patient_name = 'patient_name_example' # str |  (optional)
    patient_sex = 'patient_sex_example' # str | * `M` - Male * `F` - Female * `O` - Other (optional)
    protocol_name = 'protocol_name_example' # str |  (optional)
    series_description = 'series_description_example' # str |  (optional)
    series_instance_uid = 'series_instance_uid_example' # str |  (optional)
    study_date = '2013-10-20' # date |  (optional)
    study_description = 'study_description_example' # str |  (optional)
    study_instance_uid = 'study_instance_uid_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    max_patient_age = 56 # int |  (optional)
    max_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    min_patient_age = 56 # int |  (optional)
    min_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    pacs_identifier = 'pacs_identifier_example' # str |  (optional)

    try:
        api_response = await api_instance.pacs_series_search_list(accession_number=accession_number, patient_age=patient_age, patient_birth_date=patient_birth_date, patient_id=patient_id, patient_name=patient_name, patient_sex=patient_sex, protocol_name=protocol_name, series_description=series_description, series_instance_uid=series_instance_uid, study_date=study_date, study_description=study_description, study_instance_uid=study_instance_uid, id=id, limit=limit, max_patient_age=max_patient_age, max_creation_date=max_creation_date, min_patient_age=min_patient_age, min_creation_date=min_creation_date, offset=offset, pacs_identifier=pacs_identifier)
        print("The response of PacsApi->pacs_series_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PacsApi->pacs_series_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession_number** | **str**|  | [optional] 
 **patient_age** | **int**|  | [optional] 
 **patient_birth_date** | **date**|  | [optional] 
 **patient_id** | **str**|  | [optional] 
 **patient_name** | **str**|  | [optional] 
 **patient_sex** | **str**| * &#x60;M&#x60; - Male * &#x60;F&#x60; - Female * &#x60;O&#x60; - Other | [optional] 
 **protocol_name** | **str**|  | [optional] 
 **series_description** | **str**|  | [optional] 
 **series_instance_uid** | **str**|  | [optional] 
 **study_date** | **date**|  | [optional] 
 **study_description** | **str**|  | [optional] 
 **study_instance_uid** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **max_patient_age** | **int**|  | [optional] 
 **max_creation_date** | **datetime**|  | [optional] 
 **min_patient_age** | **int**|  | [optional] 
 **min_creation_date** | **datetime**|  | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **pacs_identifier** | **str**|  | [optional] 

### Return type

[**PaginatedPACSSeriesList**](PaginatedPACSSeriesList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

