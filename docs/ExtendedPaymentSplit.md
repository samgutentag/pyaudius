# ExtendedPaymentSplit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**percentage** | **float** |  | 
**eth_wallet** | **str** |  | [optional] 
**payout_wallet** | **str** |  | 
**amount** | **int** |  | 

## Example

```python
from pyaudius.models.extended_payment_split import ExtendedPaymentSplit

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedPaymentSplit from a JSON string
extended_payment_split_instance = ExtendedPaymentSplit.from_json(json)
# print the JSON string representation of the object
print(ExtendedPaymentSplit.to_json())

# convert the object into a dict
extended_payment_split_dict = extended_payment_split_instance.to_dict()
# create an instance of ExtendedPaymentSplit from a dict
extended_payment_split_from_dict = ExtendedPaymentSplit.from_dict(extended_payment_split_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


