# chris_oag.PipelinesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_workflows_list**](PipelinesApi.md#all_workflows_list) | **GET** /api/v1/pipelines/workflows/ | 
[**pipelines_boolean_parameter_retrieve**](PipelinesApi.md#pipelines_boolean_parameter_retrieve) | **GET** /api/v1/pipelines/boolean-parameter/{id}/ | 
[**pipelines_boolean_parameter_update**](PipelinesApi.md#pipelines_boolean_parameter_update) | **PUT** /api/v1/pipelines/boolean-parameter/{id}/ | 
[**pipelines_create**](PipelinesApi.md#pipelines_create) | **POST** /api/v1/pipelines/ | 
[**pipelines_destroy**](PipelinesApi.md#pipelines_destroy) | **DELETE** /api/v1/pipelines/{id}/ | 
[**pipelines_float_parameter_retrieve**](PipelinesApi.md#pipelines_float_parameter_retrieve) | **GET** /api/v1/pipelines/float-parameter/{id}/ | 
[**pipelines_float_parameter_update**](PipelinesApi.md#pipelines_float_parameter_update) | **PUT** /api/v1/pipelines/float-parameter/{id}/ | 
[**pipelines_integer_parameter_retrieve**](PipelinesApi.md#pipelines_integer_parameter_retrieve) | **GET** /api/v1/pipelines/integer-parameter/{id}/ | 
[**pipelines_integer_parameter_update**](PipelinesApi.md#pipelines_integer_parameter_update) | **PUT** /api/v1/pipelines/integer-parameter/{id}/ | 
[**pipelines_json_retrieve**](PipelinesApi.md#pipelines_json_retrieve) | **GET** /api/v1/pipelines/{id}/json/ | 
[**pipelines_list**](PipelinesApi.md#pipelines_list) | **GET** /api/v1/pipelines/ | 
[**pipelines_parameters_list**](PipelinesApi.md#pipelines_parameters_list) | **GET** /api/v1/pipelines/{id}/parameters/ | 
[**pipelines_pipings_list**](PipelinesApi.md#pipelines_pipings_list) | **GET** /api/v1/pipelines/{id}/pipings/ | 
[**pipelines_pipings_retrieve**](PipelinesApi.md#pipelines_pipings_retrieve) | **GET** /api/v1/pipelines/pipings/{id}/ | 
[**pipelines_plugins_list**](PipelinesApi.md#pipelines_plugins_list) | **GET** /api/v1/pipelines/{id}/plugins/ | 
[**pipelines_retrieve**](PipelinesApi.md#pipelines_retrieve) | **GET** /api/v1/pipelines/{id}/ | 
[**pipelines_search_list**](PipelinesApi.md#pipelines_search_list) | **GET** /api/v1/pipelines/search/ | 
[**pipelines_sourcefiles_create**](PipelinesApi.md#pipelines_sourcefiles_create) | **POST** /api/v1/pipelines/sourcefiles/ | 
[**pipelines_sourcefiles_list**](PipelinesApi.md#pipelines_sourcefiles_list) | **GET** /api/v1/pipelines/sourcefiles/ | 
[**pipelines_sourcefiles_retrieve**](PipelinesApi.md#pipelines_sourcefiles_retrieve) | **GET** /api/v1/pipelines/sourcefiles/{id}/ | 
[**pipelines_sourcefiles_retrieve_0**](PipelinesApi.md#pipelines_sourcefiles_retrieve_0) | **GET** /api/v1/pipelines/sourcefiles/{id}/. | 
[**pipelines_sourcefiles_search_list**](PipelinesApi.md#pipelines_sourcefiles_search_list) | **GET** /api/v1/pipelines/sourcefiles/search/ | 
[**pipelines_string_parameter_retrieve**](PipelinesApi.md#pipelines_string_parameter_retrieve) | **GET** /api/v1/pipelines/string-parameter/{id}/ | 
[**pipelines_string_parameter_update**](PipelinesApi.md#pipelines_string_parameter_update) | **PUT** /api/v1/pipelines/string-parameter/{id}/ | 
[**pipelines_update**](PipelinesApi.md#pipelines_update) | **PUT** /api/v1/pipelines/{id}/ | 
[**pipelines_workflows_create**](PipelinesApi.md#pipelines_workflows_create) | **POST** /api/v1/pipelines/{id}/workflows/ | 
[**pipelines_workflows_destroy**](PipelinesApi.md#pipelines_workflows_destroy) | **DELETE** /api/v1/pipelines/workflows/{id}/ | 
[**pipelines_workflows_plugininstances_list**](PipelinesApi.md#pipelines_workflows_plugininstances_list) | **GET** /api/v1/pipelines/workflows/{id}/plugininstances/ | 
[**pipelines_workflows_retrieve**](PipelinesApi.md#pipelines_workflows_retrieve) | **GET** /api/v1/pipelines/workflows/{id}/ | 
[**pipelines_workflows_search_list**](PipelinesApi.md#pipelines_workflows_search_list) | **GET** /api/v1/pipelines/workflows/search/ | 
[**pipelines_workflows_update**](PipelinesApi.md#pipelines_workflows_update) | **PUT** /api/v1/pipelines/workflows/{id}/ | 
[**workflows_list**](PipelinesApi.md#workflows_list) | **GET** /api/v1/pipelines/{id}/workflows/ | 


# **all_workflows_list**
> PaginatedWorkflowList all_workflows_list(limit=limit, offset=offset)



A view for the collection of all workflows.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_workflow_list import PaginatedWorkflowList
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
    api_instance = chris_oag.PipelinesApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.all_workflows_list(limit=limit, offset=offset)
        print("The response of PipelinesApi->all_workflows_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->all_workflows_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedWorkflowList**](PaginatedWorkflowList.md)

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

# **pipelines_boolean_parameter_retrieve**
> DefaultPipingBoolParameter pipelines_boolean_parameter_retrieve(id)



A view for a boolean default value for a plugin parameter in a pipeline's plugin piping.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.default_piping_bool_parameter import DefaultPipingBoolParameter
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.pipelines_boolean_parameter_retrieve(id)
        print("The response of PipelinesApi->pipelines_boolean_parameter_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_boolean_parameter_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DefaultPipingBoolParameter**](DefaultPipingBoolParameter.md)

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

# **pipelines_boolean_parameter_update**
> DefaultPipingBoolParameter pipelines_boolean_parameter_update(id, default_piping_bool_parameter_request=default_piping_bool_parameter_request)



A view for a boolean default value for a plugin parameter in a pipeline's plugin piping.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.default_piping_bool_parameter import DefaultPipingBoolParameter
from chris_oag.models.default_piping_bool_parameter_request import DefaultPipingBoolParameterRequest
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 
    default_piping_bool_parameter_request = chris_oag.DefaultPipingBoolParameterRequest() # DefaultPipingBoolParameterRequest |  (optional)

    try:
        api_response = api_instance.pipelines_boolean_parameter_update(id, default_piping_bool_parameter_request=default_piping_bool_parameter_request)
        print("The response of PipelinesApi->pipelines_boolean_parameter_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_boolean_parameter_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **default_piping_bool_parameter_request** | [**DefaultPipingBoolParameterRequest**](DefaultPipingBoolParameterRequest.md)|  | [optional] 

### Return type

[**DefaultPipingBoolParameter**](DefaultPipingBoolParameter.md)

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

# **pipelines_create**
> Pipeline pipelines_create(pipeline_request)



A view for the collection of pipelines.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.pipeline import Pipeline
from chris_oag.models.pipeline_request import PipelineRequest
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
    api_instance = chris_oag.PipelinesApi(api_client)
    pipeline_request = chris_oag.PipelineRequest() # PipelineRequest | 

    try:
        api_response = api_instance.pipelines_create(pipeline_request)
        print("The response of PipelinesApi->pipelines_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_request** | [**PipelineRequest**](PipelineRequest.md)|  | 

### Return type

[**Pipeline**](Pipeline.md)

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

# **pipelines_destroy**
> pipelines_destroy(id)



A pipeline view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 

    try:
        api_instance.pipelines_destroy(id)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_destroy: %s\n" % e)
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

# **pipelines_float_parameter_retrieve**
> DefaultPipingFloatParameter pipelines_float_parameter_retrieve(id)



A view for a float default value for a plugin parameter in a pipeline's plugin piping.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.default_piping_float_parameter import DefaultPipingFloatParameter
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.pipelines_float_parameter_retrieve(id)
        print("The response of PipelinesApi->pipelines_float_parameter_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_float_parameter_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DefaultPipingFloatParameter**](DefaultPipingFloatParameter.md)

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

# **pipelines_float_parameter_update**
> DefaultPipingFloatParameter pipelines_float_parameter_update(id, default_piping_float_parameter_request=default_piping_float_parameter_request)



A view for a float default value for a plugin parameter in a pipeline's plugin piping.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.default_piping_float_parameter import DefaultPipingFloatParameter
from chris_oag.models.default_piping_float_parameter_request import DefaultPipingFloatParameterRequest
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 
    default_piping_float_parameter_request = chris_oag.DefaultPipingFloatParameterRequest() # DefaultPipingFloatParameterRequest |  (optional)

    try:
        api_response = api_instance.pipelines_float_parameter_update(id, default_piping_float_parameter_request=default_piping_float_parameter_request)
        print("The response of PipelinesApi->pipelines_float_parameter_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_float_parameter_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **default_piping_float_parameter_request** | [**DefaultPipingFloatParameterRequest**](DefaultPipingFloatParameterRequest.md)|  | [optional] 

### Return type

[**DefaultPipingFloatParameter**](DefaultPipingFloatParameter.md)

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

# **pipelines_integer_parameter_retrieve**
> DefaultPipingIntParameter pipelines_integer_parameter_retrieve(id)



A view for an integer default value for a plugin parameter in a pipeline's plugin piping.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.default_piping_int_parameter import DefaultPipingIntParameter
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.pipelines_integer_parameter_retrieve(id)
        print("The response of PipelinesApi->pipelines_integer_parameter_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_integer_parameter_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DefaultPipingIntParameter**](DefaultPipingIntParameter.md)

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

# **pipelines_integer_parameter_update**
> DefaultPipingIntParameter pipelines_integer_parameter_update(id, default_piping_int_parameter_request=default_piping_int_parameter_request)



A view for an integer default value for a plugin parameter in a pipeline's plugin piping.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.default_piping_int_parameter import DefaultPipingIntParameter
from chris_oag.models.default_piping_int_parameter_request import DefaultPipingIntParameterRequest
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 
    default_piping_int_parameter_request = chris_oag.DefaultPipingIntParameterRequest() # DefaultPipingIntParameterRequest |  (optional)

    try:
        api_response = api_instance.pipelines_integer_parameter_update(id, default_piping_int_parameter_request=default_piping_int_parameter_request)
        print("The response of PipelinesApi->pipelines_integer_parameter_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_integer_parameter_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **default_piping_int_parameter_request** | [**DefaultPipingIntParameterRequest**](DefaultPipingIntParameterRequest.md)|  | [optional] 

### Return type

[**DefaultPipingIntParameter**](DefaultPipingIntParameter.md)

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

# **pipelines_json_retrieve**
> PipelineCustomJson pipelines_json_retrieve(id)



A pipeline with a custom JSON view resembling the originally submitted pipeline data.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.pipeline_custom_json import PipelineCustomJson
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.pipelines_json_retrieve(id)
        print("The response of PipelinesApi->pipelines_json_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_json_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PipelineCustomJson**](PipelineCustomJson.md)

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

# **pipelines_list**
> PaginatedPipelineList pipelines_list(limit=limit, offset=offset)



A view for the collection of pipelines.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_pipeline_list import PaginatedPipelineList
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
    api_instance = chris_oag.PipelinesApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.pipelines_list(limit=limit, offset=offset)
        print("The response of PipelinesApi->pipelines_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPipelineList**](PaginatedPipelineList.md)

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

# **pipelines_parameters_list**
> PaginatedGenericDefaultPipingParameterList pipelines_parameters_list(id, limit=limit, offset=offset)



A view for the collection of pipeline-specific plugin parameters' defaults.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_generic_default_piping_parameter_list import PaginatedGenericDefaultPipingParameterList
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.pipelines_parameters_list(id, limit=limit, offset=offset)
        print("The response of PipelinesApi->pipelines_parameters_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_parameters_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedGenericDefaultPipingParameterList**](PaginatedGenericDefaultPipingParameterList.md)

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

# **pipelines_pipings_list**
> PaginatedPluginPipingList pipelines_pipings_list(id, limit=limit, offset=offset)



A view for the collection of pipeline-specific plugin pipings.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_plugin_piping_list import PaginatedPluginPipingList
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.pipelines_pipings_list(id, limit=limit, offset=offset)
        print("The response of PipelinesApi->pipelines_pipings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_pipings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPluginPipingList**](PaginatedPluginPipingList.md)

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

# **pipelines_pipings_retrieve**
> PluginPiping pipelines_pipings_retrieve(id)



A plugin piping view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.plugin_piping import PluginPiping
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.pipelines_pipings_retrieve(id)
        print("The response of PipelinesApi->pipelines_pipings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_pipings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PluginPiping**](PluginPiping.md)

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

# **pipelines_plugins_list**
> PaginatedPluginList pipelines_plugins_list(id, limit=limit, offset=offset)



A view for a pipeline-specific collection of plugins.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_plugin_list import PaginatedPluginList
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.pipelines_plugins_list(id, limit=limit, offset=offset)
        print("The response of PipelinesApi->pipelines_plugins_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_plugins_list: %s\n" % e)
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

# **pipelines_retrieve**
> Pipeline pipelines_retrieve(id)



A pipeline view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.pipeline import Pipeline
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.pipelines_retrieve(id)
        print("The response of PipelinesApi->pipelines_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Pipeline**](Pipeline.md)

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

# **pipelines_search_list**
> PaginatedPipelineList pipelines_search_list(authors=authors, category=category, description=description, id=id, limit=limit, max_creation_date=max_creation_date, min_creation_date=min_creation_date, name=name, offset=offset, owner_username=owner_username)



A view for the collection of pipelines resulting from a query search.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_pipeline_list import PaginatedPipelineList
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
    api_instance = chris_oag.PipelinesApi(api_client)
    authors = 'authors_example' # str |  (optional)
    category = 'category_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    max_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    min_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    name = 'name_example' # str |  (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    owner_username = 'owner_username_example' # str |  (optional)

    try:
        api_response = api_instance.pipelines_search_list(authors=authors, category=category, description=description, id=id, limit=limit, max_creation_date=max_creation_date, min_creation_date=min_creation_date, name=name, offset=offset, owner_username=owner_username)
        print("The response of PipelinesApi->pipelines_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authors** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **max_creation_date** | **datetime**|  | [optional] 
 **min_creation_date** | **datetime**|  | [optional] 
 **name** | **str**|  | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **owner_username** | **str**|  | [optional] 

### Return type

[**PaginatedPipelineList**](PaginatedPipelineList.md)

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

# **pipelines_sourcefiles_create**
> PipelineSourceFile pipelines_sourcefiles_create(pipeline_source_file_request)



A view for the collection of pipeline source files.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.pipeline_source_file import PipelineSourceFile
from chris_oag.models.pipeline_source_file_request import PipelineSourceFileRequest
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
    api_instance = chris_oag.PipelinesApi(api_client)
    pipeline_source_file_request = chris_oag.PipelineSourceFileRequest() # PipelineSourceFileRequest | 

    try:
        api_response = api_instance.pipelines_sourcefiles_create(pipeline_source_file_request)
        print("The response of PipelinesApi->pipelines_sourcefiles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_sourcefiles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_source_file_request** | [**PipelineSourceFileRequest**](PipelineSourceFileRequest.md)|  | 

### Return type

[**PipelineSourceFile**](PipelineSourceFile.md)

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

# **pipelines_sourcefiles_list**
> PaginatedPipelineSourceFileList pipelines_sourcefiles_list(limit=limit, offset=offset)



A view for the collection of pipeline source files.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_pipeline_source_file_list import PaginatedPipelineSourceFileList
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
    api_instance = chris_oag.PipelinesApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.pipelines_sourcefiles_list(limit=limit, offset=offset)
        print("The response of PipelinesApi->pipelines_sourcefiles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_sourcefiles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedPipelineSourceFileList**](PaginatedPipelineSourceFileList.md)

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

# **pipelines_sourcefiles_retrieve**
> PipelineSourceFile pipelines_sourcefiles_retrieve(id)



A pipeline source file view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.pipeline_source_file import PipelineSourceFile
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.pipelines_sourcefiles_retrieve(id)
        print("The response of PipelinesApi->pipelines_sourcefiles_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_sourcefiles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PipelineSourceFile**](PipelineSourceFile.md)

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

# **pipelines_sourcefiles_retrieve_0**
> bytearray pipelines_sourcefiles_retrieve_0(id)



Overriden to be able to make a GET request to an actual file resource.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.pipelines_sourcefiles_retrieve_0(id)
        print("The response of PipelinesApi->pipelines_sourcefiles_retrieve_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_sourcefiles_retrieve_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bytearray**

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_sourcefiles_search_list**
> PaginatedPipelineSourceFileList pipelines_sourcefiles_search_list(fname=fname, fname_exact=fname_exact, fname_icontains=fname_icontains, id=id, limit=limit, max_creation_date=max_creation_date, min_creation_date=min_creation_date, offset=offset, uploader_username=uploader_username)



A view for the collection of pipeline source files resulting from a query search.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_pipeline_source_file_list import PaginatedPipelineSourceFileList
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
    api_instance = chris_oag.PipelinesApi(api_client)
    fname = 'fname_example' # str |  (optional)
    fname_exact = 'fname_exact_example' # str |  (optional)
    fname_icontains = 'fname_icontains_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    max_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    min_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    uploader_username = 'uploader_username_example' # str |  (optional)

    try:
        api_response = api_instance.pipelines_sourcefiles_search_list(fname=fname, fname_exact=fname_exact, fname_icontains=fname_icontains, id=id, limit=limit, max_creation_date=max_creation_date, min_creation_date=min_creation_date, offset=offset, uploader_username=uploader_username)
        print("The response of PipelinesApi->pipelines_sourcefiles_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_sourcefiles_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fname** | **str**|  | [optional] 
 **fname_exact** | **str**|  | [optional] 
 **fname_icontains** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **max_creation_date** | **datetime**|  | [optional] 
 **min_creation_date** | **datetime**|  | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **uploader_username** | **str**|  | [optional] 

### Return type

[**PaginatedPipelineSourceFileList**](PaginatedPipelineSourceFileList.md)

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

# **pipelines_string_parameter_retrieve**
> DefaultPipingStrParameter pipelines_string_parameter_retrieve(id)



A view for a string default value for a plugin parameter in a pipeline's plugin piping.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.default_piping_str_parameter import DefaultPipingStrParameter
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.pipelines_string_parameter_retrieve(id)
        print("The response of PipelinesApi->pipelines_string_parameter_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_string_parameter_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DefaultPipingStrParameter**](DefaultPipingStrParameter.md)

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

# **pipelines_string_parameter_update**
> DefaultPipingStrParameter pipelines_string_parameter_update(id, default_piping_str_parameter_request=default_piping_str_parameter_request)



A view for a string default value for a plugin parameter in a pipeline's plugin piping.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.default_piping_str_parameter import DefaultPipingStrParameter
from chris_oag.models.default_piping_str_parameter_request import DefaultPipingStrParameterRequest
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 
    default_piping_str_parameter_request = chris_oag.DefaultPipingStrParameterRequest() # DefaultPipingStrParameterRequest |  (optional)

    try:
        api_response = api_instance.pipelines_string_parameter_update(id, default_piping_str_parameter_request=default_piping_str_parameter_request)
        print("The response of PipelinesApi->pipelines_string_parameter_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_string_parameter_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **default_piping_str_parameter_request** | [**DefaultPipingStrParameterRequest**](DefaultPipingStrParameterRequest.md)|  | [optional] 

### Return type

[**DefaultPipingStrParameter**](DefaultPipingStrParameter.md)

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

# **pipelines_update**
> Pipeline pipelines_update(id, pipeline_request)



A pipeline view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.pipeline import Pipeline
from chris_oag.models.pipeline_request import PipelineRequest
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 
    pipeline_request = chris_oag.PipelineRequest() # PipelineRequest | 

    try:
        api_response = api_instance.pipelines_update(id, pipeline_request)
        print("The response of PipelinesApi->pipelines_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **pipeline_request** | [**PipelineRequest**](PipelineRequest.md)|  | 

### Return type

[**Pipeline**](Pipeline.md)

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

# **pipelines_workflows_create**
> Workflow pipelines_workflows_create(id, workflow_request=workflow_request)



A view for the collection of pipeline-specific workflows.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.workflow import Workflow
from chris_oag.models.workflow_request import WorkflowRequest
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 
    workflow_request = chris_oag.WorkflowRequest() # WorkflowRequest |  (optional)

    try:
        api_response = api_instance.pipelines_workflows_create(id, workflow_request=workflow_request)
        print("The response of PipelinesApi->pipelines_workflows_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_workflows_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **workflow_request** | [**WorkflowRequest**](WorkflowRequest.md)|  | [optional] 

### Return type

[**Workflow**](Workflow.md)

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

# **pipelines_workflows_destroy**
> pipelines_workflows_destroy(id)



A workflow view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 

    try:
        api_instance.pipelines_workflows_destroy(id)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_workflows_destroy: %s\n" % e)
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

# **pipelines_workflows_plugininstances_list**
> PaginatedPluginInstanceList pipelines_workflows_plugininstances_list(id, limit=limit, offset=offset)



A view for the collection of plugin instances that compose the workflow.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_plugin_instance_list import PaginatedPluginInstanceList
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.pipelines_workflows_plugininstances_list(id, limit=limit, offset=offset)
        print("The response of PipelinesApi->pipelines_workflows_plugininstances_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_workflows_plugininstances_list: %s\n" % e)
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

# **pipelines_workflows_retrieve**
> Workflow pipelines_workflows_retrieve(id)



A workflow view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.workflow import Workflow
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.pipelines_workflows_retrieve(id)
        print("The response of PipelinesApi->pipelines_workflows_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_workflows_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Workflow**](Workflow.md)

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

# **pipelines_workflows_search_list**
> PaginatedWorkflowList pipelines_workflows_search_list(id=id, limit=limit, offset=offset, owner_username=owner_username, pipeline_name=pipeline_name, title=title)



A view for the collection of workflows resulting from a query search.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_workflow_list import PaginatedWorkflowList
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    owner_username = 'owner_username_example' # str |  (optional)
    pipeline_name = 'pipeline_name_example' # str |  (optional)
    title = 'title_example' # str |  (optional)

    try:
        api_response = api_instance.pipelines_workflows_search_list(id=id, limit=limit, offset=offset, owner_username=owner_username, pipeline_name=pipeline_name, title=title)
        print("The response of PipelinesApi->pipelines_workflows_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_workflows_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **owner_username** | **str**|  | [optional] 
 **pipeline_name** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 

### Return type

[**PaginatedWorkflowList**](PaginatedWorkflowList.md)

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

# **pipelines_workflows_update**
> Workflow pipelines_workflows_update(id, workflow_request=workflow_request)



A workflow view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.workflow import Workflow
from chris_oag.models.workflow_request import WorkflowRequest
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 
    workflow_request = chris_oag.WorkflowRequest() # WorkflowRequest |  (optional)

    try:
        api_response = api_instance.pipelines_workflows_update(id, workflow_request=workflow_request)
        print("The response of PipelinesApi->pipelines_workflows_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_workflows_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **workflow_request** | [**WorkflowRequest**](WorkflowRequest.md)|  | [optional] 

### Return type

[**Workflow**](Workflow.md)

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

# **workflows_list**
> PaginatedWorkflowList workflows_list(id, limit=limit, offset=offset)



A view for the collection of pipeline-specific workflows.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_workflow_list import PaginatedWorkflowList
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
    api_instance = chris_oag.PipelinesApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.workflows_list(id, limit=limit, offset=offset)
        print("The response of PipelinesApi->workflows_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->workflows_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedWorkflowList**](PaginatedWorkflowList.md)

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

