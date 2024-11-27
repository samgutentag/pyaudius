# AuthorizedApps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuthorizedApp]**](AuthorizedApp.md) |  | [optional] 

## Example

```python
from pyaudius.models.authorized_apps import AuthorizedApps

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizedApps from a JSON string
authorized_apps_instance = AuthorizedApps.from_json(json)
# print the JSON string representation of the object
print(AuthorizedApps.to_json())

# convert the object into a dict
authorized_apps_dict = authorized_apps_instance.to_dict()
# create an instance of AuthorizedApps from a dict
authorized_apps_from_dict = AuthorizedApps.from_dict(authorized_apps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


