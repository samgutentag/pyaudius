# SubscribersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from pyaudius.models.subscribers_response import SubscribersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribersResponse from a JSON string
subscribers_response_instance = SubscribersResponse.from_json(json)
# print the JSON string representation of the object
print(SubscribersResponse.to_json())

# convert the object into a dict
subscribers_response_dict = subscribers_response_instance.to_dict()
# create an instance of SubscribersResponse from a dict
subscribers_response_from_dict = SubscribersResponse.from_dict(subscribers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


