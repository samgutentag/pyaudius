# DecodedUserToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | 
**handle** | **str** |  | 
**verified** | **bool** |  | 
**profile_picture** | [**ProfilePicture**](ProfilePicture.md) |  | [optional] 
**sub** | **str** |  | 
**iat** | **str** |  | 

## Example

```python
from pyaudius.models.decoded_user_token import DecodedUserToken

# TODO update the JSON string below
json = "{}"
# create an instance of DecodedUserToken from a JSON string
decoded_user_token_instance = DecodedUserToken.from_json(json)
# print the JSON string representation of the object
print(DecodedUserToken.to_json())

# convert the object into a dict
decoded_user_token_dict = decoded_user_token_instance.to_dict()
# create an instance of DecodedUserToken from a dict
decoded_user_token_from_dict = DecodedUserToken.from_dict(decoded_user_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


