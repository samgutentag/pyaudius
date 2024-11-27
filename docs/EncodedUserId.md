# EncodedUserId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 

## Example

```python
from pyaudius.models.encoded_user_id import EncodedUserId

# TODO update the JSON string below
json = "{}"
# create an instance of EncodedUserId from a JSON string
encoded_user_id_instance = EncodedUserId.from_json(json)
# print the JSON string representation of the object
print(EncodedUserId.to_json())

# convert the object into a dict
encoded_user_id_dict = encoded_user_id_instance.to_dict()
# create an instance of EncodedUserId from a dict
encoded_user_id_from_dict = EncodedUserId.from_dict(encoded_user_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


