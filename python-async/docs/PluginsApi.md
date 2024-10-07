# aiochris_oag.PluginsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_plugins_instances_list**](PluginsApi.md#all_plugins_instances_list) | **GET** /api/v1/plugins/instances/ | 
[**plugins_boolean_parameter_retrieve**](PluginsApi.md#plugins_boolean_parameter_retrieve) | **GET** /api/v1/plugins/boolean-parameter/{id}/ | 
[**plugins_computeresources_list**](PluginsApi.md#plugins_computeresources_list) | **GET** /api/v1/plugins/{id}/computeresources/ | 
[**plugins_float_parameter_retrieve**](PluginsApi.md#plugins_float_parameter_retrieve) | **GET** /api/v1/plugins/float-parameter/{id}/ | 
[**plugins_instances_create**](PluginsApi.md#plugins_instances_create) | **POST** /api/v1/plugins/{id}/instances/ | 
[**plugins_instances_descendants_list**](PluginsApi.md#plugins_instances_descendants_list) | **GET** /api/v1/plugins/instances/{id}/descendants/ | 
[**plugins_instances_destroy**](PluginsApi.md#plugins_instances_destroy) | **DELETE** /api/v1/plugins/instances/{id}/ | 
[**plugins_instances_list**](PluginsApi.md#plugins_instances_list) | **GET** /api/v1/plugins/{id}/instances/ | 
[**plugins_instances_parameters_list**](PluginsApi.md#plugins_instances_parameters_list) | **GET** /api/v1/plugins/instances/{id}/parameters/ | 
[**plugins_instances_retrieve**](PluginsApi.md#plugins_instances_retrieve) | **GET** /api/v1/plugins/instances/{id}/ | 
[**plugins_instances_search_list**](PluginsApi.md#plugins_instances_search_list) | **GET** /api/v1/plugins/instances/search/ | 
[**plugins_instances_splits_create**](PluginsApi.md#plugins_instances_splits_create) | **POST** /api/v1/plugins/instances/{id}/splits/ | 
[**plugins_instances_splits_list**](PluginsApi.md#plugins_instances_splits_list) | **GET** /api/v1/plugins/instances/{id}/splits/ | 
[**plugins_instances_splits_retrieve**](PluginsApi.md#plugins_instances_splits_retrieve) | **GET** /api/v1/plugins/instances/splits/{id}/ | 
[**plugins_instances_update**](PluginsApi.md#plugins_instances_update) | **PUT** /api/v1/plugins/instances/{id}/ | 
[**plugins_integer_parameter_retrieve**](PluginsApi.md#plugins_integer_parameter_retrieve) | **GET** /api/v1/plugins/integer-parameter/{id}/ | 
[**plugins_list**](PluginsApi.md#plugins_list) | **GET** /api/v1/plugins/ | 
[**plugins_metas_list**](PluginsApi.md#plugins_metas_list) | **GET** /api/v1/plugins/metas/ | 
[**plugins_metas_plugins_list**](PluginsApi.md#plugins_metas_plugins_list) | **GET** /api/v1/plugins/metas/{id}/plugins/ | 
[**plugins_metas_retrieve**](PluginsApi.md#plugins_metas_retrieve) | **GET** /api/v1/plugins/metas/{id}/ | 
[**plugins_metas_search_list**](PluginsApi.md#plugins_metas_search_list) | **GET** /api/v1/plugins/metas/search/ | 
[**plugins_parameters_list**](PluginsApi.md#plugins_parameters_list) | **GET** /api/v1/plugins/{id}/parameters/ | 
[**plugins_parameters_retrieve**](PluginsApi.md#plugins_parameters_retrieve) | **GET** /api/v1/plugins/parameters/{id}/ | 
[**plugins_path_parameter_retrieve**](PluginsApi.md#plugins_path_parameter_retrieve) | **GET** /api/v1/plugins/path-parameter/{id}/ | 
[**plugins_retrieve**](PluginsApi.md#plugins_retrieve) | **GET** /api/v1/plugins/{id}/ | 
[**plugins_search_list**](PluginsApi.md#plugins_search_list) | **GET** /api/v1/plugins/search/ | 
[**plugins_string_parameter_retrieve**](PluginsApi.md#plugins_string_parameter_retrieve) | **GET** /api/v1/plugins/string-parameter/{id}/ | 
[**plugins_unextpath_parameter_retrieve**](PluginsApi.md#plugins_unextpath_parameter_retrieve) | **GET** /api/v1/plugins/unextpath-parameter/{id}/ | 


# **all_plugins_instances_list**
> PaginatedPluginInstanceList all_plugins_instances_list(limit=limit, offset=offset)



A view for the collection of all plugin instances.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_plugin_instance_list import PaginatedPluginInstanceList
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.all_plugins_instances_list(limit=limit, offset=offset)
        print("The response of PluginsApi->all_plugins_instances_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->all_plugins_instances_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPluginInstanceList**](PaginatedPluginInstanceList.md)

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

# **plugins_boolean_parameter_retrieve**
> BoolParameter plugins_boolean_parameter_retrieve(id)



A boolean parameter view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.bool_parameter import BoolParameter
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.plugins_boolean_parameter_retrieve(id)
        print("The response of PluginsApi->plugins_boolean_parameter_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_boolean_parameter_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BoolParameter**](BoolParameter.md)

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

# **plugins_computeresources_list**
> PaginatedComputeResourceList plugins_computeresources_list(id, limit=limit, offset=offset)



A view for a plugin-specific collection of compute resources.

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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.plugins_computeresources_list(id, limit=limit, offset=offset)
        print("The response of PluginsApi->plugins_computeresources_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_computeresources_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
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

# **plugins_float_parameter_retrieve**
> FloatParameter plugins_float_parameter_retrieve(id)



A float parameter view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.float_parameter import FloatParameter
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.plugins_float_parameter_retrieve(id)
        print("The response of PluginsApi->plugins_float_parameter_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_float_parameter_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**FloatParameter**](FloatParameter.md)

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

# **plugins_instances_create**
> PluginInstance plugins_instances_create(id, plugin_instance_request=plugin_instance_request)



A view for the collection of plugin instances.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.plugin_instance import PluginInstance
from aiochris_oag.models.plugin_instance_request import PluginInstanceRequest
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 
    plugin_instance_request = aiochris_oag.PluginInstanceRequest() # PluginInstanceRequest |  (optional)

    try:
        api_response = await api_instance.plugins_instances_create(id, plugin_instance_request=plugin_instance_request)
        print("The response of PluginsApi->plugins_instances_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_instances_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **plugin_instance_request** | [**PluginInstanceRequest**](PluginInstanceRequest.md)|  | [optional] 

### Return type

[**PluginInstance**](PluginInstance.md)

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

# **plugins_instances_descendants_list**
> PaginatedPluginInstanceList plugins_instances_descendants_list(id, limit=limit, offset=offset)



A view for the collection of plugin instances that are a descendant of this plugin instance.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_plugin_instance_list import PaginatedPluginInstanceList
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.plugins_instances_descendants_list(id, limit=limit, offset=offset)
        print("The response of PluginsApi->plugins_instances_descendants_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_instances_descendants_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPluginInstanceList**](PaginatedPluginInstanceList.md)

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

# **plugins_instances_destroy**
> plugins_instances_destroy(id)



A plugin instance view.

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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 

    try:
        await api_instance.plugins_instances_destroy(id)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_instances_destroy: %s\n" % e)
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

# **plugins_instances_list**
> PaginatedPluginInstanceList plugins_instances_list(id, limit=limit, offset=offset)



A view for the collection of plugin instances.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_plugin_instance_list import PaginatedPluginInstanceList
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.plugins_instances_list(id, limit=limit, offset=offset)
        print("The response of PluginsApi->plugins_instances_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_instances_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPluginInstanceList**](PaginatedPluginInstanceList.md)

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

# **plugins_instances_parameters_list**
> PaginatedGenericParameterList plugins_instances_parameters_list(id, limit=limit, offset=offset)



A view for the collection of parameters that the plugin instance was run with.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_generic_parameter_list import PaginatedGenericParameterList
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.plugins_instances_parameters_list(id, limit=limit, offset=offset)
        print("The response of PluginsApi->plugins_instances_parameters_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_instances_parameters_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedGenericParameterList**](PaginatedGenericParameterList.md)

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

# **plugins_instances_retrieve**
> PluginInstance plugins_instances_retrieve(id)



A plugin instance view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.plugin_instance import PluginInstance
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.plugins_instances_retrieve(id)
        print("The response of PluginsApi->plugins_instances_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_instances_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PluginInstance**](PluginInstance.md)

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

# **plugins_instances_search_list**
> PaginatedPluginInstanceList plugins_instances_search_list(feed_id=feed_id, id=id, limit=limit, max_end_date=max_end_date, max_start_date=max_start_date, min_end_date=min_end_date, min_start_date=min_start_date, offset=offset, owner_username=owner_username, plugin_id=plugin_id, plugin_name=plugin_name, plugin_name_exact=plugin_name_exact, plugin_version=plugin_version, previous_id=previous_id, root_id=root_id, status=status, title=title, workflow_id=workflow_id)



A view for the collection of plugin instances resulting from a query search.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_plugin_instance_list import PaginatedPluginInstanceList
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    feed_id = 'feed_id_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    max_end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    max_start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    min_end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    min_start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    owner_username = 'owner_username_example' # str |  (optional)
    plugin_id = 'plugin_id_example' # str |  (optional)
    plugin_name = 'plugin_name_example' # str |  (optional)
    plugin_name_exact = 'plugin_name_exact_example' # str |  (optional)
    plugin_version = 'plugin_version_example' # str |  (optional)
    previous_id = 'previous_id_example' # str |  (optional)
    root_id = 'root_id_example' # str |  (optional)
    status = 'status_example' # str | * `created` - Default initial * `waiting` - Waiting to be scheduled * `scheduled` - Scheduled on worker * `started` - Started on compute env * `registeringFiles` - Registering output files * `finishedSuccessfully` - Finished successfully * `finishedWithError` - Finished with error * `cancelled` - Cancelled (optional)
    title = 'title_example' # str |  (optional)
    workflow_id = 'workflow_id_example' # str |  (optional)

    try:
        api_response = await api_instance.plugins_instances_search_list(feed_id=feed_id, id=id, limit=limit, max_end_date=max_end_date, max_start_date=max_start_date, min_end_date=min_end_date, min_start_date=min_start_date, offset=offset, owner_username=owner_username, plugin_id=plugin_id, plugin_name=plugin_name, plugin_name_exact=plugin_name_exact, plugin_version=plugin_version, previous_id=previous_id, root_id=root_id, status=status, title=title, workflow_id=workflow_id)
        print("The response of PluginsApi->plugins_instances_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_instances_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_id** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **max_end_date** | **datetime**|  | [optional] 
 **max_start_date** | **datetime**|  | [optional] 
 **min_end_date** | **datetime**|  | [optional] 
 **min_start_date** | **datetime**|  | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **owner_username** | **str**|  | [optional] 
 **plugin_id** | **str**|  | [optional] 
 **plugin_name** | **str**|  | [optional] 
 **plugin_name_exact** | **str**|  | [optional] 
 **plugin_version** | **str**|  | [optional] 
 **previous_id** | **str**|  | [optional] 
 **root_id** | **str**|  | [optional] 
 **status** | **str**| * &#x60;created&#x60; - Default initial * &#x60;waiting&#x60; - Waiting to be scheduled * &#x60;scheduled&#x60; - Scheduled on worker * &#x60;started&#x60; - Started on compute env * &#x60;registeringFiles&#x60; - Registering output files * &#x60;finishedSuccessfully&#x60; - Finished successfully * &#x60;finishedWithError&#x60; - Finished with error * &#x60;cancelled&#x60; - Cancelled | [optional] 
 **title** | **str**|  | [optional] 
 **workflow_id** | **str**|  | [optional] 

### Return type

[**PaginatedPluginInstanceList**](PaginatedPluginInstanceList.md)

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

# **plugins_instances_splits_create**
> PluginInstanceSplit plugins_instances_splits_create(id, plugin_instance_split_request=plugin_instance_split_request)



A view for the collection of splits for a plugin instance.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.plugin_instance_split import PluginInstanceSplit
from aiochris_oag.models.plugin_instance_split_request import PluginInstanceSplitRequest
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 
    plugin_instance_split_request = aiochris_oag.PluginInstanceSplitRequest() # PluginInstanceSplitRequest |  (optional)

    try:
        api_response = await api_instance.plugins_instances_splits_create(id, plugin_instance_split_request=plugin_instance_split_request)
        print("The response of PluginsApi->plugins_instances_splits_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_instances_splits_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **plugin_instance_split_request** | [**PluginInstanceSplitRequest**](PluginInstanceSplitRequest.md)|  | [optional] 

### Return type

[**PluginInstanceSplit**](PluginInstanceSplit.md)

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

# **plugins_instances_splits_list**
> PaginatedPluginInstanceSplitList plugins_instances_splits_list(id, limit=limit, offset=offset)



A view for the collection of splits for a plugin instance.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_plugin_instance_split_list import PaginatedPluginInstanceSplitList
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.plugins_instances_splits_list(id, limit=limit, offset=offset)
        print("The response of PluginsApi->plugins_instances_splits_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_instances_splits_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPluginInstanceSplitList**](PaginatedPluginInstanceSplitList.md)

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

# **plugins_instances_splits_retrieve**
> PluginInstanceSplit plugins_instances_splits_retrieve(id)



A view for a plugin instance split.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.plugin_instance_split import PluginInstanceSplit
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.plugins_instances_splits_retrieve(id)
        print("The response of PluginsApi->plugins_instances_splits_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_instances_splits_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PluginInstanceSplit**](PluginInstanceSplit.md)

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

# **plugins_instances_update**
> PluginInstance plugins_instances_update(id, plugin_instance_request=plugin_instance_request)



A plugin instance view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.plugin_instance import PluginInstance
from aiochris_oag.models.plugin_instance_request import PluginInstanceRequest
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 
    plugin_instance_request = aiochris_oag.PluginInstanceRequest() # PluginInstanceRequest |  (optional)

    try:
        api_response = await api_instance.plugins_instances_update(id, plugin_instance_request=plugin_instance_request)
        print("The response of PluginsApi->plugins_instances_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_instances_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **plugin_instance_request** | [**PluginInstanceRequest**](PluginInstanceRequest.md)|  | [optional] 

### Return type

[**PluginInstance**](PluginInstance.md)

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

# **plugins_integer_parameter_retrieve**
> IntParameter plugins_integer_parameter_retrieve(id)



An integer parameter view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.int_parameter import IntParameter
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.plugins_integer_parameter_retrieve(id)
        print("The response of PluginsApi->plugins_integer_parameter_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_integer_parameter_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**IntParameter**](IntParameter.md)

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

# **plugins_list**
> PaginatedPluginList plugins_list(limit=limit, offset=offset)



A view for the collection of plugins.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_plugin_list import PaginatedPluginList
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.plugins_list(limit=limit, offset=offset)
        print("The response of PluginsApi->plugins_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPluginList**](PaginatedPluginList.md)

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

# **plugins_metas_list**
> PaginatedPluginMetaList plugins_metas_list(limit=limit, offset=offset)



A view for the collection of plugin metas.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_plugin_meta_list import PaginatedPluginMetaList
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.plugins_metas_list(limit=limit, offset=offset)
        print("The response of PluginsApi->plugins_metas_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_metas_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPluginMetaList**](PaginatedPluginMetaList.md)

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

# **plugins_metas_plugins_list**
> PaginatedPluginList plugins_metas_plugins_list(id, limit=limit, offset=offset)



A view for the collection of meta-specific plugins.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_plugin_list import PaginatedPluginList
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.plugins_metas_plugins_list(id, limit=limit, offset=offset)
        print("The response of PluginsApi->plugins_metas_plugins_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_metas_plugins_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPluginList**](PaginatedPluginList.md)

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

# **plugins_metas_retrieve**
> PluginMeta plugins_metas_retrieve(id)



A plugin meta view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.plugin_meta import PluginMeta
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.plugins_metas_retrieve(id)
        print("The response of PluginsApi->plugins_metas_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_metas_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PluginMeta**](PluginMeta.md)

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

# **plugins_metas_search_list**
> PaginatedPluginMetaList plugins_metas_search_list(authors=authors, category=category, id=id, limit=limit, max_creation_date=max_creation_date, min_creation_date=min_creation_date, name=name, name_authors_category=name_authors_category, name_exact=name_exact, name_title_category=name_title_category, offset=offset, title=title, type=type)



A view for the collection of plugin metas resulting from a query search.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_plugin_meta_list import PaginatedPluginMetaList
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    authors = 'authors_example' # str |  (optional)
    category = 'category_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    max_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    min_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    name = 'name_example' # str |  (optional)
    name_authors_category = 'name_authors_category_example' # str |  (optional)
    name_exact = 'name_exact_example' # str |  (optional)
    name_title_category = 'name_title_category_example' # str |  (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    title = 'title_example' # str |  (optional)
    type = 'type_example' # str |  (optional)

    try:
        api_response = await api_instance.plugins_metas_search_list(authors=authors, category=category, id=id, limit=limit, max_creation_date=max_creation_date, min_creation_date=min_creation_date, name=name, name_authors_category=name_authors_category, name_exact=name_exact, name_title_category=name_title_category, offset=offset, title=title, type=type)
        print("The response of PluginsApi->plugins_metas_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_metas_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authors** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **max_creation_date** | **datetime**|  | [optional] 
 **min_creation_date** | **datetime**|  | [optional] 
 **name** | **str**|  | [optional] 
 **name_authors_category** | **str**|  | [optional] 
 **name_exact** | **str**|  | [optional] 
 **name_title_category** | **str**|  | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **title** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**PaginatedPluginMetaList**](PaginatedPluginMetaList.md)

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

# **plugins_parameters_list**
> PaginatedPluginParameterList plugins_parameters_list(id, limit=limit, offset=offset)



A view for the collection of plugin parameters.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_plugin_parameter_list import PaginatedPluginParameterList
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = await api_instance.plugins_parameters_list(id, limit=limit, offset=offset)
        print("The response of PluginsApi->plugins_parameters_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_parameters_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPluginParameterList**](PaginatedPluginParameterList.md)

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

# **plugins_parameters_retrieve**
> PluginParameter plugins_parameters_retrieve(id)



A plugin parameter view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.plugin_parameter import PluginParameter
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.plugins_parameters_retrieve(id)
        print("The response of PluginsApi->plugins_parameters_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_parameters_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PluginParameter**](PluginParameter.md)

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

# **plugins_path_parameter_retrieve**
> PathParameter plugins_path_parameter_retrieve(id)



A path parameter view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.path_parameter import PathParameter
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.plugins_path_parameter_retrieve(id)
        print("The response of PluginsApi->plugins_path_parameter_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_path_parameter_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PathParameter**](PathParameter.md)

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

# **plugins_retrieve**
> Plugin plugins_retrieve(id)



A plugin view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.plugin import Plugin
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.plugins_retrieve(id)
        print("The response of PluginsApi->plugins_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Plugin**](Plugin.md)

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

# **plugins_search_list**
> PaginatedPluginList plugins_search_list(category=category, compute_resource_id=compute_resource_id, description=description, dock_image=dock_image, id=id, limit=limit, max_creation_date=max_creation_date, min_creation_date=min_creation_date, name=name, name_exact=name_exact, name_title_category=name_title_category, offset=offset, title=title, type=type, version=version)



A view for the collection of plugins resulting from a query search.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.paginated_plugin_list import PaginatedPluginList
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    category = 'category_example' # str |  (optional)
    compute_resource_id = 'compute_resource_id_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    dock_image = 'dock_image_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    max_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    min_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    name = 'name_example' # str |  (optional)
    name_exact = 'name_exact_example' # str |  (optional)
    name_title_category = 'name_title_category_example' # str |  (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    title = 'title_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        api_response = await api_instance.plugins_search_list(category=category, compute_resource_id=compute_resource_id, description=description, dock_image=dock_image, id=id, limit=limit, max_creation_date=max_creation_date, min_creation_date=min_creation_date, name=name, name_exact=name_exact, name_title_category=name_title_category, offset=offset, title=title, type=type, version=version)
        print("The response of PluginsApi->plugins_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | [optional] 
 **compute_resource_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **dock_image** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **max_creation_date** | **datetime**|  | [optional] 
 **min_creation_date** | **datetime**|  | [optional] 
 **name** | **str**|  | [optional] 
 **name_exact** | **str**|  | [optional] 
 **name_title_category** | **str**|  | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **title** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**PaginatedPluginList**](PaginatedPluginList.md)

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

# **plugins_string_parameter_retrieve**
> StrParameter plugins_string_parameter_retrieve(id)



A string parameter view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.str_parameter import StrParameter
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.plugins_string_parameter_retrieve(id)
        print("The response of PluginsApi->plugins_string_parameter_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_string_parameter_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**StrParameter**](StrParameter.md)

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

# **plugins_unextpath_parameter_retrieve**
> UnextpathParameter plugins_unextpath_parameter_retrieve(id)



A unextpath parameter view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import aiochris_oag
from aiochris_oag.models.unextpath_parameter import UnextpathParameter
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
    api_instance = aiochris_oag.PluginsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.plugins_unextpath_parameter_retrieve(id)
        print("The response of PluginsApi->plugins_unextpath_parameter_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_unextpath_parameter_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UnextpathParameter**](UnextpathParameter.md)

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

