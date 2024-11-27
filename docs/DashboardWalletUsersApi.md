# pyaudius.DashboardWalletUsersApi

All URIs are relative to *https://discoveryprovider.audius.co/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_get_dashboard_wallet_users**](DashboardWalletUsersApi.md#bulk_get_dashboard_wallet_users) | **GET** /dashboard_wallet_users | 


# **bulk_get_dashboard_wallet_users**
> DashboardWalletUsersResponse bulk_get_dashboard_wallet_users(wallets)



Gets Audius user profiles connected to given dashboard wallet addresses

### Example


```python
import pyaudius
from pyaudius.models.dashboard_wallet_users_response import DashboardWalletUsersResponse
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
    api_instance = pyaudius.DashboardWalletUsersApi(api_client)
    wallets = ['wallets_example'] # List[str] | The wallets for which to fetch connected Audius user profiles.

    try:
        api_response = api_instance.bulk_get_dashboard_wallet_users(wallets)
        print("The response of DashboardWalletUsersApi->bulk_get_dashboard_wallet_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardWalletUsersApi->bulk_get_dashboard_wallet_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallets** | [**List[str]**](str.md)| The wallets for which to fetch connected Audius user profiles. | 

### Return type

[**DashboardWalletUsersResponse**](DashboardWalletUsersResponse.md)

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
**404** | No such dashboard wallets |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

