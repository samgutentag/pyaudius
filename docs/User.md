# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_count** | **int** |  | 
**artist_pick_track_id** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**cover_photo** | [**CoverPhoto**](CoverPhoto.md) |  | [optional] 
**followee_count** | **int** |  | 
**follower_count** | **int** |  | 
**handle** | **str** |  | 
**id** | **str** |  | 
**is_verified** | **bool** |  | 
**twitter_handle** | **str** |  | [optional] 
**instagram_handle** | **str** |  | [optional] 
**tiktok_handle** | **str** |  | [optional] 
**verified_with_twitter** | **bool** |  | 
**verified_with_instagram** | **bool** |  | 
**verified_with_tiktok** | **bool** |  | 
**website** | **str** |  | [optional] 
**donation** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**name** | **str** |  | 
**playlist_count** | **int** |  | 
**profile_picture** | [**ProfilePicture**](ProfilePicture.md) |  | [optional] 
**repost_count** | **int** |  | 
**track_count** | **int** |  | 
**is_deactivated** | **bool** |  | 
**is_available** | **bool** |  | 
**erc_wallet** | **str** |  | 
**spl_wallet** | **str** |  | 
**spl_usdc_payout_wallet** | **str** |  | [optional] 
**supporter_count** | **int** |  | 
**supporting_count** | **int** |  | 
**total_audio_balance** | **int** |  | 
**wallet** | **str** | The user&#39;s Ethereum wallet address for their account | 

## Example

```python
from pyaudius.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


