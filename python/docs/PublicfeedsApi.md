# chris_oag.PublicfeedsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publicfeeds_list**](PublicfeedsApi.md#publicfeeds_list) | **GET** /api/v1/publicfeeds/ | 
[**publicfeeds_search_list**](PublicfeedsApi.md#publicfeeds_search_list) | **GET** /api/v1/publicfeeds/search/ | 


# **publicfeeds_list**
> PaginatedFeedList publicfeeds_list(limit=limit, offset=offset)



A view for the collection of public feeds.

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
    api_instance = chris_oag.PublicfeedsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.publicfeeds_list(limit=limit, offset=offset)
        print("The response of PublicfeedsApi->publicfeeds_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicfeedsApi->publicfeeds_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **publicfeeds_search_list**
> PaginatedFeedList publicfeeds_search_list(files_fname_icontains=files_fname_icontains, id=id, limit=limit, max_creation_date=max_creation_date, max_id=max_id, min_creation_date=min_creation_date, min_id=min_id, name=name, name_exact=name_exact, name_startswith=name_startswith, offset=offset)



A view for the collection of public feeds resulting from a query search.

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
    api_instance = chris_oag.PublicfeedsApi(api_client)
    files_fname_icontains = 'files_fname_icontains_example' # str |  (optional)
    id = 56 # int |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    max_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    max_id = 56 # int |  (optional)
    min_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    min_id = 56 # int |  (optional)
    name = 'name_example' # str |  (optional)
    name_exact = 'name_exact_example' # str |  (optional)
    name_startswith = 'name_startswith_example' # str |  (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.publicfeeds_search_list(files_fname_icontains=files_fname_icontains, id=id, limit=limit, max_creation_date=max_creation_date, max_id=max_id, min_creation_date=min_creation_date, min_id=min_id, name=name, name_exact=name_exact, name_startswith=name_startswith, offset=offset)
        print("The response of PublicfeedsApi->publicfeeds_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicfeedsApi->publicfeeds_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files_fname_icontains** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **max_creation_date** | **datetime**|  | [optional] 
 **max_id** | **int**|  | [optional] 
 **min_creation_date** | **datetime**|  | [optional] 
 **min_id** | **int**|  | [optional] 
 **name** | **str**|  | [optional] 
 **name_exact** | **str**|  | [optional] 
 **name_startswith** | **str**|  | [optional] 
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

