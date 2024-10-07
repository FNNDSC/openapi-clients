# aiochris_oag.ChrisAdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chris_admin_api_v1_computeresources_create**](ChrisAdminApi.md#chris_admin_api_v1_computeresources_create) | **POST** /chris-admin/api/v1/computeresources/ | 
[**chris_admin_api_v1_computeresources_destroy**](ChrisAdminApi.md#chris_admin_api_v1_computeresources_destroy) | **DELETE** /chris-admin/api/v1/computeresources/{id}/ | 
[**chris_admin_api_v1_computeresources_list**](ChrisAdminApi.md#chris_admin_api_v1_computeresources_list) | **GET** /chris-admin/api/v1/computeresources/ | 
[**chris_admin_api_v1_computeresources_retrieve**](ChrisAdminApi.md#chris_admin_api_v1_computeresources_retrieve) | **GET** /chris-admin/api/v1/computeresources/{id}/ | 
[**chris_admin_api_v1_create**](ChrisAdminApi.md#chris_admin_api_v1_create) | **POST** /chris-admin/api/v1/ | 
[**chris_admin_api_v1_destroy**](ChrisAdminApi.md#chris_admin_api_v1_destroy) | **DELETE** /chris-admin/api/v1/{id}/ | 
[**chris_admin_api_v1_list**](ChrisAdminApi.md#chris_admin_api_v1_list) | **GET** /chris-admin/api/v1/ | 
[**chris_admin_api_v1_retrieve**](ChrisAdminApi.md#chris_admin_api_v1_retrieve) | **GET** /chris-admin/api/v1/{id}/ | 
[**chris_admin_api_v1_update**](ChrisAdminApi.md#chris_admin_api_v1_update) | **PUT** /chris-admin/api/v1/{id}/ | 


# **chris_admin_api_v1_computeresources_create**
> ComputeResource chris_admin_api_v1_computeresources_create(compute_resource_request)



A JSON view for the collection of compute resources that can be used by ChRIS admins to add a new compute resource through a REST API (alternative to the HTML-based admin site).

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.compute_resource import ComputeResource
from aiochris_oag.models.compute_resource_request import ComputeResourceRequest
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
    api_instance = aiochris_oag.ChrisAdminApi(api_client)
    compute_resource_request = aiochris_oag.ComputeResourceRequest() # ComputeResourceRequest | 

    try:
        api_response = await api_instance.chris_admin_api_v1_computeresources_create(compute_resource_request)
        print("The response of ChrisAdminApi->chris_admin_api_v1_computeresources_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChrisAdminApi->chris_admin_api_v1_computeresources_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_resource_request** | [**ComputeResourceRequest**](ComputeResourceRequest.md)|  | 

### Return type

[**ComputeResource**](ComputeResource.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chris_admin_api_v1_computeresources_destroy**
> chris_admin_api_v1_computeresources_destroy(id)



A JSON view for a compute resource that can be used by ChRIS admins to delete the compute resource through a REST API.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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
    api_instance = aiochris_oag.ChrisAdminApi(api_client)
    id = 56 # int | 

    try:
        await api_instance.chris_admin_api_v1_computeresources_destroy(id)
    except Exception as e:
        print("Exception when calling ChrisAdminApi->chris_admin_api_v1_computeresources_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chris_admin_api_v1_computeresources_list**
> PaginatedComputeResourceList chris_admin_api_v1_computeresources_list(limit=limit, offset=offset)



A JSON view for the collection of compute resources that can be used by ChRIS admins to add a new compute resource through a REST API (alternative to the HTML-based admin site).

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_compute_resource_list import PaginatedComputeResourceList
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
    api_instance = aiochris_oag.ChrisAdminApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.chris_admin_api_v1_computeresources_list(limit=limit, offset=offset)
        print("The response of ChrisAdminApi->chris_admin_api_v1_computeresources_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChrisAdminApi->chris_admin_api_v1_computeresources_list: %s\n" % e)
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

# **chris_admin_api_v1_computeresources_retrieve**
> ComputeResource chris_admin_api_v1_computeresources_retrieve(id)



A JSON view for a compute resource that can be used by ChRIS admins to delete the compute resource through a REST API.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.compute_resource import ComputeResource
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
    api_instance = aiochris_oag.ChrisAdminApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.chris_admin_api_v1_computeresources_retrieve(id)
        print("The response of ChrisAdminApi->chris_admin_api_v1_computeresources_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChrisAdminApi->chris_admin_api_v1_computeresources_retrieve: %s\n" % e)
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

# **chris_admin_api_v1_create**
> PluginAdmin chris_admin_api_v1_create(plugin_admin_request)



A JSON view for the collection of plugins that can be used by ChRIS admins to register plugins through a REST API (alternative to the HTML-based admin site).

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.plugin_admin import PluginAdmin
from aiochris_oag.models.plugin_admin_request import PluginAdminRequest
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
    api_instance = aiochris_oag.ChrisAdminApi(api_client)
    plugin_admin_request = aiochris_oag.PluginAdminRequest() # PluginAdminRequest | 

    try:
        api_response = await api_instance.chris_admin_api_v1_create(plugin_admin_request)
        print("The response of ChrisAdminApi->chris_admin_api_v1_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChrisAdminApi->chris_admin_api_v1_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_admin_request** | [**PluginAdminRequest**](PluginAdminRequest.md)|  | 

### Return type

[**PluginAdmin**](PluginAdmin.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chris_admin_api_v1_destroy**
> chris_admin_api_v1_destroy(id)



A JSON view for a plugin that can be used by ChRIS admins to delete the plugin through a REST API.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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
    api_instance = aiochris_oag.ChrisAdminApi(api_client)
    id = 56 # int | 

    try:
        await api_instance.chris_admin_api_v1_destroy(id)
    except Exception as e:
        print("Exception when calling ChrisAdminApi->chris_admin_api_v1_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chris_admin_api_v1_list**
> PaginatedPluginAdminList chris_admin_api_v1_list(limit=limit, offset=offset)



A JSON view for the collection of plugins that can be used by ChRIS admins to register plugins through a REST API (alternative to the HTML-based admin site).

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_plugin_admin_list import PaginatedPluginAdminList
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
    api_instance = aiochris_oag.ChrisAdminApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.chris_admin_api_v1_list(limit=limit, offset=offset)
        print("The response of ChrisAdminApi->chris_admin_api_v1_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChrisAdminApi->chris_admin_api_v1_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPluginAdminList**](PaginatedPluginAdminList.md)

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

# **chris_admin_api_v1_retrieve**
> PluginAdmin chris_admin_api_v1_retrieve(id)



A JSON view for a plugin that can be used by ChRIS admins to delete the plugin through a REST API.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.plugin_admin import PluginAdmin
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
    api_instance = aiochris_oag.ChrisAdminApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.chris_admin_api_v1_retrieve(id)
        print("The response of ChrisAdminApi->chris_admin_api_v1_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChrisAdminApi->chris_admin_api_v1_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PluginAdmin**](PluginAdmin.md)

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

# **chris_admin_api_v1_update**
> PluginAdmin chris_admin_api_v1_update(id, plugin_admin_request)



A JSON view for a plugin that can be used by ChRIS admins to delete the plugin through a REST API.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.plugin_admin import PluginAdmin
from aiochris_oag.models.plugin_admin_request import PluginAdminRequest
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
    api_instance = aiochris_oag.ChrisAdminApi(api_client)
    id = 56 # int | 
    plugin_admin_request = aiochris_oag.PluginAdminRequest() # PluginAdminRequest | 

    try:
        api_response = await api_instance.chris_admin_api_v1_update(id, plugin_admin_request)
        print("The response of ChrisAdminApi->chris_admin_api_v1_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChrisAdminApi->chris_admin_api_v1_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **plugin_admin_request** | [**PluginAdminRequest**](PluginAdminRequest.md)|  | 

### Return type

[**PluginAdmin**](PluginAdmin.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

