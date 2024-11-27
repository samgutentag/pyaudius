# NftGate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nft_collection** | [**NftCollection**](NftCollection.md) | Must hold an NFT of the given collection to unlock | 

## Example

```python
from pyaudius.models.nft_gate import NftGate

# TODO update the JSON string below
json = "{}"
# create an instance of NftGate from a JSON string
nft_gate_instance = NftGate.from_json(json)
# print the JSON string representation of the object
print(NftGate.to_json())

# convert the object into a dict
nft_gate_dict = nft_gate_instance.to_dict()
# create an instance of NftGate from a dict
nft_gate_from_dict = NftGate.from_dict(nft_gate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


