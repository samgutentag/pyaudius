# TipGate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tip_user_id** | **int** | Must tip the given user ID to unlock | 

## Example

```python
from pyaudius.models.tip_gate import TipGate

# TODO update the JSON string below
json = "{}"
# create an instance of TipGate from a JSON string
tip_gate_instance = TipGate.from_json(json)
# print the JSON string representation of the object
print(TipGate.to_json())

# convert the object into a dict
tip_gate_dict = tip_gate_instance.to_dict()
# create an instance of TipGate from a dict
tip_gate_from_dict = TipGate.from_dict(tip_gate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


