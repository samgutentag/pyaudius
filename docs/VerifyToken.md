# VerifyToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DecodedUserToken**](DecodedUserToken.md) |  | [optional] 

## Example

```python
from pyaudius.models.verify_token import VerifyToken

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyToken from a JSON string
verify_token_instance = VerifyToken.from_json(json)
# print the JSON string representation of the object
print(VerifyToken.to_json())

# convert the object into a dict
verify_token_dict = verify_token_instance.to_dict()
# create an instance of VerifyToken from a dict
verify_token_from_dict = VerifyToken.from_dict(verify_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


