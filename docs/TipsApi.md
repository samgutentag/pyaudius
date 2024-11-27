# pyaudius.TipsApi

All URIs are relative to *https://discoveryprovider.audius.co/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tips**](TipsApi.md#get_tips) | **GET** /tips | 


# **get_tips**
> GetTipsResponse get_tips(offset=offset, limit=limit, user_id=user_id, receiver_min_followers=receiver_min_followers, receiver_is_verified=receiver_is_verified, current_user_follows=current_user_follows, unique_by=unique_by)



Gets the most recent tips on the network

### Example


```python
import pyaudius
from pyaudius.models.get_tips_response import GetTipsResponse
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
    api_instance = pyaudius.TipsApi(api_client)
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    receiver_min_followers = 0 # int | Only include tips to recipients that have this many followers (optional) (default to 0)
    receiver_is_verified = False # bool | Only include tips to recipients that are verified (optional) (default to False)
    current_user_follows = 'current_user_follows_example' # str | Only include tips involving the user's followers in the given capacity. Requires user_id to be set. (optional)
    unique_by = 'unique_by_example' # str | Only include the most recent tip for a user was involved in the given capacity.  Eg. 'sender' will ensure that each tip returned has a unique sender, using the most recent tip sent by a user if that user has sent multiple tips.      (optional)

    try:
        api_response = api_instance.get_tips(offset=offset, limit=limit, user_id=user_id, receiver_min_followers=receiver_min_followers, receiver_is_verified=receiver_is_verified, current_user_follows=current_user_follows, unique_by=unique_by)
        print("The response of TipsApi->get_tips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TipsApi->get_tips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **receiver_min_followers** | **int**| Only include tips to recipients that have this many followers | [optional] [default to 0]
 **receiver_is_verified** | **bool**| Only include tips to recipients that are verified | [optional] [default to False]
 **current_user_follows** | **str**| Only include tips involving the user&#39;s followers in the given capacity. Requires user_id to be set. | [optional] 
 **unique_by** | **str**| Only include the most recent tip for a user was involved in the given capacity.  Eg. &#39;sender&#39; will ensure that each tip returned has a unique sender, using the most recent tip sent by a user if that user has sent multiple tips.      | [optional] 

### Return type

[**GetTipsResponse**](GetTipsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

