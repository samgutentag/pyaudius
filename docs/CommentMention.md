# CommentMention


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**handle** | **str** |  | 

## Example

```python
from pyaudius.models.comment_mention import CommentMention

# TODO update the JSON string below
json = "{}"
# create an instance of CommentMention from a JSON string
comment_mention_instance = CommentMention.from_json(json)
# print the JSON string representation of the object
print(CommentMention.to_json())

# convert the object into a dict
comment_mention_dict = comment_mention_instance.to_dict()
# create an instance of CommentMention from a dict
comment_mention_from_dict = CommentMention.from_dict(comment_mention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


