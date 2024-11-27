# UndisbursedChallenge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_id** | **str** |  | 
**user_id** | **str** |  | 
**specifier** | **str** |  | 
**amount** | **str** |  | 
**completed_blocknumber** | **int** |  | 
**handle** | **str** |  | 
**wallet** | **str** |  | 
**created_at** | **str** |  | 
**completed_at** | **str** |  | 
**cooldown_days** | **int** |  | [optional] 

## Example

```python
from pyaudius.models.undisbursed_challenge import UndisbursedChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of UndisbursedChallenge from a JSON string
undisbursed_challenge_instance = UndisbursedChallenge.from_json(json)
# print the JSON string representation of the object
print(UndisbursedChallenge.to_json())

# convert the object into a dict
undisbursed_challenge_dict = undisbursed_challenge_instance.to_dict()
# create an instance of UndisbursedChallenge from a dict
undisbursed_challenge_from_dict = UndisbursedChallenge.from_dict(undisbursed_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


