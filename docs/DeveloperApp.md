# DeveloperApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 

## Example

```python
from pyaudius.models.developer_app import DeveloperApp

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperApp from a JSON string
developer_app_instance = DeveloperApp.from_json(json)
# print the JSON string representation of the object
print(DeveloperApp.to_json())

# convert the object into a dict
developer_app_dict = developer_app_instance.to_dict()
# create an instance of DeveloperApp from a dict
developer_app_from_dict = DeveloperApp.from_dict(developer_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


