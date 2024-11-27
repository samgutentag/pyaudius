# UserSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from pyaudius.models.user_search import UserSearch

# TODO update the JSON string below
json = "{}"
# create an instance of UserSearch from a JSON string
user_search_instance = UserSearch.from_json(json)
# print the JSON string representation of the object
print(UserSearch.to_json())

# convert the object into a dict
user_search_dict = user_search_instance.to_dict()
# create an instance of UserSearch from a dict
user_search_from_dict = UserSearch.from_dict(user_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


