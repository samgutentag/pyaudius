# StemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Stem]**](Stem.md) |  | [optional] 

## Example

```python
from pyaudius.models.stems_response import StemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StemsResponse from a JSON string
stems_response_instance = StemsResponse.from_json(json)
# print the JSON string representation of the object
print(StemsResponse.to_json())

# convert the object into a dict
stems_response_dict = stems_response_instance.to_dict()
# create an instance of StemsResponse from a dict
stems_response_from_dict = StemsResponse.from_dict(stems_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


