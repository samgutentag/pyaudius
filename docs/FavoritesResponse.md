# FavoritesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Favorite]**](Favorite.md) |  | [optional] 

## Example

```python
from pyaudius.models.favorites_response import FavoritesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FavoritesResponse from a JSON string
favorites_response_instance = FavoritesResponse.from_json(json)
# print the JSON string representation of the object
print(FavoritesResponse.to_json())

# convert the object into a dict
favorites_response_dict = favorites_response_instance.to_dict()
# create an instance of FavoritesResponse from a dict
favorites_response_from_dict = FavoritesResponse.from_dict(favorites_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


