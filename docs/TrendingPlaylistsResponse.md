# TrendingPlaylistsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Playlist]**](Playlist.md) |  | [optional] 

## Example

```python
from pyaudius.models.trending_playlists_response import TrendingPlaylistsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingPlaylistsResponse from a JSON string
trending_playlists_response_instance = TrendingPlaylistsResponse.from_json(json)
# print the JSON string representation of the object
print(TrendingPlaylistsResponse.to_json())

# convert the object into a dict
trending_playlists_response_dict = trending_playlists_response_instance.to_dict()
# create an instance of TrendingPlaylistsResponse from a dict
trending_playlists_response_from_dict = TrendingPlaylistsResponse.from_dict(trending_playlists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


