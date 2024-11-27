# TrackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Track**](Track.md) |  | [optional] 

## Example

```python
from pyaudius.models.track_response import TrackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrackResponse from a JSON string
track_response_instance = TrackResponse.from_json(json)
# print the JSON string representation of the object
print(TrackResponse.to_json())

# convert the object into a dict
track_response_dict = track_response_instance.to_dict()
# create an instance of TrackResponse from a dict
track_response_from_dict = TrackResponse.from_dict(track_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


