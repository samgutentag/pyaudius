# RelatedArtistResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from pyaudius.models.related_artist_response import RelatedArtistResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedArtistResponse from a JSON string
related_artist_response_instance = RelatedArtistResponse.from_json(json)
# print the JSON string representation of the object
print(RelatedArtistResponse.to_json())

# convert the object into a dict
related_artist_response_dict = related_artist_response_instance.to_dict()
# create an instance of RelatedArtistResponse from a dict
related_artist_response_from_dict = RelatedArtistResponse.from_dict(related_artist_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


