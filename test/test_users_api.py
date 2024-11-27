# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.api.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersApi()

    def tearDown(self) -> None:
        pass

    def test_download_purchases_as_csv(self) -> None:
        """Test case for download_purchases_as_csv

        """
        pass

    def test_download_sales_as_csv(self) -> None:
        """Test case for download_sales_as_csv

        """
        pass

    def test_download_sales_as_json(self) -> None:
        """Test case for download_sales_as_json

        """
        pass

    def test_download_usdc_withdrawals_as_csv(self) -> None:
        """Test case for download_usdc_withdrawals_as_csv

        """
        pass

    def test_get_ai_attributed_tracks_by_user_handle(self) -> None:
        """Test case for get_ai_attributed_tracks_by_user_handle

        """
        pass

    def test_get_albums_by_user(self) -> None:
        """Test case for get_albums_by_user

        """
        pass

    def test_get_authorized_apps(self) -> None:
        """Test case for get_authorized_apps

        """
        pass

    def test_get_bulk_users(self) -> None:
        """Test case for get_bulk_users

        """
        pass

    def test_get_connected_wallets(self) -> None:
        """Test case for get_connected_wallets

        """
        pass

    def test_get_developer_apps(self) -> None:
        """Test case for get_developer_apps

        """
        pass

    def test_get_favorites(self) -> None:
        """Test case for get_favorites

        """
        pass

    def test_get_followers(self) -> None:
        """Test case for get_followers

        """
        pass

    def test_get_following(self) -> None:
        """Test case for get_following

        """
        pass

    def test_get_muted_users(self) -> None:
        """Test case for get_muted_users

        """
        pass

    def test_get_playlists_by_user(self) -> None:
        """Test case for get_playlists_by_user

        """
        pass

    def test_get_purchasers(self) -> None:
        """Test case for get_purchasers

        """
        pass

    def test_get_related_users(self) -> None:
        """Test case for get_related_users

        """
        pass

    def test_get_remixers(self) -> None:
        """Test case for get_remixers

        """
        pass

    def test_get_reposts(self) -> None:
        """Test case for get_reposts

        """
        pass

    def test_get_sales_aggregate(self) -> None:
        """Test case for get_sales_aggregate

        """
        pass

    def test_get_subscribers(self) -> None:
        """Test case for get_subscribers

        """
        pass

    def test_get_supported_users(self) -> None:
        """Test case for get_supported_users

        """
        pass

    def test_get_supporters(self) -> None:
        """Test case for get_supporters

        """
        pass

    def test_get_top_track_tags(self) -> None:
        """Test case for get_top_track_tags

        Fetch most used tags in a user's tracks
        """
        pass

    def test_get_tracks_by_user(self) -> None:
        """Test case for get_tracks_by_user

        """
        pass

    def test_get_user(self) -> None:
        """Test case for get_user

        """
        pass

    def test_get_user_by_handle(self) -> None:
        """Test case for get_user_by_handle

        """
        pass

    def test_get_user_challenges(self) -> None:
        """Test case for get_user_challenges

        """
        pass

    def test_get_user_id_from_wallet(self) -> None:
        """Test case for get_user_id_from_wallet

        """
        pass

    def test_get_user_tracks_remixed(self) -> None:
        """Test case for get_user_tracks_remixed

        """
        pass

    def test_search_users(self) -> None:
        """Test case for search_users

        """
        pass

    def test_verify_id_token(self) -> None:
        """Test case for verify_id_token

        """
        pass


if __name__ == '__main__':
    unittest.main()