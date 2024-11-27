# TrackCommentNotificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommentNotificationSetting**](CommentNotificationSetting.md) |  | [optional] 

## Example

```python
from pyaudius.models.track_comment_notification_response import TrackCommentNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrackCommentNotificationResponse from a JSON string
track_comment_notification_response_instance = TrackCommentNotificationResponse.from_json(json)
# print the JSON string representation of the object
print(TrackCommentNotificationResponse.to_json())

# convert the object into a dict
track_comment_notification_response_dict = track_comment_notification_response_instance.to_dict()
# create an instance of TrackCommentNotificationResponse from a dict
track_comment_notification_response_from_dict = TrackCommentNotificationResponse.from_dict(track_comment_notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


