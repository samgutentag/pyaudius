# TrackInspect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BlobInfo**](BlobInfo.md) |  | [optional] 

## Example

```python
from pyaudius.models.track_inspect import TrackInspect

# TODO update the JSON string below
json = "{}"
# create an instance of TrackInspect from a JSON string
track_inspect_instance = TrackInspect.from_json(json)
# print the JSON string representation of the object
print(TrackInspect.to_json())

# convert the object into a dict
track_inspect_dict = track_inspect_instance.to_dict()
# create an instance of TrackInspect from a dict
track_inspect_from_dict = TrackInspect.from_dict(track_inspect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


