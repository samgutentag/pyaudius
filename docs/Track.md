# Track


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artwork** | [**TrackArtwork**](TrackArtwork.md) |  | 
**description** | **str** |  | [optional] 
**genre** | **str** |  | 
**id** | **str** |  | 
**track_cid** | **str** |  | [optional] 
**preview_cid** | **str** |  | [optional] 
**orig_file_cid** | **str** |  | [optional] 
**orig_filename** | **str** |  | [optional] 
**is_original_available** | **bool** |  | 
**mood** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**remix_of** | [**RemixParent**](RemixParent.md) |  | [optional] 
**repost_count** | **int** |  | 
**favorite_count** | **int** |  | 
**comment_count** | **int** |  | 
**tags** | **str** |  | [optional] 
**title** | **str** |  | 
**user** | [**User**](User.md) |  | 
**duration** | **int** |  | 
**is_downloadable** | **bool** |  | 
**play_count** | **int** |  | 
**permalink** | **str** |  | 
**is_streamable** | **bool** |  | [optional] 
**ddex_app** | **str** |  | [optional] 
**playlists_containing_track** | **List[int]** |  | [optional] 
**pinned_comment_id** | **int** |  | [optional] 

## Example

```python
from pyaudius.models.track import Track

# TODO update the JSON string below
json = "{}"
# create an instance of Track from a JSON string
track_instance = Track.from_json(json)
# print the JSON string representation of the object
print(Track.to_json())

# convert the object into a dict
track_dict = track_instance.to_dict()
# create an instance of Track from a dict
track_from_dict = Track.from_dict(track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


