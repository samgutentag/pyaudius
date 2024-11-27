# GetSupporters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Supporter]**](Supporter.md) |  | [optional] 

## Example

```python
from pyaudius.models.get_supporters import GetSupporters

# TODO update the JSON string below
json = "{}"
# create an instance of GetSupporters from a JSON string
get_supporters_instance = GetSupporters.from_json(json)
# print the JSON string representation of the object
print(GetSupporters.to_json())

# convert the object into a dict
get_supporters_dict = get_supporters_instance.to_dict()
# create an instance of GetSupporters from a dict
get_supporters_from_dict = GetSupporters.from_dict(get_supporters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


