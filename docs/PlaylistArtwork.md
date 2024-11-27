# PlaylistArtwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_150x150** | **str** |  | [optional] 
**var_480x480** | **str** |  | [optional] 
**var_1000x1000** | **str** |  | [optional] 

## Example

```python
from pyaudius.models.playlist_artwork import PlaylistArtwork

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistArtwork from a JSON string
playlist_artwork_instance = PlaylistArtwork.from_json(json)
# print the JSON string representation of the object
print(PlaylistArtwork.to_json())

# convert the object into a dict
playlist_artwork_dict = playlist_artwork_instance.to_dict()
# create an instance of PlaylistArtwork from a dict
playlist_artwork_from_dict = PlaylistArtwork.from_dict(playlist_artwork_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


