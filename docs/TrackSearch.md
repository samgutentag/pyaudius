# TrackSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Track]**](Track.md) |  | [optional] 

## Example

```python
from pyaudius.models.track_search import TrackSearch

# TODO update the JSON string below
json = "{}"
# create an instance of TrackSearch from a JSON string
track_search_instance = TrackSearch.from_json(json)
# print the JSON string representation of the object
print(TrackSearch.to_json())

# convert the object into a dict
track_search_dict = track_search_instance.to_dict()
# create an instance of TrackSearch from a dict
track_search_from_dict = TrackSearch.from_dict(track_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


