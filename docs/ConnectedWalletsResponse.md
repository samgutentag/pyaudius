# ConnectedWalletsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ConnectedWallets**](ConnectedWallets.md) |  | [optional] 

## Example

```python
from pyaudius.models.connected_wallets_response import ConnectedWalletsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedWalletsResponse from a JSON string
connected_wallets_response_instance = ConnectedWalletsResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectedWalletsResponse.to_json())

# convert the object into a dict
connected_wallets_response_dict = connected_wallets_response_instance.to_dict()
# create an instance of ConnectedWalletsResponse from a dict
connected_wallets_response_from_dict = ConnectedWalletsResponse.from_dict(connected_wallets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


