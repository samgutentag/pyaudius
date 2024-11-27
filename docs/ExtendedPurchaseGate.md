# ExtendedPurchaseGate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usdc_purchase** | [**ExtendedUsdcGate**](ExtendedUsdcGate.md) | Must pay the total price and split to the given addresses to unlock | 

## Example

```python
from pyaudius.models.extended_purchase_gate import ExtendedPurchaseGate

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedPurchaseGate from a JSON string
extended_purchase_gate_instance = ExtendedPurchaseGate.from_json(json)
# print the JSON string representation of the object
print(ExtendedPurchaseGate.to_json())

# convert the object into a dict
extended_purchase_gate_dict = extended_purchase_gate_instance.to_dict()
# create an instance of ExtendedPurchaseGate from a dict
extended_purchase_gate_from_dict = ExtendedPurchaseGate.from_dict(extended_purchase_gate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


