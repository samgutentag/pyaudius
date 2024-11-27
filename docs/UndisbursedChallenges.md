# UndisbursedChallenges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UndisbursedChallenge]**](UndisbursedChallenge.md) |  | [optional] 

## Example

```python
from pyaudius.models.undisbursed_challenges import UndisbursedChallenges

# TODO update the JSON string below
json = "{}"
# create an instance of UndisbursedChallenges from a JSON string
undisbursed_challenges_instance = UndisbursedChallenges.from_json(json)
# print the JSON string representation of the object
print(UndisbursedChallenges.to_json())

# convert the object into a dict
undisbursed_challenges_dict = undisbursed_challenges_instance.to_dict()
# create an instance of UndisbursedChallenges from a dict
undisbursed_challenges_from_dict = UndisbursedChallenges.from_dict(undisbursed_challenges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


