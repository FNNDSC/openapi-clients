# chris_oag.TagsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feed_tags_list**](TagsApi.md#feed_tags_list) | **GET** /api/v1/{id}/tags/ | 
[**tags_create**](TagsApi.md#tags_create) | **POST** /api/v1/tags/ | 
[**tags_destroy**](TagsApi.md#tags_destroy) | **DELETE** /api/v1/tags/{id}/ | 
[**tags_feeds_list**](TagsApi.md#tags_feeds_list) | **GET** /api/v1/tags/{id}/feeds/ | 
[**tags_list**](TagsApi.md#tags_list) | **GET** /api/v1/tags/ | 
[**tags_retrieve**](TagsApi.md#tags_retrieve) | **GET** /api/v1/tags/{id}/ | 
[**tags_search_list**](TagsApi.md#tags_search_list) | **GET** /api/v1/tags/search/ | 
[**tags_taggings_create**](TagsApi.md#tags_taggings_create) | **POST** /api/v1/tags/{id}/taggings/ | 
[**tags_taggings_list**](TagsApi.md#tags_taggings_list) | **GET** /api/v1/tags/{id}/taggings/ | 
[**tags_update**](TagsApi.md#tags_update) | **PUT** /api/v1/tags/{id}/ | 


# **feed_tags_list**
> PaginatedTagList feed_tags_list(id, limit=limit, offset=offset)



A view for a feed-specific collection of user-specific tags.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_tag_list import PaginatedTagList
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
    api_instance = chris_oag.TagsApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.feed_tags_list(id, limit=limit, offset=offset)
        print("The response of TagsApi->feed_tags_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->feed_tags_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedTagList**](PaginatedTagList.md)

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

# **tags_create**
> Tag tags_create(tag_request)



A view for the collection of tags.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.tag import Tag
from chris_oag.models.tag_request import TagRequest
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
    api_instance = chris_oag.TagsApi(api_client)
    tag_request = chris_oag.TagRequest() # TagRequest | 

    try:
        api_response = api_instance.tags_create(tag_request)
        print("The response of TagsApi->tags_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_request** | [**TagRequest**](TagRequest.md)|  | 

### Return type

[**Tag**](Tag.md)

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

# **tags_destroy**
> tags_destroy(id)



A tag view.

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
    api_instance = chris_oag.TagsApi(api_client)
    id = 56 # int | 

    try:
        api_instance.tags_destroy(id)
    except Exception as e:
        print("Exception when calling TagsApi->tags_destroy: %s\n" % e)
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

# **tags_feeds_list**
> PaginatedFeedList tags_feeds_list(id, limit=limit, offset=offset)



A view for the tag-specific collection of feeds.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_feed_list import PaginatedFeedList
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
    api_instance = chris_oag.TagsApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.tags_feeds_list(id, limit=limit, offset=offset)
        print("The response of TagsApi->tags_feeds_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_feeds_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedFeedList**](PaginatedFeedList.md)

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

# **tags_list**
> PaginatedTagList tags_list(limit=limit, offset=offset)



A view for the collection of tags.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_tag_list import PaginatedTagList
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
    api_instance = chris_oag.TagsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.tags_list(limit=limit, offset=offset)
        print("The response of TagsApi->tags_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedTagList**](PaginatedTagList.md)

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

# **tags_retrieve**
> Tag tags_retrieve(id)



A tag view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.tag import Tag
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
    api_instance = chris_oag.TagsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.tags_retrieve(id)
        print("The response of TagsApi->tags_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Tag**](Tag.md)

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

# **tags_search_list**
> PaginatedTagList tags_search_list(color=color, id=id, limit=limit, name=name, offset=offset, owner_username=owner_username)



A view for the collection of tags resulting from a query search.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_tag_list import PaginatedTagList
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
    api_instance = chris_oag.TagsApi(api_client)
    color = 'color_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str |  (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    owner_username = 'owner_username_example' # str |  (optional)

    try:
        api_response = api_instance.tags_search_list(color=color, id=id, limit=limit, name=name, offset=offset, owner_username=owner_username)
        print("The response of TagsApi->tags_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **color** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**|  | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **owner_username** | **str**|  | [optional] 

### Return type

[**PaginatedTagList**](PaginatedTagList.md)

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

# **tags_taggings_create**
> Tagging tags_taggings_create(id)



A view for the collection of tag-specific taggings.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.tagging import Tagging
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
    api_instance = chris_oag.TagsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.tags_taggings_create(id)
        print("The response of TagsApi->tags_taggings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_taggings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Tagging**](Tagging.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_taggings_list**
> PaginatedTaggingList tags_taggings_list(id, limit=limit, offset=offset)



A view for the collection of tag-specific taggings.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.paginated_tagging_list import PaginatedTaggingList
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
    api_instance = chris_oag.TagsApi(api_client)
    id = 56 # int | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.tags_taggings_list(id, limit=limit, offset=offset)
        print("The response of TagsApi->tags_taggings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_taggings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedTaggingList**](PaginatedTaggingList.md)

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

# **tags_update**
> Tag tags_update(id, tag_request)



A tag view.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import chris_oag
from chris_oag.models.tag import Tag
from chris_oag.models.tag_request import TagRequest
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
    api_instance = chris_oag.TagsApi(api_client)
    id = 56 # int | 
    tag_request = chris_oag.TagRequest() # TagRequest | 

    try:
        api_response = api_instance.tags_update(id, tag_request)
        print("The response of TagsApi->tags_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tag_request** | [**TagRequest**](TagRequest.md)|  | 

### Return type

[**Tag**](Tag.md)

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

