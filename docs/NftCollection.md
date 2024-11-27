# NftCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | **str** |  | 
**standard** | **str** |  | [optional] 
**address** | **str** |  | 
**name** | **str** |  | 
**image_url** | **str** |  | [optional] 
**external_link** | **str** |  | [optional] 

## Example

```python
from pyaudius.models.nft_collection import NftCollection

# TODO update the JSON string below
json = "{}"
# create an instance of NftCollection from a JSON string
nft_collection_instance = NftCollection.from_json(json)
# print the JSON string representation of the object
print(NftCollection.to_json())

# convert the object into a dict
nft_collection_dict = nft_collection_instance.to_dict()
# create an instance of NftCollection from a dict
nft_collection_from_dict = NftCollection.from_dict(nft_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


