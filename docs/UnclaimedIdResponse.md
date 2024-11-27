# UnclaimedIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 

## Example

```python
from pyaudius.models.unclaimed_id_response import UnclaimedIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnclaimedIdResponse from a JSON string
unclaimed_id_response_instance = UnclaimedIdResponse.from_json(json)
# print the JSON string representation of the object
print(UnclaimedIdResponse.to_json())

# convert the object into a dict
unclaimed_id_response_dict = unclaimed_id_response_instance.to_dict()
# create an instance of UnclaimedIdResponse from a dict
unclaimed_id_response_from_dict = UnclaimedIdResponse.from_dict(unclaimed_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


