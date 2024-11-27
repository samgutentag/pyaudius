# RemixedTrackAggregate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track_id** | **str** |  | 
**title** | **str** |  | 
**remix_count** | **int** |  | 

## Example

```python
from pyaudius.models.remixed_track_aggregate import RemixedTrackAggregate

# TODO update the JSON string below
json = "{}"
# create an instance of RemixedTrackAggregate from a JSON string
remixed_track_aggregate_instance = RemixedTrackAggregate.from_json(json)
# print the JSON string representation of the object
print(RemixedTrackAggregate.to_json())

# convert the object into a dict
remixed_track_aggregate_dict = remixed_track_aggregate_instance.to_dict()
# create an instance of RemixedTrackAggregate from a dict
remixed_track_aggregate_from_dict = RemixedTrackAggregate.from_dict(remixed_track_aggregate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


