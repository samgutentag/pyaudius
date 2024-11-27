# SalesAggregateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SalesAggregate]**](SalesAggregate.md) |  | [optional] 

## Example

```python
from pyaudius.models.sales_aggregate_response import SalesAggregateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SalesAggregateResponse from a JSON string
sales_aggregate_response_instance = SalesAggregateResponse.from_json(json)
# print the JSON string representation of the object
print(SalesAggregateResponse.to_json())

# convert the object into a dict
sales_aggregate_response_dict = sales_aggregate_response_instance.to_dict()
# create an instance of SalesAggregateResponse from a dict
sales_aggregate_response_from_dict = SalesAggregateResponse.from_dict(sales_aggregate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


