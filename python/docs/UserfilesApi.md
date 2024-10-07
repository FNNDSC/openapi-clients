# chris_oag.UserfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userfiles_create**](UserfilesApi.md#userfiles_create) | **POST** /api/v1/userfiles/ | 
[**userfiles_destroy**](UserfilesApi.md#userfiles_destroy) | **DELETE** /api/v1/userfiles/{id}/ | 
[**userfiles_list**](UserfilesApi.md#userfiles_list) | **GET** /api/v1/userfiles/ | 
[**userfiles_retrieve**](UserfilesApi.md#userfiles_retrieve) | **GET** /api/v1/userfiles/{id}/ | 
[**userfiles_retrieve_0**](UserfilesApi.md#userfiles_retrieve_0) | **GET** /api/v1/userfiles/{id}/. | 
[**userfiles_search_list**](UserfilesApi.md#userfiles_search_list) | **GET** /api/v1/userfiles/search/ | 
[**userfiles_update**](UserfilesApi.md#userfiles_update) | **PUT** /api/v1/userfiles/{id}/ | 


# **userfiles_create**
> UserFile userfiles_create(user_file_request=user_file_request)



A view for the collection of user files.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.user_file import UserFile
from chris_oag.models.user_file_request import UserFileRequest
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
    api_instance = chris_oag.UserfilesApi(api_client)
    user_file_request = chris_oag.UserFileRequest() # UserFileRequest |  (optional)

    try:
        api_response = api_instance.userfiles_create(user_file_request=user_file_request)
        print("The response of UserfilesApi->userfiles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserfilesApi->userfiles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_file_request** | [**UserFileRequest**](UserFileRequest.md)|  | [optional] 

### Return type

[**UserFile**](UserFile.md)

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

# **userfiles_destroy**
> userfiles_destroy(id)



A user file view.

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
    api_instance = chris_oag.UserfilesApi(api_client)
    id = 56 # int | 

    try:
        api_instance.userfiles_destroy(id)
    except Exception as e:
        print("Exception when calling UserfilesApi->userfiles_destroy: %s\n" % e)
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

# **userfiles_list**
> PaginatedUserFileList userfiles_list(limit=limit, offset=offset)



A view for the collection of user files.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_user_file_list import PaginatedUserFileList
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
    api_instance = chris_oag.UserfilesApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.userfiles_list(limit=limit, offset=offset)
        print("The response of UserfilesApi->userfiles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserfilesApi->userfiles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedUserFileList**](PaginatedUserFileList.md)

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

# **userfiles_retrieve**
> UserFile userfiles_retrieve(id)



A user file view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.user_file import UserFile
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
    api_instance = chris_oag.UserfilesApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.userfiles_retrieve(id)
        print("The response of UserfilesApi->userfiles_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserfilesApi->userfiles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UserFile**](UserFile.md)

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

# **userfiles_retrieve_0**
> bytearray userfiles_retrieve_0(id)



Overriden to be able to make a GET request to an actual file resource.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (DownloadTokenInQueryString):

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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: DownloadTokenInQueryString
configuration.api_key['DownloadTokenInQueryString'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['DownloadTokenInQueryString'] = 'Bearer'

# Enter a context with an instance of the API client
with chris_oag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = chris_oag.UserfilesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.userfiles_retrieve_0(id)
        print("The response of UserfilesApi->userfiles_retrieve_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserfilesApi->userfiles_retrieve_0: %s\n" % e)
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

# **userfiles_search_list**
> PaginatedUserFileList userfiles_search_list(fname=fname, fname_exact=fname_exact, fname_icontains=fname_icontains, fname_icontains_multiple=fname_icontains_multiple, fname_nslashes=fname_nslashes, id=id, limit=limit, max_creation_date=max_creation_date, min_creation_date=min_creation_date, offset=offset, owner_username=owner_username)



A view for the collection of user files resulting from a query search.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_user_file_list import PaginatedUserFileList
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
    api_instance = chris_oag.UserfilesApi(api_client)
    fname = 'fname_example' # str |  (optional)
    fname_exact = 'fname_exact_example' # str |  (optional)
    fname_icontains = 'fname_icontains_example' # str |  (optional)
    fname_icontains_multiple = 'fname_icontains_multiple_example' # str |  (optional)
    fname_nslashes = 'fname_nslashes_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    max_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    min_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    owner_username = 'owner_username_example' # str |  (optional)

    try:
        api_response = api_instance.userfiles_search_list(fname=fname, fname_exact=fname_exact, fname_icontains=fname_icontains, fname_icontains_multiple=fname_icontains_multiple, fname_nslashes=fname_nslashes, id=id, limit=limit, max_creation_date=max_creation_date, min_creation_date=min_creation_date, offset=offset, owner_username=owner_username)
        print("The response of UserfilesApi->userfiles_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserfilesApi->userfiles_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fname** | **str**|  | [optional] 
 **fname_exact** | **str**|  | [optional] 
 **fname_icontains** | **str**|  | [optional] 
 **fname_icontains_multiple** | **str**|  | [optional] 
 **fname_nslashes** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **max_creation_date** | **datetime**|  | [optional] 
 **min_creation_date** | **datetime**|  | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **owner_username** | **str**|  | [optional] 

### Return type

[**PaginatedUserFileList**](PaginatedUserFileList.md)

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

# **userfiles_update**
> UserFile userfiles_update(id, user_file_request=user_file_request)



A user file view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.user_file import UserFile
from chris_oag.models.user_file_request import UserFileRequest
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
    api_instance = chris_oag.UserfilesApi(api_client)
    id = 56 # int | 
    user_file_request = chris_oag.UserFileRequest() # UserFileRequest |  (optional)

    try:
        api_response = api_instance.userfiles_update(id, user_file_request=user_file_request)
        print("The response of UserfilesApi->userfiles_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserfilesApi->userfiles_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **user_file_request** | [**UserFileRequest**](UserFileRequest.md)|  | [optional] 

### Return type

[**UserFile**](UserFile.md)

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

