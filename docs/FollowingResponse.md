# FollowingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from pyaudius.models.following_response import FollowingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FollowingResponse from a JSON string
following_response_instance = FollowingResponse.from_json(json)
# print the JSON string representation of the object
print(FollowingResponse.to_json())

# convert the object into a dict
following_response_dict = following_response_instance.to_dict()
# create an instance of FollowingResponse from a dict
following_response_from_dict = FollowingResponse.from_dict(following_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


