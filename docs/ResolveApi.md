# pyaudius.ResolveApi

All URIs are relative to *https://discoveryprovider.audius.co/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolve**](ResolveApi.md#resolve) | **GET** /resolve | Resolves and redirects a provided Audius app URL to the API resource URL it represents


# **resolve**
> resolve(url)

Resolves and redirects a provided Audius app URL to the API resource URL it represents

This endpoint allows you to lookup and access API resources when you only know the audius.co URL. Tracks, Playlists, and Users are supported.

### Example


```python
import pyaudius
from pyaudius.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discoveryprovider.audius.co/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pyaudius.Configuration(
    host = "https://discoveryprovider.audius.co/v1"
)


# Enter a context with an instance of the API client
with pyaudius.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyaudius.ResolveApi(api_client)
    url = 'url_example' # str | URL to resolve. Either fully formed URL (https://audius.co) or just the absolute path

    try:
        # Resolves and redirects a provided Audius app URL to the API resource URL it represents
        api_instance.resolve(url)
    except Exception as e:
        print("Exception when calling ResolveApi->resolve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| URL to resolve. Either fully formed URL (https://audius.co) or just the absolute path | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Internal redirect |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

