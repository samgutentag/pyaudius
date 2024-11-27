# FollowGate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**follow_user_id** | **int** | Must follow the given user ID to unlock | 

## Example

```python
from pyaudius.models.follow_gate import FollowGate

# TODO update the JSON string below
json = "{}"
# create an instance of FollowGate from a JSON string
follow_gate_instance = FollowGate.from_json(json)
# print the JSON string representation of the object
print(FollowGate.to_json())

# convert the object into a dict
follow_gate_dict = follow_gate_instance.to_dict()
# create an instance of FollowGate from a dict
follow_gate_from_dict = FollowGate.from_dict(follow_gate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


