# UserTracksRemixedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RemixedTrackAggregate]**](RemixedTrackAggregate.md) |  | [optional] 

## Example

```python
from pyaudius.models.user_tracks_remixed_response import UserTracksRemixedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserTracksRemixedResponse from a JSON string
user_tracks_remixed_response_instance = UserTracksRemixedResponse.from_json(json)
# print the JSON string representation of the object
print(UserTracksRemixedResponse.to_json())

# convert the object into a dict
user_tracks_remixed_response_dict = user_tracks_remixed_response_instance.to_dict()
# create an instance of UserTracksRemixedResponse from a dict
user_tracks_remixed_response_from_dict = UserTracksRemixedResponse.from_dict(user_tracks_remixed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


