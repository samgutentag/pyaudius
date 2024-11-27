# pyaudius.UsersApi

All URIs are relative to *https://discoveryprovider.audius.co/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_purchases_as_csv**](UsersApi.md#download_purchases_as_csv) | **GET** /users/{id}/purchases/download | 
[**download_sales_as_csv**](UsersApi.md#download_sales_as_csv) | **GET** /users/{id}/sales/download | 
[**download_sales_as_json**](UsersApi.md#download_sales_as_json) | **GET** /users/{id}/sales/download/json | 
[**download_usdc_withdrawals_as_csv**](UsersApi.md#download_usdc_withdrawals_as_csv) | **GET** /users/{id}/withdrawals/download | 
[**get_ai_attributed_tracks_by_user_handle**](UsersApi.md#get_ai_attributed_tracks_by_user_handle) | **GET** /users/handle/{handle}/tracks/ai_attributed | 
[**get_albums_by_user**](UsersApi.md#get_albums_by_user) | **GET** /users/{id}/albums | 
[**get_authorized_apps**](UsersApi.md#get_authorized_apps) | **GET** /users/{id}/authorized_apps | 
[**get_bulk_users**](UsersApi.md#get_bulk_users) | **GET** /users | 
[**get_connected_wallets**](UsersApi.md#get_connected_wallets) | **GET** /users/{id}/connected_wallets | 
[**get_developer_apps**](UsersApi.md#get_developer_apps) | **GET** /users/{id}/developer_apps | 
[**get_favorites**](UsersApi.md#get_favorites) | **GET** /users/{id}/favorites | 
[**get_followers**](UsersApi.md#get_followers) | **GET** /users/{id}/followers | 
[**get_following**](UsersApi.md#get_following) | **GET** /users/{id}/following | 
[**get_muted_users**](UsersApi.md#get_muted_users) | **GET** /users/{id}/muted | 
[**get_playlists_by_user**](UsersApi.md#get_playlists_by_user) | **GET** /users/{id}/playlists | 
[**get_purchasers**](UsersApi.md#get_purchasers) | **GET** /users/{id}/purchasers | 
[**get_related_users**](UsersApi.md#get_related_users) | **GET** /users/{id}/related | 
[**get_remixers**](UsersApi.md#get_remixers) | **GET** /users/{id}/remixers | 
[**get_reposts**](UsersApi.md#get_reposts) | **GET** /users/{id}/reposts | 
[**get_sales_aggregate**](UsersApi.md#get_sales_aggregate) | **GET** /users/{id}/sales/aggregate | 
[**get_subscribers**](UsersApi.md#get_subscribers) | **GET** /users/{id}/subscribers | 
[**get_supported_users**](UsersApi.md#get_supported_users) | **GET** /users/{id}/supporting | 
[**get_supporters**](UsersApi.md#get_supporters) | **GET** /users/{id}/supporters | 
[**get_top_track_tags**](UsersApi.md#get_top_track_tags) | **GET** /users/{id}/tags | Fetch most used tags in a user&#39;s tracks
[**get_tracks_by_user**](UsersApi.md#get_tracks_by_user) | **GET** /users/{id}/tracks | 
[**get_user**](UsersApi.md#get_user) | **GET** /users/{id} | 
[**get_user_by_handle**](UsersApi.md#get_user_by_handle) | **GET** /users/handle/{handle} | 
[**get_user_challenges**](UsersApi.md#get_user_challenges) | **GET** /users/{id}/challenges | 
[**get_user_id_from_wallet**](UsersApi.md#get_user_id_from_wallet) | **GET** /users/id | 
[**get_user_tracks_remixed**](UsersApi.md#get_user_tracks_remixed) | **GET** /users/{id}/tracks/remixed | 
[**search_users**](UsersApi.md#search_users) | **GET** /users/search | 
[**verify_id_token**](UsersApi.md#verify_id_token) | **GET** /users/verify_token | 


# **download_purchases_as_csv**
> download_purchases_as_csv(id, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)



Downloads the purchases the user has made as a CSV file

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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    encoded_data_message = 'encoded_data_message_example' # str | The data that was signed by the user for signature recovery (optional)
    encoded_data_signature = 'encoded_data_signature_example' # str | The signature of data, used for signature recovery (optional)

    try:
        api_instance.download_purchases_as_csv(id, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)
    except Exception as e:
        print("Exception when calling UsersApi->download_purchases_as_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **encoded_data_message** | **str**| The data that was signed by the user for signature recovery | [optional] 
 **encoded_data_signature** | **str**| The signature of data, used for signature recovery | [optional] 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_sales_as_csv**
> download_sales_as_csv(id, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)



Downloads the sales the user has made as a CSV file

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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    encoded_data_message = 'encoded_data_message_example' # str | The data that was signed by the user for signature recovery (optional)
    encoded_data_signature = 'encoded_data_signature_example' # str | The signature of data, used for signature recovery (optional)

    try:
        api_instance.download_sales_as_csv(id, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)
    except Exception as e:
        print("Exception when calling UsersApi->download_sales_as_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **encoded_data_message** | **str**| The data that was signed by the user for signature recovery | [optional] 
 **encoded_data_signature** | **str**| The signature of data, used for signature recovery | [optional] 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_sales_as_json**
> download_sales_as_json(id, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)



Gets the sales data for the user in JSON format

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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    encoded_data_message = 'encoded_data_message_example' # str | The data that was signed by the user for signature recovery (optional)
    encoded_data_signature = 'encoded_data_signature_example' # str | The signature of data, used for signature recovery (optional)

    try:
        api_instance.download_sales_as_json(id, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)
    except Exception as e:
        print("Exception when calling UsersApi->download_sales_as_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **encoded_data_message** | **str**| The data that was signed by the user for signature recovery | [optional] 
 **encoded_data_signature** | **str**| The signature of data, used for signature recovery | [optional] 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_usdc_withdrawals_as_csv**
> download_usdc_withdrawals_as_csv(id, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)



Downloads the USDC withdrawals the user has made as a CSV file

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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    encoded_data_message = 'encoded_data_message_example' # str | The data that was signed by the user for signature recovery (optional)
    encoded_data_signature = 'encoded_data_signature_example' # str | The signature of data, used for signature recovery (optional)

    try:
        api_instance.download_usdc_withdrawals_as_csv(id, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)
    except Exception as e:
        print("Exception when calling UsersApi->download_usdc_withdrawals_as_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **encoded_data_message** | **str**| The data that was signed by the user for signature recovery | [optional] 
 **encoded_data_signature** | **str**| The signature of data, used for signature recovery | [optional] 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_attributed_tracks_by_user_handle**
> TracksResponse get_ai_attributed_tracks_by_user_handle(handle, offset=offset, limit=limit, user_id=user_id, sort=sort, query=query, sort_method=sort_method, sort_direction=sort_direction, filter_tracks=filter_tracks, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)



Gets the AI generated tracks attributed to a user using the user's handle

### Example


```python
import pyaudius
from pyaudius.models.tracks_response import TracksResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    handle = 'handle_example' # str | A User handle
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    sort = date # str | [Deprecated] Field to sort by (optional) (default to date)
    query = 'query_example' # str | The filter query (optional)
    sort_method = 'sort_method_example' # str | The sort method (optional)
    sort_direction = 'sort_direction_example' # str | The sort direction (optional)
    filter_tracks = all # str | Filter by unlisted or public tracks (optional) (default to all)
    encoded_data_message = 'encoded_data_message_example' # str | The data that was signed by the user for signature recovery (optional)
    encoded_data_signature = 'encoded_data_signature_example' # str | The signature of data, used for signature recovery (optional)

    try:
        api_response = api_instance.get_ai_attributed_tracks_by_user_handle(handle, offset=offset, limit=limit, user_id=user_id, sort=sort, query=query, sort_method=sort_method, sort_direction=sort_direction, filter_tracks=filter_tracks, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)
        print("The response of UsersApi->get_ai_attributed_tracks_by_user_handle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_ai_attributed_tracks_by_user_handle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**| A User handle | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **sort** | **str**| [Deprecated] Field to sort by | [optional] [default to date]
 **query** | **str**| The filter query | [optional] 
 **sort_method** | **str**| The sort method | [optional] 
 **sort_direction** | **str**| The sort direction | [optional] 
 **filter_tracks** | **str**| Filter by unlisted or public tracks | [optional] [default to all]
 **encoded_data_message** | **str**| The data that was signed by the user for signature recovery | [optional] 
 **encoded_data_signature** | **str**| The signature of data, used for signature recovery | [optional] 

### Return type

[**TracksResponse**](TracksResponse.md)

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

# **get_albums_by_user**
> AlbumsResponse get_albums_by_user(id, offset=offset, limit=limit, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)



Gets the albums created by a user using their user ID

### Example


```python
import pyaudius
from pyaudius.models.albums_response import AlbumsResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    encoded_data_message = 'encoded_data_message_example' # str | The data that was signed by the user for signature recovery (optional)
    encoded_data_signature = 'encoded_data_signature_example' # str | The signature of data, used for signature recovery (optional)

    try:
        api_response = api_instance.get_albums_by_user(id, offset=offset, limit=limit, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)
        print("The response of UsersApi->get_albums_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_albums_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **encoded_data_message** | **str**| The data that was signed by the user for signature recovery | [optional] 
 **encoded_data_signature** | **str**| The signature of data, used for signature recovery | [optional] 

### Return type

[**AlbumsResponse**](AlbumsResponse.md)

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

# **get_authorized_apps**
> AuthorizedApps get_authorized_apps(id)



Get the apps that user has authorized to write to their account

### Example


```python
import pyaudius
from pyaudius.models.authorized_apps import AuthorizedApps
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID

    try:
        api_response = api_instance.get_authorized_apps(id)
        print("The response of UsersApi->get_authorized_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_authorized_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 

### Return type

[**AuthorizedApps**](AuthorizedApps.md)

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

# **get_bulk_users**
> UsersResponse get_bulk_users(user_id=user_id, id=id)



Gets a list of users by ID

### Example


```python
import pyaudius
from pyaudius.models.users_response import UsersResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    id = ['id_example'] # List[str] | The ID of the user(s) (optional)

    try:
        api_response = api_instance.get_bulk_users(user_id=user_id, id=id)
        print("The response of UsersApi->get_bulk_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_bulk_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **id** | [**List[str]**](str.md)| The ID of the user(s) | [optional] 

### Return type

[**UsersResponse**](UsersResponse.md)

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

# **get_connected_wallets**
> ConnectedWalletsResponse get_connected_wallets(id)



Get the User's ERC and SPL connected wallets

### Example


```python
import pyaudius
from pyaudius.models.connected_wallets_response import ConnectedWalletsResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID

    try:
        api_response = api_instance.get_connected_wallets(id)
        print("The response of UsersApi->get_connected_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_connected_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 

### Return type

[**ConnectedWalletsResponse**](ConnectedWalletsResponse.md)

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

# **get_developer_apps**
> DeveloperApps get_developer_apps(id)



Gets the developer apps that the user owns

### Example


```python
import pyaudius
from pyaudius.models.developer_apps import DeveloperApps
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID

    try:
        api_response = api_instance.get_developer_apps(id)
        print("The response of UsersApi->get_developer_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_developer_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 

### Return type

[**DeveloperApps**](DeveloperApps.md)

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

# **get_favorites**
> FavoritesResponse get_favorites(id)



Gets a user's favorite tracks

### Example


```python
import pyaudius
from pyaudius.models.favorites_response import FavoritesResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID

    try:
        api_response = api_instance.get_favorites(id)
        print("The response of UsersApi->get_favorites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_favorites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 

### Return type

[**FavoritesResponse**](FavoritesResponse.md)

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

# **get_followers**
> FollowersResponse get_followers(id, offset=offset, limit=limit, user_id=user_id)



All users that follow the provided user

### Example


```python
import pyaudius
from pyaudius.models.followers_response import FollowersResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)

    try:
        api_response = api_instance.get_followers(id, offset=offset, limit=limit, user_id=user_id)
        print("The response of UsersApi->get_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_followers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 

### Return type

[**FollowersResponse**](FollowersResponse.md)

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

# **get_following**
> FollowingResponse get_following(id, offset=offset, limit=limit, user_id=user_id)



All users that the provided user follows

### Example


```python
import pyaudius
from pyaudius.models.following_response import FollowingResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)

    try:
        api_response = api_instance.get_following(id, offset=offset, limit=limit, user_id=user_id)
        print("The response of UsersApi->get_following:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_following: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 

### Return type

[**FollowingResponse**](FollowingResponse.md)

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

# **get_muted_users**
> UsersResponse get_muted_users(id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)



Gets users muted by the given user

### Example


```python
import pyaudius
from pyaudius.models.users_response import UsersResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    encoded_data_message = 'encoded_data_message_example' # str | The data that was signed by the user for signature recovery (optional)
    encoded_data_signature = 'encoded_data_signature_example' # str | The signature of data, used for signature recovery (optional)

    try:
        api_response = api_instance.get_muted_users(id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)
        print("The response of UsersApi->get_muted_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_muted_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **encoded_data_message** | **str**| The data that was signed by the user for signature recovery | [optional] 
 **encoded_data_signature** | **str**| The signature of data, used for signature recovery | [optional] 

### Return type

[**UsersResponse**](UsersResponse.md)

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

# **get_playlists_by_user**
> PlaylistsResponse get_playlists_by_user(id, offset=offset, limit=limit, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)



Gets the playlists created by a user using their user ID

### Example


```python
import pyaudius
from pyaudius.models.playlists_response import PlaylistsResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    encoded_data_message = 'encoded_data_message_example' # str | The data that was signed by the user for signature recovery (optional)
    encoded_data_signature = 'encoded_data_signature_example' # str | The signature of data, used for signature recovery (optional)

    try:
        api_response = api_instance.get_playlists_by_user(id, offset=offset, limit=limit, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)
        print("The response of UsersApi->get_playlists_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_playlists_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **encoded_data_message** | **str**| The data that was signed by the user for signature recovery | [optional] 
 **encoded_data_signature** | **str**| The signature of data, used for signature recovery | [optional] 

### Return type

[**PlaylistsResponse**](PlaylistsResponse.md)

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

# **get_purchasers**
> PurchasersResponse get_purchasers(id, offset=offset, limit=limit, user_id=user_id, content_type=content_type, content_id=content_id)



Gets the list of unique users who have purchased content by the given user

### Example


```python
import pyaudius
from pyaudius.models.purchasers_response import PurchasersResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    content_type = 'content_type_example' # str | Type of content to filter by (track or album) (optional)
    content_id = 'content_id_example' # str | Filters for users who have purchased the given track or album ID (optional)

    try:
        api_response = api_instance.get_purchasers(id, offset=offset, limit=limit, user_id=user_id, content_type=content_type, content_id=content_id)
        print("The response of UsersApi->get_purchasers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_purchasers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **content_type** | **str**| Type of content to filter by (track or album) | [optional] 
 **content_id** | **str**| Filters for users who have purchased the given track or album ID | [optional] 

### Return type

[**PurchasersResponse**](PurchasersResponse.md)

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

# **get_related_users**
> RelatedArtistResponse get_related_users(id, offset=offset, limit=limit, user_id=user_id)



Gets a list of users that might be of interest to followers of this user.

### Example


```python
import pyaudius
from pyaudius.models.related_artist_response import RelatedArtistResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)

    try:
        api_response = api_instance.get_related_users(id, offset=offset, limit=limit, user_id=user_id)
        print("The response of UsersApi->get_related_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_related_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 

### Return type

[**RelatedArtistResponse**](RelatedArtistResponse.md)

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

# **get_remixers**
> RemixersResponse get_remixers(id, offset=offset, limit=limit, user_id=user_id, track_id=track_id)



Gets the list of unique users who have remixed tracks by the given user, or a specific track by that user if provided

### Example


```python
import pyaudius
from pyaudius.models.remixers_response import RemixersResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    track_id = 'track_id_example' # str | Filters for remixers who have remixed the given track ID (optional)

    try:
        api_response = api_instance.get_remixers(id, offset=offset, limit=limit, user_id=user_id, track_id=track_id)
        print("The response of UsersApi->get_remixers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_remixers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **track_id** | **str**| Filters for remixers who have remixed the given track ID | [optional] 

### Return type

[**RemixersResponse**](RemixersResponse.md)

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

# **get_reposts**
> Reposts get_reposts(id, offset=offset, limit=limit, user_id=user_id)



Gets the given user's reposts

### Example


```python
import pyaudius
from pyaudius.models.reposts import Reposts
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)

    try:
        api_response = api_instance.get_reposts(id, offset=offset, limit=limit, user_id=user_id)
        print("The response of UsersApi->get_reposts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_reposts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 

### Return type

[**Reposts**](Reposts.md)

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

# **get_sales_aggregate**
> SalesAggregateResponse get_sales_aggregate(id, offset=offset, limit=limit, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)



Gets the aggregated sales data for the user

### Example


```python
import pyaudius
from pyaudius.models.sales_aggregate_response import SalesAggregateResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    encoded_data_message = 'encoded_data_message_example' # str | The data that was signed by the user for signature recovery (optional)
    encoded_data_signature = 'encoded_data_signature_example' # str | The signature of data, used for signature recovery (optional)

    try:
        api_response = api_instance.get_sales_aggregate(id, offset=offset, limit=limit, user_id=user_id, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)
        print("The response of UsersApi->get_sales_aggregate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_sales_aggregate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **encoded_data_message** | **str**| The data that was signed by the user for signature recovery | [optional] 
 **encoded_data_signature** | **str**| The signature of data, used for signature recovery | [optional] 

### Return type

[**SalesAggregateResponse**](SalesAggregateResponse.md)

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

# **get_subscribers**
> SubscribersResponse get_subscribers(id, offset=offset, limit=limit, user_id=user_id)



All users that subscribe to the provided user

### Example


```python
import pyaudius
from pyaudius.models.subscribers_response import SubscribersResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)

    try:
        api_response = api_instance.get_subscribers(id, offset=offset, limit=limit, user_id=user_id)
        print("The response of UsersApi->get_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 

### Return type

[**SubscribersResponse**](SubscribersResponse.md)

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

# **get_supported_users**
> GetSupportedUsers get_supported_users(id, offset=offset, limit=limit)



Gets the users that the given user supports

### Example


```python
import pyaudius
from pyaudius.models.get_supported_users import GetSupportedUsers
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)

    try:
        api_response = api_instance.get_supported_users(id, offset=offset, limit=limit)
        print("The response of UsersApi->get_supported_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_supported_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 

### Return type

[**GetSupportedUsers**](GetSupportedUsers.md)

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

# **get_supporters**
> GetSupporters get_supporters(id, offset=offset, limit=limit)



Gets the supporters of the given user

### Example


```python
import pyaudius
from pyaudius.models.get_supporters import GetSupporters
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)

    try:
        api_response = api_instance.get_supporters(id, offset=offset, limit=limit)
        print("The response of UsersApi->get_supporters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_supporters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 

### Return type

[**GetSupporters**](GetSupporters.md)

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

# **get_top_track_tags**
> TagsResponse get_top_track_tags(id, limit=limit, user_id=user_id)

Fetch most used tags in a user's tracks

Gets the most used track tags by a user.

### Example


```python
import pyaudius
from pyaudius.models.tags_response import TagsResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)

    try:
        # Fetch most used tags in a user's tracks
        api_response = api_instance.get_top_track_tags(id, limit=limit, user_id=user_id)
        print("The response of UsersApi->get_top_track_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_top_track_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 

### Return type

[**TagsResponse**](TagsResponse.md)

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

# **get_tracks_by_user**
> TracksResponse get_tracks_by_user(id, offset=offset, limit=limit, user_id=user_id, sort=sort, query=query, sort_method=sort_method, sort_direction=sort_direction, filter_tracks=filter_tracks, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)



Gets the tracks created by a user using their user ID

### Example


```python
import pyaudius
from pyaudius.models.tracks_response import TracksResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    sort = date # str | [Deprecated] Field to sort by (optional) (default to date)
    query = 'query_example' # str | The filter query (optional)
    sort_method = 'sort_method_example' # str | The sort method (optional)
    sort_direction = 'sort_direction_example' # str | The sort direction (optional)
    filter_tracks = all # str | Filter by unlisted or public tracks (optional) (default to all)
    encoded_data_message = 'encoded_data_message_example' # str | The data that was signed by the user for signature recovery (optional)
    encoded_data_signature = 'encoded_data_signature_example' # str | The signature of data, used for signature recovery (optional)

    try:
        api_response = api_instance.get_tracks_by_user(id, offset=offset, limit=limit, user_id=user_id, sort=sort, query=query, sort_method=sort_method, sort_direction=sort_direction, filter_tracks=filter_tracks, encoded_data_message=encoded_data_message, encoded_data_signature=encoded_data_signature)
        print("The response of UsersApi->get_tracks_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_tracks_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **sort** | **str**| [Deprecated] Field to sort by | [optional] [default to date]
 **query** | **str**| The filter query | [optional] 
 **sort_method** | **str**| The sort method | [optional] 
 **sort_direction** | **str**| The sort direction | [optional] 
 **filter_tracks** | **str**| Filter by unlisted or public tracks | [optional] [default to all]
 **encoded_data_message** | **str**| The data that was signed by the user for signature recovery | [optional] 
 **encoded_data_signature** | **str**| The signature of data, used for signature recovery | [optional] 

### Return type

[**TracksResponse**](TracksResponse.md)

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

# **get_user**
> UserResponse get_user(id)



Gets a single user by their user ID

### Example


```python
import pyaudius
from pyaudius.models.user_response import UserResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID

    try:
        api_response = api_instance.get_user(id)
        print("The response of UsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user_by_handle**
> UserResponse get_user_by_handle(handle, user_id=user_id)



Gets a single user by their handle

### Example


```python
import pyaudius
from pyaudius.models.user_response import UserResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    handle = 'handle_example' # str | A User handle
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)

    try:
        api_response = api_instance.get_user_by_handle(handle, user_id=user_id)
        print("The response of UsersApi->get_user_by_handle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_by_handle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**| A User handle | 
 **user_id** | **str**| The user ID of the user making the request | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user_challenges**
> GetChallenges get_user_challenges(id, show_historical=show_historical)



Gets all challenges for the given user

### Example


```python
import pyaudius
from pyaudius.models.get_challenges import GetChallenges
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    show_historical = False # bool | Whether to show challenges that are inactive but completed (optional) (default to False)

    try:
        api_response = api_instance.get_user_challenges(id, show_historical=show_historical)
        print("The response of UsersApi->get_user_challenges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_challenges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **show_historical** | **bool**| Whether to show challenges that are inactive but completed | [optional] [default to False]

### Return type

[**GetChallenges**](GetChallenges.md)

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

# **get_user_id_from_wallet**
> UserAssociatedWalletResponse get_user_id_from_wallet(associated_wallet)



Gets a User ID from an associated wallet address

### Example


```python
import pyaudius
from pyaudius.models.user_associated_wallet_response import UserAssociatedWalletResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    associated_wallet = 'associated_wallet_example' # str | Wallet address

    try:
        api_response = api_instance.get_user_id_from_wallet(associated_wallet)
        print("The response of UsersApi->get_user_id_from_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_id_from_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **associated_wallet** | **str**| Wallet address | 

### Return type

[**UserAssociatedWalletResponse**](UserAssociatedWalletResponse.md)

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

# **get_user_tracks_remixed**
> UserTracksRemixedResponse get_user_tracks_remixed(id, offset=offset, limit=limit, user_id=user_id)



Gets tracks owned by the user which have been remixed by another track

### Example


```python
import pyaudius
from pyaudius.models.user_tracks_remixed_response import UserTracksRemixedResponse
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
    api_instance = pyaudius.UsersApi(api_client)
    id = 'id_example' # str | A User ID
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)

    try:
        api_response = api_instance.get_user_tracks_remixed(id, offset=offset, limit=limit, user_id=user_id)
        print("The response of UsersApi->get_user_tracks_remixed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_tracks_remixed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A User ID | 
 **offset** | **int**| The number of items to skip. Useful for pagination (page number * limit) | [optional] 
 **limit** | **int**| The number of items to fetch | [optional] 
 **user_id** | **str**| The user ID of the user making the request | [optional] 

### Return type

[**UserTracksRemixedResponse**](UserTracksRemixedResponse.md)

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

# **search_users**
> UserSearch search_users(query=query, genre=genre, sort_method=sort_method, is_verified=is_verified)



Search for users that match the given query

### Example


```python
import pyaudius
from pyaudius.models.user_search import UserSearch
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
    api_instance = pyaudius.UsersApi(api_client)
    query = 'query_example' # str | The search query (optional)
    genre = ['genre_example'] # List[str] | The genres to filter by (optional)
    sort_method = 'sort_method_example' # str | The sort method (optional)
    is_verified = 'is_verified_example' # str | Only include verified users in the user results (optional)

    try:
        api_response = api_instance.search_users(query=query, genre=genre, sort_method=sort_method, is_verified=is_verified)
        print("The response of UsersApi->search_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->search_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query | [optional] 
 **genre** | [**List[str]**](str.md)| The genres to filter by | [optional] 
 **sort_method** | **str**| The sort method | [optional] 
 **is_verified** | **str**| Only include verified users in the user results | [optional] 

### Return type

[**UserSearch**](UserSearch.md)

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

# **verify_id_token**
> VerifyToken verify_id_token(token)



Verify if the given jwt ID token was signed by the subject (user) in the payload

### Example


```python
import pyaudius
from pyaudius.models.verify_token import VerifyToken
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
    api_instance = pyaudius.UsersApi(api_client)
    token = 'token_example' # str | JWT to verify

    try:
        api_response = api_instance.verify_id_token(token)
        print("The response of UsersApi->verify_id_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->verify_id_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| JWT to verify | 

### Return type

[**VerifyToken**](VerifyToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad input |  -  |
**404** | ID token not valid |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

