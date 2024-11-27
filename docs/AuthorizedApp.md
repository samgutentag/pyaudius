# AuthorizedApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**grantor_user_id** | **str** |  | 
**grant_created_at** | **str** |  | 
**grant_updated_at** | **str** |  | 

## Example

```python
from pyaudius.models.authorized_app import AuthorizedApp

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizedApp from a JSON string
authorized_app_instance = AuthorizedApp.from_json(json)
# print the JSON string representation of the object
print(AuthorizedApp.to_json())

# convert the object into a dict
authorized_app_dict = authorized_app_instance.to_dict()
# create an instance of AuthorizedApp from a dict
authorized_app_from_dict = AuthorizedApp.from_dict(authorized_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


