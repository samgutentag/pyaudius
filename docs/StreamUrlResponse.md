# StreamUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | 

## Example

```python
from pyaudius.models.stream_url_response import StreamUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreamUrlResponse from a JSON string
stream_url_response_instance = StreamUrlResponse.from_json(json)
# print the JSON string representation of the object
print(StreamUrlResponse.to_json())

# convert the object into a dict
stream_url_response_dict = stream_url_response_instance.to_dict()
# create an instance of StreamUrlResponse from a dict
stream_url_response_from_dict = StreamUrlResponse.from_dict(stream_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


