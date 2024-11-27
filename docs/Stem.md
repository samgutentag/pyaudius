# Stem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**parent_id** | **str** |  | 
**category** | **str** |  | 
**cid** | **str** |  | 
**user_id** | **str** |  | 
**blocknumber** | **int** |  | 
**orig_filename** | **str** |  | 

## Example

```python
from pyaudius.models.stem import Stem

# TODO update the JSON string below
json = "{}"
# create an instance of Stem from a JSON string
stem_instance = Stem.from_json(json)
# print the JSON string representation of the object
print(Stem.to_json())

# convert the object into a dict
stem_dict = stem_instance.to_dict()
# create an instance of Stem from a dict
stem_from_dict = Stem.from_dict(stem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


