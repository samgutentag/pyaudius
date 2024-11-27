# AccessInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TrackAccessInfo**](TrackAccessInfo.md) |  | [optional] 

## Example

```python
from pyaudius.models.access_info_response import AccessInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessInfoResponse from a JSON string
access_info_response_instance = AccessInfoResponse.from_json(json)
# print the JSON string representation of the object
print(AccessInfoResponse.to_json())

# convert the object into a dict
access_info_response_dict = access_info_response_instance.to_dict()
# create an instance of AccessInfoResponse from a dict
access_info_response_from_dict = AccessInfoResponse.from_dict(access_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


