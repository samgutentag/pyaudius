# Supporter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** |  | 
**amount** | **str** |  | 
**sender** | [**User**](User.md) |  | 

## Example

```python
from pyaudius.models.supporter import Supporter

# TODO update the JSON string below
json = "{}"
# create an instance of Supporter from a JSON string
supporter_instance = Supporter.from_json(json)
# print the JSON string representation of the object
print(Supporter.to_json())

# convert the object into a dict
supporter_dict = supporter_instance.to_dict()
# create an instance of Supporter from a dict
supporter_from_dict = Supporter.from_dict(supporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


