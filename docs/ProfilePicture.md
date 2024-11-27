# ProfilePicture


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_150x150** | **str** |  | [optional] 
**var_480x480** | **str** |  | [optional] 
**var_1000x1000** | **str** |  | [optional] 

## Example

```python
from pyaudius.models.profile_picture import ProfilePicture

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilePicture from a JSON string
profile_picture_instance = ProfilePicture.from_json(json)
# print the JSON string representation of the object
print(ProfilePicture.to_json())

# convert the object into a dict
profile_picture_dict = profile_picture_instance.to_dict()
# create an instance of ProfilePicture from a dict
profile_picture_from_dict = ProfilePicture.from_dict(profile_picture_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


