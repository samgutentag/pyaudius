# TrackAccessInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**Access**](Access.md) | Describes what access the given user has | [optional] 
**user_id** | **str** | The user ID of the owner of this track | 
**blocknumber** | **int** | The blocknumber this track was last updated | 
**is_stream_gated** | **bool** | Whether or not the owner has restricted streaming behind an access gate | [optional] 
**stream_conditions** | **object** | How to unlock stream access to the track | [optional] 
**is_download_gated** | **bool** | Whether or not the owner has restricted downloading behind an access gate | [optional] 
**download_conditions** | **object** | How to unlock the track download | [optional] 

## Example

```python
from pyaudius.models.track_access_info import TrackAccessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TrackAccessInfo from a JSON string
track_access_info_instance = TrackAccessInfo.from_json(json)
# print the JSON string representation of the object
print(TrackAccessInfo.to_json())

# convert the object into a dict
track_access_info_dict = track_access_info_instance.to_dict()
# create an instance of TrackAccessInfo from a dict
track_access_info_from_dict = TrackAccessInfo.from_dict(track_access_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


