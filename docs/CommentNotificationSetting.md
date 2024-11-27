# CommentNotificationSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_muted** | **bool** |  | 

## Example

```python
from pyaudius.models.comment_notification_setting import CommentNotificationSetting

# TODO update the JSON string below
json = "{}"
# create an instance of CommentNotificationSetting from a JSON string
comment_notification_setting_instance = CommentNotificationSetting.from_json(json)
# print the JSON string representation of the object
print(CommentNotificationSetting.to_json())

# convert the object into a dict
comment_notification_setting_dict = comment_notification_setting_instance.to_dict()
# create an instance of CommentNotificationSetting from a dict
comment_notification_setting_from_dict = CommentNotificationSetting.from_dict(comment_notification_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


