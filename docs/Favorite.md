# Favorite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite_item_id** | **str** |  | 
**favorite_type** | **str** |  | 
**user_id** | **str** |  | 
**created_at** | **str** |  | 

## Example

```python
from pyaudius.models.favorite import Favorite

# TODO update the JSON string below
json = "{}"
# create an instance of Favorite from a JSON string
favorite_instance = Favorite.from_json(json)
# print the JSON string representation of the object
print(Favorite.to_json())

# convert the object into a dict
favorite_dict = favorite_instance.to_dict()
# create an instance of Favorite from a dict
favorite_from_dict = Favorite.from_dict(favorite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


