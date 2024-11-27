# GetChallenges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ChallengeResponse]**](ChallengeResponse.md) |  | [optional] 

## Example

```python
from pyaudius.models.get_challenges import GetChallenges

# TODO update the JSON string below
json = "{}"
# create an instance of GetChallenges from a JSON string
get_challenges_instance = GetChallenges.from_json(json)
# print the JSON string representation of the object
print(GetChallenges.to_json())

# convert the object into a dict
get_challenges_dict = get_challenges_instance.to_dict()
# create an instance of GetChallenges from a dict
get_challenges_from_dict = GetChallenges.from_dict(get_challenges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


