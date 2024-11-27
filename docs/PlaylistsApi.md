# pyaudius.PlaylistsApi

All URIs are relative to *https://discoveryprovider.audius.co/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bulk_playlists**](PlaylistsApi.md#get_bulk_playlists) | **GET** /playlists | 
[**get_playlist**](PlaylistsApi.md#get_playlist) | **GET** /playlists/{playlist_id} | 
[**get_playlist_access_info**](PlaylistsApi.md#get_playlist_access_info) | **GET** /playlists/{playlist_id}/access-info | 
[**get_playlist_by_handle_and_slug**](PlaylistsApi.md#get_playlist_by_handle_and_slug) | **GET** /playlists/by_permalink/{handle}/{slug} | 
[**get_playlist_tracks**](PlaylistsApi.md#get_playlist_tracks) | **GET** /playlists/{playlist_id}/tracks | 
[**get_trending_playlists**](PlaylistsApi.md#get_trending_playlists) | **GET** /playlists/trending | 
[**search_playlists**](PlaylistsApi.md#search_playlists) | **GET** /playlists/search | 


# **get_bulk_playlists**
> PlaylistResponse get_bulk_playlists(user_id=user_id, id=id)



Gets a list of playlists by ID

### Example


```python
import pyaudius
from pyaudius.models.playlist_response import PlaylistResponse
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
    api_instance = pyaudius.PlaylistsApi(api_client)
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)
    id = ['id_example'] # List[str] | The ID of the playlist(s) (optional)

    try:
        api_response = api_instance.get_bulk_playlists(user_id=user_id, id=id)
        print("The response of PlaylistsApi->get_bulk_playlists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_bulk_playlists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID of the user making the request | [optional] 
 **id** | [**List[str]**](str.md)| The ID of the playlist(s) | [optional] 

### Return type

[**PlaylistResponse**](PlaylistResponse.md)

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

# **get_playlist**
> PlaylistResponse get_playlist(playlist_id, user_id=user_id)



Get a playlist by ID

### Example


```python
import pyaudius
from pyaudius.models.playlist_response import PlaylistResponse
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
    api_instance = pyaudius.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | A Playlist ID
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)

    try:
        api_response = api_instance.get_playlist(playlist_id, user_id=user_id)
        print("The response of PlaylistsApi->get_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| A Playlist ID | 
 **user_id** | **str**| The user ID of the user making the request | [optional] 

### Return type

[**PlaylistResponse**](PlaylistResponse.md)

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

# **get_playlist_access_info**
> AccessInfoResponse get_playlist_access_info(playlist_id, user_id=user_id)



Gets the information necessary to access the playlist and what access the given user has.

### Example


```python
import pyaudius
from pyaudius.models.access_info_response import AccessInfoResponse
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
    api_instance = pyaudius.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | A Playlist ID
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)

    try:
        api_response = api_instance.get_playlist_access_info(playlist_id, user_id=user_id)
        print("The response of PlaylistsApi->get_playlist_access_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_playlist_access_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| A Playlist ID | 
 **user_id** | **str**| The user ID of the user making the request | [optional] 

### Return type

[**AccessInfoResponse**](AccessInfoResponse.md)

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

# **get_playlist_by_handle_and_slug**
> PlaylistResponse get_playlist_by_handle_and_slug(handle, slug, user_id=user_id)



Get a playlist by handle and slug

### Example


```python
import pyaudius
from pyaudius.models.playlist_response import PlaylistResponse
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
    api_instance = pyaudius.PlaylistsApi(api_client)
    handle = 'handle_example' # str | playlist owner handle
    slug = 'slug_example' # str | playlist slug
    user_id = 'user_id_example' # str | The user ID of the user making the request (optional)

    try:
        api_response = api_instance.get_playlist_by_handle_and_slug(handle, slug, user_id=user_id)
        print("The response of PlaylistsApi->get_playlist_by_handle_and_slug:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_playlist_by_handle_and_slug: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**| playlist owner handle | 
 **slug** | **str**| playlist slug | 
 **user_id** | **str**| The user ID of the user making the request | [optional] 

### Return type

[**PlaylistResponse**](PlaylistResponse.md)

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

# **get_playlist_tracks**
> PlaylistTracksResponse get_playlist_tracks(playlist_id)



Fetch tracks within a playlist.

### Example


```python
import pyaudius
from pyaudius.models.playlist_tracks_response import PlaylistTracksResponse
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
    api_instance = pyaudius.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | A Playlist ID

    try:
        api_response = api_instance.get_playlist_tracks(playlist_id)
        print("The response of PlaylistsApi->get_playlist_tracks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_playlist_tracks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| A Playlist ID | 

### Return type

[**PlaylistTracksResponse**](PlaylistTracksResponse.md)

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

# **get_trending_playlists**
> TrendingPlaylistsResponse get_trending_playlists(time=time)



Gets trending playlists for a time period

### Example


```python
import pyaudius
from pyaudius.models.trending_playlists_response import TrendingPlaylistsResponse
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
    api_instance = pyaudius.PlaylistsApi(api_client)
    time = 'time_example' # str | Calculate trending over a specified time range (optional)

    try:
        api_response = api_instance.get_trending_playlists(time=time)
        print("The response of PlaylistsApi->get_trending_playlists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_trending_playlists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time** | **str**| Calculate trending over a specified time range | [optional] 

### Return type

[**TrendingPlaylistsResponse**](TrendingPlaylistsResponse.md)

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

# **search_playlists**
> PlaylistSearchResult search_playlists(query=query, genre=genre, sort_method=sort_method, mood=mood, include_purchaseable=include_purchaseable, has_downloads=has_downloads)



Search for a playlist

### Example


```python
import pyaudius
from pyaudius.models.playlist_search_result import PlaylistSearchResult
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
    api_instance = pyaudius.PlaylistsApi(api_client)
    query = 'query_example' # str | The search query (optional)
    genre = ['genre_example'] # List[str] | The genres to filter by (optional)
    sort_method = 'sort_method_example' # str | The sort method (optional)
    mood = ['mood_example'] # List[str] | The moods to filter by (optional)
    include_purchaseable = 'include_purchaseable_example' # str | Whether or not to include purchaseable content (optional)
    has_downloads = 'has_downloads_example' # str | Only include tracks that have downloads in the track results (optional)

    try:
        api_response = api_instance.search_playlists(query=query, genre=genre, sort_method=sort_method, mood=mood, include_purchaseable=include_purchaseable, has_downloads=has_downloads)
        print("The response of PlaylistsApi->search_playlists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->search_playlists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query | [optional] 
 **genre** | [**List[str]**](str.md)| The genres to filter by | [optional] 
 **sort_method** | **str**| The sort method | [optional] 
 **mood** | [**List[str]**](str.md)| The moods to filter by | [optional] 
 **include_purchaseable** | **str**| Whether or not to include purchaseable content | [optional] 
 **has_downloads** | **str**| Only include tracks that have downloads in the track results | [optional] 

### Return type

[**PlaylistSearchResult**](PlaylistSearchResult.md)

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

