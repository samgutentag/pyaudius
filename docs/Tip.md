# Tip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | 
**sender** | [**User**](User.md) |  | [optional] 
**receiver** | [**User**](User.md) |  | [optional] 
**created_at** | **str** |  | 

## Example

```python
from pyaudius.models.tip import Tip

# TODO update the JSON string below
json = "{}"
# create an instance of Tip from a JSON string
tip_instance = Tip.from_json(json)
# print the JSON string representation of the object
print(Tip.to_json())

# convert the object into a dict
tip_dict = tip_instance.to_dict()
# create an instance of Tip from a dict
tip_from_dict = Tip.from_dict(tip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


