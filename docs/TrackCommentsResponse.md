# TrackCommentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Comment]**](Comment.md) |  | [optional] 

## Example

```python
from pyaudius.models.track_comments_response import TrackCommentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrackCommentsResponse from a JSON string
track_comments_response_instance = TrackCommentsResponse.from_json(json)
# print the JSON string representation of the object
print(TrackCommentsResponse.to_json())

# convert the object into a dict
track_comments_response_dict = track_comments_response_instance.to_dict()
# create an instance of TrackCommentsResponse from a dict
track_comments_response_from_dict = TrackCommentsResponse.from_dict(track_comments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


