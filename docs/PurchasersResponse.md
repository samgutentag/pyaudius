# PurchasersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from pyaudius.models.purchasers_response import PurchasersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasersResponse from a JSON string
purchasers_response_instance = PurchasersResponse.from_json(json)
# print the JSON string representation of the object
print(PurchasersResponse.to_json())

# convert the object into a dict
purchasers_response_dict = purchasers_response_instance.to_dict()
# create an instance of PurchasersResponse from a dict
purchasers_response_from_dict = PurchasersResponse.from_dict(purchasers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


