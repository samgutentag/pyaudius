# ConnectedWallets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**erc_wallets** | **List[str]** |  | 
**spl_wallets** | **List[str]** |  | 

## Example

```python
from pyaudius.models.connected_wallets import ConnectedWallets

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedWallets from a JSON string
connected_wallets_instance = ConnectedWallets.from_json(json)
# print the JSON string representation of the object
print(ConnectedWallets.to_json())

# convert the object into a dict
connected_wallets_dict = connected_wallets_instance.to_dict()
# create an instance of ConnectedWallets from a dict
connected_wallets_from_dict = ConnectedWallets.from_dict(connected_wallets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


