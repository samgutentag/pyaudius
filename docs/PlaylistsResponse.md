# PlaylistsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Playlist]**](Playlist.md) |  | [optional] 

## Example

```python
from pyaudius.models.playlists_response import PlaylistsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsResponse from a JSON string
playlists_response_instance = PlaylistsResponse.from_json(json)
# print the JSON string representation of the object
print(PlaylistsResponse.to_json())

# convert the object into a dict
playlists_response_dict = playlists_response_instance.to_dict()
# create an instance of PlaylistsResponse from a dict
playlists_response_from_dict = PlaylistsResponse.from_dict(playlists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


