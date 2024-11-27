# DashboardWalletUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet** | **str** |  | 
**user** | [**User**](User.md) |  | 

## Example

```python
from pyaudius.models.dashboard_wallet_user import DashboardWalletUser

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardWalletUser from a JSON string
dashboard_wallet_user_instance = DashboardWalletUser.from_json(json)
# print the JSON string representation of the object
print(DashboardWalletUser.to_json())

# convert the object into a dict
dashboard_wallet_user_dict = dashboard_wallet_user_instance.to_dict()
# create an instance of DashboardWalletUser from a dict
dashboard_wallet_user_from_dict = DashboardWalletUser.from_dict(dashboard_wallet_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


