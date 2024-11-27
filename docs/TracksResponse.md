# TracksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Track]**](Track.md) |  | [optional] 

## Example

```python
from pyaudius.models.tracks_response import TracksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TracksResponse from a JSON string
tracks_response_instance = TracksResponse.from_json(json)
# print the JSON string representation of the object
print(TracksResponse.to_json())

# convert the object into a dict
tracks_response_dict = tracks_response_instance.to_dict()
# create an instance of TracksResponse from a dict
tracks_response_from_dict = TracksResponse.from_dict(tracks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


