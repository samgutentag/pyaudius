# FollowersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from pyaudius.models.followers_response import FollowersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FollowersResponse from a JSON string
followers_response_instance = FollowersResponse.from_json(json)
# print the JSON string representation of the object
print(FollowersResponse.to_json())

# convert the object into a dict
followers_response_dict = followers_response_instance.to_dict()
# create an instance of FollowersResponse from a dict
followers_response_from_dict = FollowersResponse.from_dict(followers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


