# Supporting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** |  | 
**amount** | **str** |  | 
**receiver** | [**User**](User.md) |  | 

## Example

```python
from pyaudius.models.supporting import Supporting

# TODO update the JSON string below
json = "{}"
# create an instance of Supporting from a JSON string
supporting_instance = Supporting.from_json(json)
# print the JSON string representation of the object
print(Supporting.to_json())

# convert the object into a dict
supporting_dict = supporting_instance.to_dict()
# create an instance of Supporting from a dict
supporting_from_dict = Supporting.from_dict(supporting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


