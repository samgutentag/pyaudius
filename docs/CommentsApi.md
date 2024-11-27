# pyaudius.CommentsApi

All URIs are relative to *https://discoveryprovider.audius.co/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_comment_replies**](CommentsApi.md#get_comment_replies) | **GET** /comments/{comment_id}/replies | 
[**get_unclaimed_comment_id**](CommentsApi.md#get_unclaimed_comment_id) | **GET** /comments/unclaimed_id | 


# **get_comment_replies**
> CommentResponse get_comment_replies(comment_id, offset=offset, limit=limit, user_id=user_id)



Gets replies to a parent comment

### Example


```python
import pyaudius
from pyaudius.models.comment_response import CommentResponse
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
    api_instance = pyaudius.CommentsApi(api_client)
    comment_id = 'comment_id_example' # str | A Comment ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)

    try:
        api_response = api_instance.get_comment_replies(comment_id, offset=offset, limit=limit, user_id=user_id)
        print("The response of CommentsApi->get_comment_replies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->get_comment_replies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**| A Comment ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 

### Return type

[**CommentResponse**](CommentResponse.md)

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
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unclaimed_comment_id**
> UnclaimedIdResponse get_unclaimed_comment_id()



Gets an unclaimed blockchain comment ID

### Example


```python
import pyaudius
from pyaudius.models.unclaimed_id_response import UnclaimedIdResponse
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
    api_instance = pyaudius.CommentsApi(api_client)

    try:
        api_response = api_instance.get_unclaimed_comment_id()
        print("The response of CommentsApi->get_unclaimed_comment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->get_unclaimed_comment_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UnclaimedIdResponse**](UnclaimedIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

