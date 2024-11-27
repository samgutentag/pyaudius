# PlaylistSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Playlist]**](Playlist.md) |  | [optional] 

## Example

```python
from pyaudius.models.playlist_search_result import PlaylistSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistSearchResult from a JSON string
playlist_search_result_instance = PlaylistSearchResult.from_json(json)
# print the JSON string representation of the object
print(PlaylistSearchResult.to_json())

# convert the object into a dict
playlist_search_result_dict = playlist_search_result_instance.to_dict()
# create an instance of PlaylistSearchResult from a dict
playlist_search_result_from_dict = PlaylistSearchResult.from_dict(playlist_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


