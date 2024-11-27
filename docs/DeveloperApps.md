# DeveloperApps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DeveloperApp]**](DeveloperApp.md) |  | [optional] 

## Example

```python
from pyaudius.models.developer_apps import DeveloperApps

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperApps from a JSON string
developer_apps_instance = DeveloperApps.from_json(json)
# print the JSON string representation of the object
print(DeveloperApps.to_json())

# convert the object into a dict
developer_apps_dict = developer_apps_instance.to_dict()
# create an instance of DeveloperApps from a dict
developer_apps_from_dict = DeveloperApps.from_dict(developer_apps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


