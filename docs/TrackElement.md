# TrackElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_track_id** | **str** |  | 

## Example

```python
from pyaudius.models.track_element import TrackElement

# TODO update the JSON string below
json = "{}"
# create an instance of TrackElement from a JSON string
track_element_instance = TrackElement.from_json(json)
# print the JSON string representation of the object
print(TrackElement.to_json())

# convert the object into a dict
track_element_dict = track_element_instance.to_dict()
# create an instance of TrackElement from a dict
track_element_from_dict = TrackElement.from_dict(track_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


