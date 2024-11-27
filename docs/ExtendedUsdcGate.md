# ExtendedUsdcGate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **int** |  | 
**splits** | [**List[ExtendedPaymentSplit]**](ExtendedPaymentSplit.md) |  | 

## Example

```python
from pyaudius.models.extended_usdc_gate import ExtendedUsdcGate

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedUsdcGate from a JSON string
extended_usdc_gate_instance = ExtendedUsdcGate.from_json(json)
# print the JSON string representation of the object
print(ExtendedUsdcGate.to_json())

# convert the object into a dict
extended_usdc_gate_dict = extended_usdc_gate_instance.to_dict()
# create an instance of ExtendedUsdcGate from a dict
extended_usdc_gate_from_dict = ExtendedUsdcGate.from_dict(extended_usdc_gate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


