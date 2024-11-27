# CollectionActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**item_type** | **str** |  | 
**item** | [**Playlist**](Playlist.md) |  | 

## Example

```python
from pyaudius.models.collection_activity import CollectionActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionActivity from a JSON string
collection_activity_instance = CollectionActivity.from_json(json)
# print the JSON string representation of the object
print(CollectionActivity.to_json())

# convert the object into a dict
collection_activity_dict = collection_activity_instance.to_dict()
# create an instance of CollectionActivity from a dict
collection_activity_from_dict = CollectionActivity.from_dict(collection_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


