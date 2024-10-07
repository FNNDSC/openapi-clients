# chris_oag.ComputeresourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**computeresources_list**](ComputeresourcesApi.md#computeresources_list) | **GET** /api/v1/computeresources/ | 
[**computeresources_retrieve**](ComputeresourcesApi.md#computeresources_retrieve) | **GET** /api/v1/computeresources/{id}/ | 
[**computeresources_search_list**](ComputeresourcesApi.md#computeresources_search_list) | **GET** /api/v1/computeresources/search/ | 


# **computeresources_list**
> PaginatedComputeResourceList computeresources_list(limit=limit, offset=offset)



A view for the collection of compute resources.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_compute_resource_list import PaginatedComputeResourceList
from chris_oag.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = chris_oag.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = chris_oag.Configuration(
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
with chris_oag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = chris_oag.ComputeresourcesApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.computeresources_list(limit=limit, offset=offset)
        print("The response of ComputeresourcesApi->computeresources_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputeresourcesApi->computeresources_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedComputeResourceList**](PaginatedComputeResourceList.md)

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

# **computeresources_retrieve**
> ComputeResource computeresources_retrieve(id)



A compute resource view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.compute_resource import ComputeResource
from chris_oag.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = chris_oag.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = chris_oag.Configuration(
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
with chris_oag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = chris_oag.ComputeresourcesApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.computeresources_retrieve(id)
        print("The response of ComputeresourcesApi->computeresources_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputeresourcesApi->computeresources_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ComputeResource**](ComputeResource.md)

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

# **computeresources_search_list**
> PaginatedComputeResourceList computeresources_search_list(description=description, id=id, limit=limit, name=name, name_exact=name_exact, offset=offset, plugin_id=plugin_id)



A view for the collection of compute resources resulting from a query search.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_compute_resource_list import PaginatedComputeResourceList
from chris_oag.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = chris_oag.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = chris_oag.Configuration(
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
with chris_oag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = chris_oag.ComputeresourcesApi(api_client)
    description = 'description_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str |  (optional)
    name_exact = 'name_exact_example' # str |  (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    plugin_id = 'plugin_id_example' # str |  (optional)

    try:
        api_response = api_instance.computeresources_search_list(description=description, id=id, limit=limit, name=name, name_exact=name_exact, offset=offset, plugin_id=plugin_id)
        print("The response of ComputeresourcesApi->computeresources_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputeresourcesApi->computeresources_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**|  | [optional] 
 **name_exact** | **str**|  | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **plugin_id** | **str**|  | [optional] 

### Return type

[**PaginatedComputeResourceList**](PaginatedComputeResourceList.md)

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

