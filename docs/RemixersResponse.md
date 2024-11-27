# RemixersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from pyaudius.models.remixers_response import RemixersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemixersResponse from a JSON string
remixers_response_instance = RemixersResponse.from_json(json)
# print the JSON string representation of the object
print(RemixersResponse.to_json())

# convert the object into a dict
remixers_response_dict = remixers_response_instance.to_dict()
# create an instance of RemixersResponse from a dict
remixers_response_from_dict = RemixersResponse.from_dict(remixers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


