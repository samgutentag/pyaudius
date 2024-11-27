# TagsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** |  | [optional] 

## Example

```python
from pyaudius.models.tags_response import TagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TagsResponse from a JSON string
tags_response_instance = TagsResponse.from_json(json)
# print the JSON string representation of the object
print(TagsResponse.to_json())

# convert the object into a dict
tags_response_dict = tags_response_instance.to_dict()
# create an instance of TagsResponse from a dict
tags_response_from_dict = TagsResponse.from_dict(tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

