# ReplyComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**message** | **str** |  | 
**mentions** | [**List[CommentMention]**](CommentMention.md) |  | [optional] 
**track_timestamp_s** | **int** |  | [optional] 
**react_count** | **int** |  | 
**is_edited** | **bool** |  | 
**is_current_user_reacted** | **bool** |  | [optional] 
**is_artist_reacted** | **bool** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | [optional] 

## Example

```python
from pyaudius.models.reply_comment import ReplyComment

# TODO update the JSON string below
json = "{}"
# create an instance of ReplyComment from a JSON string
reply_comment_instance = ReplyComment.from_json(json)
# print the JSON string representation of the object
print(ReplyComment.to_json())

# convert the object into a dict
reply_comment_dict = reply_comment_instance.to_dict()
# create an instance of ReplyComment from a dict
reply_comment_from_dict = ReplyComment.from_dict(reply_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


