# DeveloperAppResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeveloperApp**](DeveloperApp.md) |  | [optional] 

## Example

```python
from pyaudius.models.developer_app_response import DeveloperAppResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperAppResponse from a JSON string
developer_app_response_instance = DeveloperAppResponse.from_json(json)
# print the JSON string representation of the object
print(DeveloperAppResponse.to_json())

# convert the object into a dict
developer_app_response_dict = developer_app_response_instance.to_dict()
# create an instance of DeveloperAppResponse from a dict
developer_app_response_from_dict = DeveloperAppResponse.from_dict(developer_app_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


