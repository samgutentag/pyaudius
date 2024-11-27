# TrackArtwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_150x150** | **str** |  | [optional] 
**var_480x480** | **str** |  | [optional] 
**var_1000x1000** | **str** |  | [optional] 

## Example

```python
from pyaudius.models.track_artwork import TrackArtwork

# TODO update the JSON string below
json = "{}"
# create an instance of TrackArtwork from a JSON string
track_artwork_instance = TrackArtwork.from_json(json)
# print the JSON string representation of the object
print(TrackArtwork.to_json())

# convert the object into a dict
track_artwork_dict = track_artwork_instance.to_dict()
# create an instance of TrackArtwork from a dict
track_artwork_from_dict = TrackArtwork.from_dict(track_artwork_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


