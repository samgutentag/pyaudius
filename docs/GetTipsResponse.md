# GetTipsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Tip]**](Tip.md) |  | [optional] 

## Example

```python
from pyaudius.models.get_tips_response import GetTipsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTipsResponse from a JSON string
get_tips_response_instance = GetTipsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTipsResponse.to_json())

# convert the object into a dict
get_tips_response_dict = get_tips_response_instance.to_dict()
# create an instance of GetTipsResponse from a dict
get_tips_response_from_dict = GetTipsResponse.from_dict(get_tips_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


