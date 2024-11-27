# PlaylistResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Playlist]**](Playlist.md) |  | [optional] 

## Example

```python
from pyaudius.models.playlist_response import PlaylistResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistResponse from a JSON string
playlist_response_instance = PlaylistResponse.from_json(json)
# print the JSON string representation of the object
print(PlaylistResponse.to_json())

# convert the object into a dict
playlist_response_dict = playlist_response_instance.to_dict()
# create an instance of PlaylistResponse from a dict
playlist_response_from_dict = PlaylistResponse.from_dict(playlist_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


