# CoverPhoto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_640x** | **str** |  | [optional] 
**var_2000x** | **str** |  | [optional] 

## Example

```python
from pyaudius.models.cover_photo import CoverPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of CoverPhoto from a JSON string
cover_photo_instance = CoverPhoto.from_json(json)
# print the JSON string representation of the object
print(CoverPhoto.to_json())

# convert the object into a dict
cover_photo_dict = cover_photo_instance.to_dict()
# create an instance of CoverPhoto from a dict
cover_photo_from_dict = CoverPhoto.from_dict(cover_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


