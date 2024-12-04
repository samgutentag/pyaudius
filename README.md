# pyaudius

Audius V1 API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/samgutentag/pyaudius.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/samgutentag/pyaudius.git`)

Then import the package:

```python
import pyaudius
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import pyaudius
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import pyaudius
from pyaudius.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discoveryprovider.audius.co/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pyaudius.Configuration(
    host = "https://discoveryprovider.audius.co/v1"
)



# Enter a context with an instance of the API client
with pyaudius.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyaudius.ChallengesApi(api_client)
    offset = 56 # int | The number of items to skip. Useful for pagination (page number * limit) (optional)
    limit = 56 # int | The number of items to fetch (optional)
    user_id = 'user_id_example' # str | A User ID to filter the undisbursed challenges to a particular user (optional)
    completed_blocknumber = 56 # int | Starting blocknumber to retrieve completed undisbursed challenges (optional)

    try:
        api_response = api_instance.get_undisbursed_challenges(offset=offset, limit=limit, user_id=user_id, completed_blocknumber=completed_blocknumber)
        print("The response of ChallengesApi->get_undisbursed_challenges:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengesApi->get_undisbursed_challenges: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://discoveryprovider.audius.co/v1*

| Class                     | Method                                                                                                  | HTTP request                                            | Description                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| _ChallengesApi_           | [**get_undisbursed_challenges**](docs/ChallengesApi.md#get_undisbursed_challenges)                      | **GET** /challenges/undisbursed                         |
| _CommentsApi_             | [**get_comment_replies**](docs/CommentsApi.md#get_comment_replies)                                      | **GET** /comments/{comment_id}/replies                  |
| _CommentsApi_             | [**get_unclaimed_comment_id**](docs/CommentsApi.md#get_unclaimed_comment_id)                            | **GET** /comments/unclaimed_id                          |
| _DashboardWalletUsersApi_ | [**bulk_get_dashboard_wallet_users**](docs/DashboardWalletUsersApi.md#bulk_get_dashboard_wallet_users)  | **GET** /dashboard_wallet_users                         |
| _DeveloperAppsApi_        | [**get_developer_app**](docs/DeveloperAppsApi.md#get_developer_app)                                     | **GET** /developer_apps/{address}                       |
| _PlaylistsApi_            | [**get_bulk_playlists**](docs/PlaylistsApi.md#get_bulk_playlists)                                       | **GET** /playlists                                      |
| _PlaylistsApi_            | [**get_playlist**](docs/PlaylistsApi.md#get_playlist)                                                   | **GET** /playlists/{playlist_id}                        |
| _PlaylistsApi_            | [**get_playlist_access_info**](docs/PlaylistsApi.md#get_playlist_access_info)                           | **GET** /playlists/{playlist_id}/access-info            |
| _PlaylistsApi_            | [**get_playlist_by_handle_and_slug**](docs/PlaylistsApi.md#get_playlist_by_handle_and_slug)             | **GET** /playlists/by_permalink/{handle}/{slug}         |
| _PlaylistsApi_            | [**get_playlist_tracks**](docs/PlaylistsApi.md#get_playlist_tracks)                                     | **GET** /playlists/{playlist_id}/tracks                 |
| _PlaylistsApi_            | [**get_trending_playlists**](docs/PlaylistsApi.md#get_trending_playlists)                               | **GET** /playlists/trending                             |
| _PlaylistsApi_            | [**search_playlists**](docs/PlaylistsApi.md#search_playlists)                                           | **GET** /playlists/search                               |
| _ResolveApi_              | [**resolve**](docs/ResolveApi.md#resolve)                                                               | **GET** /resolve                                        | Resolves and redirects a provided Audius app URL to the API resource URL it represents |
| _TipsApi_                 | [**get_tips**](docs/TipsApi.md#get_tips)                                                                | **GET** /tips                                           |
| _TracksApi_               | [**download_track**](docs/TracksApi.md#download_track)                                                  | **GET** /tracks/{track_id}/download                     | Download the original or MP3 file of a track                                           |
| _TracksApi_               | [**get_bulk_tracks**](docs/TracksApi.md#get_bulk_tracks)                                                | **GET** /tracks                                         |
| _TracksApi_               | [**get_track**](docs/TracksApi.md#get_track)                                                            | **GET** /tracks/{track_id}                              |
| _TracksApi_               | [**get_track_access_info**](docs/TracksApi.md#get_track_access_info)                                    | **GET** /tracks/{track_id}/access-info                  |
| _TracksApi_               | [**get_track_stems**](docs/TracksApi.md#get_track_stems)                                                | **GET** /tracks/{track_id}/stems                        |
| _TracksApi_               | [**get_track_top_listeners**](docs/TracksApi.md#get_track_top_listeners)                                | **GET** /tracks/{track_id}/top_listeners                |
| _TracksApi_               | [**get_trending_tracks**](docs/TracksApi.md#get_trending_tracks)                                        | **GET** /tracks/trending                                |
| _TracksApi_               | [**get_underground_trending_tracks**](docs/TracksApi.md#get_underground_trending_tracks)                | **GET** /tracks/trending/underground                    |
| _TracksApi_               | [**inspect_track**](docs/TracksApi.md#inspect_track)                                                    | **GET** /tracks/{track_id}/inspect                      | Inspects the details of the file for a track                                           |
| _TracksApi_               | [**search_tracks**](docs/TracksApi.md#search_tracks)                                                    | **GET** /tracks/search                                  |
| _TracksApi_               | [**stream_track**](docs/TracksApi.md#stream_track)                                                      | **GET** /tracks/{track_id}/stream                       | Get the streamable MP3 file of a track                                                 |
| _TracksApi_               | [**track_comment_count**](docs/TracksApi.md#track_comment_count)                                        | **GET** /tracks/{track_id}/comment_count                |
| _TracksApi_               | [**track_comment_notification_setting**](docs/TracksApi.md#track_comment_notification_setting)          | **GET** /tracks/{track_id}/comment_notification_setting |
| _TracksApi_               | [**track_comments**](docs/TracksApi.md#track_comments)                                                  | **GET** /tracks/{track_id}/comments                     |
| _UsersApi_                | [**download_purchases_as_csv**](docs/UsersApi.md#download_purchases_as_csv)                             | **GET** /users/{id}/purchases/download                  |
| _UsersApi_                | [**download_sales_as_csv**](docs/UsersApi.md#download_sales_as_csv)                                     | **GET** /users/{id}/sales/download                      |
| _UsersApi_                | [**download_sales_as_json**](docs/UsersApi.md#download_sales_as_json)                                   | **GET** /users/{id}/sales/download/json                 |
| _UsersApi_                | [**download_usdc_withdrawals_as_csv**](docs/UsersApi.md#download_usdc_withdrawals_as_csv)               | **GET** /users/{id}/withdrawals/download                |
| _UsersApi_                | [**get_ai_attributed_tracks_by_user_handle**](docs/UsersApi.md#get_ai_attributed_tracks_by_user_handle) | **GET** /users/handle/{handle}/tracks/ai_attributed     |
| _UsersApi_                | [**get_albums_by_user**](docs/UsersApi.md#get_albums_by_user)                                           | **GET** /users/{id}/albums                              |
| _UsersApi_                | [**get_authorized_apps**](docs/UsersApi.md#get_authorized_apps)                                         | **GET** /users/{id}/authorized_apps                     |
| _UsersApi_                | [**get_bulk_users**](docs/UsersApi.md#get_bulk_users)                                                   | **GET** /users                                          |
| _UsersApi_                | [**get_connected_wallets**](docs/UsersApi.md#get_connected_wallets)                                     | **GET** /users/{id}/connected_wallets                   |
| _UsersApi_                | [**get_developer_apps**](docs/UsersApi.md#get_developer_apps)                                           | **GET** /users/{id}/developer_apps                      |
| _UsersApi_                | [**get_favorites**](docs/UsersApi.md#get_favorites)                                                     | **GET** /users/{id}/favorites                           |
| _UsersApi_                | [**get_followers**](docs/UsersApi.md#get_followers)                                                     | **GET** /users/{id}/followers                           |
| _UsersApi_                | [**get_following**](docs/UsersApi.md#get_following)                                                     | **GET** /users/{id}/following                           |
| _UsersApi_                | [**get_muted_users**](docs/UsersApi.md#get_muted_users)                                                 | **GET** /users/{id}/muted                               |
| _UsersApi_                | [**get_playlists_by_user**](docs/UsersApi.md#get_playlists_by_user)                                     | **GET** /users/{id}/playlists                           |
| _UsersApi_                | [**get_purchasers**](docs/UsersApi.md#get_purchasers)                                                   | **GET** /users/{id}/purchasers                          |
| _UsersApi_                | [**get_related_users**](docs/UsersApi.md#get_related_users)                                             | **GET** /users/{id}/related                             |
| _UsersApi_                | [**get_remixers**](docs/UsersApi.md#get_remixers)                                                       | **GET** /users/{id}/remixers                            |
| _UsersApi_                | [**get_reposts**](docs/UsersApi.md#get_reposts)                                                         | **GET** /users/{id}/reposts                             |
| _UsersApi_                | [**get_sales_aggregate**](docs/UsersApi.md#get_sales_aggregate)                                         | **GET** /users/{id}/sales/aggregate                     |
| _UsersApi_                | [**get_subscribers**](docs/UsersApi.md#get_subscribers)                                                 | **GET** /users/{id}/subscribers                         |
| _UsersApi_                | [**get_supported_users**](docs/UsersApi.md#get_supported_users)                                         | **GET** /users/{id}/supporting                          |
| _UsersApi_                | [**get_supporters**](docs/UsersApi.md#get_supporters)                                                   | **GET** /users/{id}/supporters                          |
| _UsersApi_                | [**get_top_track_tags**](docs/UsersApi.md#get_top_track_tags)                                           | **GET** /users/{id}/tags                                | Fetch most used tags in a user&#39;s tracks                                            |
| _UsersApi_                | [**get_tracks_by_user**](docs/UsersApi.md#get_tracks_by_user)                                           | **GET** /users/{id}/tracks                              |
| _UsersApi_                | [**get_user**](docs/UsersApi.md#get_user)                                                               | **GET** /users/{id}                                     |
| _UsersApi_                | [**get_user_by_handle**](docs/UsersApi.md#get_user_by_handle)                                           | **GET** /users/handle/{handle}                          |
| _UsersApi_                | [**get_user_challenges**](docs/UsersApi.md#get_user_challenges)                                         | **GET** /users/{id}/challenges                          |
| _UsersApi_                | [**get_user_id_from_wallet**](docs/UsersApi.md#get_user_id_from_wallet)                                 | **GET** /users/id                                       |
| _UsersApi_                | [**get_user_tracks_remixed**](docs/UsersApi.md#get_user_tracks_remixed)                                 | **GET** /users/{id}/tracks/remixed                      |
| _UsersApi_                | [**search_users**](docs/UsersApi.md#search_users)                                                       | **GET** /users/search                                   |
| _UsersApi_                | [**verify_id_token**](docs/UsersApi.md#verify_id_token)                                                 | **GET** /users/verify_token                             |

## Documentation For Models

- [Access](docs/Access.md)
- [AccessInfoResponse](docs/AccessInfoResponse.md)
- [Activity](docs/Activity.md)
- [AlbumsResponse](docs/AlbumsResponse.md)
- [AuthorizedApp](docs/AuthorizedApp.md)
- [AuthorizedApps](docs/AuthorizedApps.md)
- [BlobInfo](docs/BlobInfo.md)
- [ChallengeResponse](docs/ChallengeResponse.md)
- [CollectionActivity](docs/CollectionActivity.md)
- [Comment](docs/Comment.md)
- [CommentMention](docs/CommentMention.md)
- [CommentNotificationSetting](docs/CommentNotificationSetting.md)
- [CommentResponse](docs/CommentResponse.md)
- [ConnectedWallets](docs/ConnectedWallets.md)
- [ConnectedWalletsResponse](docs/ConnectedWalletsResponse.md)
- [CoverPhoto](docs/CoverPhoto.md)
- [DashboardWalletUser](docs/DashboardWalletUser.md)
- [DashboardWalletUsersResponse](docs/DashboardWalletUsersResponse.md)
- [DecodedUserToken](docs/DecodedUserToken.md)
- [DeveloperApp](docs/DeveloperApp.md)
- [DeveloperAppResponse](docs/DeveloperAppResponse.md)
- [DeveloperApps](docs/DeveloperApps.md)
- [EncodedUserId](docs/EncodedUserId.md)
- [ExtendedPaymentSplit](docs/ExtendedPaymentSplit.md)
- [ExtendedPurchaseGate](docs/ExtendedPurchaseGate.md)
- [ExtendedUsdcGate](docs/ExtendedUsdcGate.md)
- [Favorite](docs/Favorite.md)
- [FavoritesResponse](docs/FavoritesResponse.md)
- [FollowGate](docs/FollowGate.md)
- [FollowersResponse](docs/FollowersResponse.md)
- [FollowingResponse](docs/FollowingResponse.md)
- [GetChallenges](docs/GetChallenges.md)
- [GetSupportedUsers](docs/GetSupportedUsers.md)
- [GetSupporters](docs/GetSupporters.md)
- [GetTipsResponse](docs/GetTipsResponse.md)
- [NftCollection](docs/NftCollection.md)
- [NftGate](docs/NftGate.md)
- [Playlist](docs/Playlist.md)
- [PlaylistAddedTimestamp](docs/PlaylistAddedTimestamp.md)
- [PlaylistArtwork](docs/PlaylistArtwork.md)
- [PlaylistResponse](docs/PlaylistResponse.md)
- [PlaylistSearchResult](docs/PlaylistSearchResult.md)
- [PlaylistTracksResponse](docs/PlaylistTracksResponse.md)
- [PlaylistsResponse](docs/PlaylistsResponse.md)
- [ProfilePicture](docs/ProfilePicture.md)
- [PurchasersResponse](docs/PurchasersResponse.md)
- [RelatedArtistResponse](docs/RelatedArtistResponse.md)
- [RemixParent](docs/RemixParent.md)
- [RemixedTrackAggregate](docs/RemixedTrackAggregate.md)
- [RemixersResponse](docs/RemixersResponse.md)
- [ReplyComment](docs/ReplyComment.md)
- [Reposts](docs/Reposts.md)
- [SalesAggregate](docs/SalesAggregate.md)
- [SalesAggregateResponse](docs/SalesAggregateResponse.md)
- [Stem](docs/Stem.md)
- [StemsResponse](docs/StemsResponse.md)
- [StreamUrlResponse](docs/StreamUrlResponse.md)
- [SubscribersResponse](docs/SubscribersResponse.md)
- [Supporter](docs/Supporter.md)
- [Supporting](docs/Supporting.md)
- [TagsResponse](docs/TagsResponse.md)
- [Tip](docs/Tip.md)
- [TipGate](docs/TipGate.md)
- [TopListener](docs/TopListener.md)
- [Track](docs/Track.md)
- [TrackAccessInfo](docs/TrackAccessInfo.md)
- [TrackActivity](docs/TrackActivity.md)
- [TrackArtwork](docs/TrackArtwork.md)
- [TrackCommentCountResponse](docs/TrackCommentCountResponse.md)
- [TrackCommentNotificationResponse](docs/TrackCommentNotificationResponse.md)
- [TrackCommentsResponse](docs/TrackCommentsResponse.md)
- [TrackElement](docs/TrackElement.md)
- [TrackInspect](docs/TrackInspect.md)
- [TrackResponse](docs/TrackResponse.md)
- [TrackSearch](docs/TrackSearch.md)
- [TracksResponse](docs/TracksResponse.md)
- [TrendingPlaylistsResponse](docs/TrendingPlaylistsResponse.md)
- [UnclaimedIdResponse](docs/UnclaimedIdResponse.md)
- [UndisbursedChallenge](docs/UndisbursedChallenge.md)
- [UndisbursedChallenges](docs/UndisbursedChallenges.md)
- [User](docs/User.md)
- [UserAssociatedWalletResponse](docs/UserAssociatedWalletResponse.md)
- [UserResponse](docs/UserResponse.md)
- [UserSearch](docs/UserSearch.md)
- [UserTracksRemixedResponse](docs/UserTracksRemixedResponse.md)
- [UsersResponse](docs/UsersResponse.md)
- [VerifyToken](docs/VerifyToken.md)

<a id="documentation-for-authorization"></a>

## Documentation For Authorization

Endpoints do not require authorization.

## Author

## Build and Deploy with poetry

1. install poetry with `pip install poetry`
2. install dependencies with `poetry install`
3. build package with `poetry build`
4. publish with `poetry publish --build`

### PyPi Distribution

If you plan to distribute via PyPI, ensure you have a PyPI account and an API token configured in Poetry:
`poetry config pypi-token.pypi your-token`
