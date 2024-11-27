# GetSupportedUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Supporting]**](Supporting.md) |  | [optional] 

## Example

```python
from pyaudius.models.get_supported_users import GetSupportedUsers

# TODO update the JSON string below
json = "{}"
# create an instance of GetSupportedUsers from a JSON string
get_supported_users_instance = GetSupportedUsers.from_json(json)
# print the JSON string representation of the object
print(GetSupportedUsers.to_json())

# convert the object into a dict
get_supported_users_dict = get_supported_users_instance.to_dict()
# create an instance of GetSupportedUsers from a dict
get_supported_users_from_dict = GetSupportedUsers.from_dict(get_supported_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


