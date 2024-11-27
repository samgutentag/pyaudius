# DashboardWalletUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DashboardWalletUser]**](DashboardWalletUser.md) |  | [optional] 

## Example

```python
from pyaudius.models.dashboard_wallet_users_response import DashboardWalletUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardWalletUsersResponse from a JSON string
dashboard_wallet_users_response_instance = DashboardWalletUsersResponse.from_json(json)
# print the JSON string representation of the object
print(DashboardWalletUsersResponse.to_json())

# convert the object into a dict
dashboard_wallet_users_response_dict = dashboard_wallet_users_response_instance.to_dict()
# create an instance of DashboardWalletUsersResponse from a dict
dashboard_wallet_users_response_from_dict = DashboardWalletUsersResponse.from_dict(dashboard_wallet_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


