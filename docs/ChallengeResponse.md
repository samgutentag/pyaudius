# ChallengeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_id** | **str** |  | 
**user_id** | **str** |  | 
**specifier** | **str** |  | [optional] 
**is_complete** | **bool** |  | 
**is_active** | **bool** |  | 
**is_disbursed** | **bool** |  | 
**current_step_count** | **int** |  | [optional] 
**max_steps** | **int** |  | [optional] 
**challenge_type** | **str** |  | 
**amount** | **str** |  | 
**disbursed_amount** | **int** |  | 
**cooldown_days** | **int** |  | [optional] 
**metadata** | **object** |  | 

## Example

```python
from pyaudius.models.challenge_response import ChallengeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChallengeResponse from a JSON string
challenge_response_instance = ChallengeResponse.from_json(json)
# print the JSON string representation of the object
print(ChallengeResponse.to_json())

# convert the object into a dict
challenge_response_dict = challenge_response_instance.to_dict()
# create an instance of ChallengeResponse from a dict
challenge_response_from_dict = ChallengeResponse.from_dict(challenge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


