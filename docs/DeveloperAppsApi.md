# pyaudius.DeveloperAppsApi

All URIs are relative to *https://discoveryprovider.audius.co/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_developer_app**](DeveloperAppsApi.md#get_developer_app) | **GET** /developer_apps/{address} | 


# **get_developer_app**
> DeveloperAppResponse get_developer_app(address)



Gets developer app matching given address (API key)

### Example


```python
import pyaudius
from pyaudius.models.developer_app_response import DeveloperAppResponse
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
    api_instance = pyaudius.DeveloperAppsApi(api_client)
    address = 'address_example' # str | A developer app address (API Key)

    try:
        api_response = api_instance.get_developer_app(address)
        print("The response of DeveloperAppsApi->get_developer_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperAppsApi->get_developer_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| A developer app address (API Key) | 

### Return type

[**DeveloperAppResponse**](DeveloperAppResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

