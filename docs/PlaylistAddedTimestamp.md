# PlaylistAddedTimestamp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_timestamp** | **int** |  | 
**timestamp** | **int** |  | 
**track_id** | **str** |  | 

## Example

```python
from pyaudius.models.playlist_added_timestamp import PlaylistAddedTimestamp

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistAddedTimestamp from a JSON string
playlist_added_timestamp_instance = PlaylistAddedTimestamp.from_json(json)
# print the JSON string representation of the object
print(PlaylistAddedTimestamp.to_json())

# convert the object into a dict
playlist_added_timestamp_dict = playlist_added_timestamp_instance.to_dict()
# create an instance of PlaylistAddedTimestamp from a dict
playlist_added_timestamp_from_dict = PlaylistAddedTimestamp.from_dict(playlist_added_timestamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


