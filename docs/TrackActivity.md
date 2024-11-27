# TrackActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | **str** |  | 
**item** | [**Track**](Track.md) |  | 

## Example

```python
from pyaudius.models.track_activity import TrackActivity

# TODO update the JSON string below
json = "{}"
# create an instance of TrackActivity from a JSON string
track_activity_instance = TrackActivity.from_json(json)
# print the JSON string representation of the object
print(TrackActivity.to_json())

# convert the object into a dict
track_activity_dict = track_activity_instance.to_dict()
# create an instance of TrackActivity from a dict
track_activity_from_dict = TrackActivity.from_dict(track_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


