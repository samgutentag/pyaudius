# UserAssociatedWalletResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EncodedUserId**](EncodedUserId.md) |  | [optional] 

## Example

```python
from pyaudius.models.user_associated_wallet_response import UserAssociatedWalletResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserAssociatedWalletResponse from a JSON string
user_associated_wallet_response_instance = UserAssociatedWalletResponse.from_json(json)
# print the JSON string representation of the object
print(UserAssociatedWalletResponse.to_json())

# convert the object into a dict
user_associated_wallet_response_dict = user_associated_wallet_response_instance.to_dict()
# create an instance of UserAssociatedWalletResponse from a dict
user_associated_wallet_response_from_dict = UserAssociatedWalletResponse.from_dict(user_associated_wallet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


