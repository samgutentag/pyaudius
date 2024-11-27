# pyaudius.ChallengesApi

All URIs are relative to *https://discoveryprovider.audius.co/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_undisbursed_challenges**](ChallengesApi.md#get_undisbursed_challenges) | **GET** /challenges/undisbursed | 


# **get_undisbursed_challenges**
> UndisbursedChallenges get_undisbursed_challenges(offset=offset, limit=limit, user_id=user_id, completed_blocknumber=completed_blocknumber)



Get all undisbursed challenges

### Example


```python
import pyaudius
from pyaudius.models.undisbursed_challenges import UndisbursedChallenges
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
    api_instance = pyaudius.ChallengesApi(api_client)
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | A User ID to filter the undisbursed challenges to a particular user (optional)
    completed_blocknumber = 56 # int | Starting blocknumber to retrieve completed undisbursed challenges (optional)

    try:
        api_response = api_instance.get_undisbursed_challenges(offset=offset, limit=limit, user_id=user_id, completed_blocknumber=completed_blocknumber)
        print("The response of ChallengesApi->get_undisbursed_challenges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChallengesApi->get_undisbursed_challenges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| A User ID to filter the undisbursed challenges to a particular user | [optional] 
 **completed_blocknumber** | **int**| Starting blocknumber to retrieve completed undisbursed challenges | [optional] 

### Return type

[**UndisbursedChallenges**](UndisbursedChallenges.md)

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

