# PlaylistTracksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Track]**](Track.md) |  | [optional] 

## Example

```python
from pyaudius.models.playlist_tracks_response import PlaylistTracksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistTracksResponse from a JSON string
playlist_tracks_response_instance = PlaylistTracksResponse.from_json(json)
# print the JSON string representation of the object
print(PlaylistTracksResponse.to_json())

# convert the object into a dict
playlist_tracks_response_dict = playlist_tracks_response_instance.to_dict()
# create an instance of PlaylistTracksResponse from a dict
playlist_tracks_response_from_dict = PlaylistTracksResponse.from_dict(playlist_tracks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


