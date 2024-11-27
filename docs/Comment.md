# Comment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**message** | **str** |  | 
**mentions** | [**List[CommentMention]**](CommentMention.md) |  | [optional] 
**track_timestamp_s** | **int** |  | [optional] 
**react_count** | **int** |  | 
**reply_count** | **int** |  | 
**is_edited** | **bool** |  | 
**is_current_user_reacted** | **bool** |  | [optional] 
**is_artist_reacted** | **bool** |  | [optional] 
**is_tombstone** | **bool** |  | [optional] 
**is_muted** | **bool** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | [optional] 
**replies** | [**List[ReplyComment]**](ReplyComment.md) |  | [optional] 

## Example

```python
from pyaudius.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print(Comment.to_json())

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_from_dict = Comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


