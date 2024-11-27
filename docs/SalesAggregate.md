# SalesAggregate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | 
**content_id** | **str** |  | 
**purchase_count** | **int** |  | 

## Example

```python
from pyaudius.models.sales_aggregate import SalesAggregate

# TODO update the JSON string below
json = "{}"
# create an instance of SalesAggregate from a JSON string
sales_aggregate_instance = SalesAggregate.from_json(json)
# print the JSON string representation of the object
print(SalesAggregate.to_json())

# convert the object into a dict
sales_aggregate_dict = sales_aggregate_instance.to_dict()
# create an instance of SalesAggregate from a dict
sales_aggregate_from_dict = SalesAggregate.from_dict(sales_aggregate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


