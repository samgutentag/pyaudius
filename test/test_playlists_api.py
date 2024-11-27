# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.api.playlists_api import PlaylistsApi


class TestPlaylistsApi(unittest.TestCase):
    """PlaylistsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlaylistsApi()

    def tearDown(self) -> None:
        pass

    def test_get_bulk_playlists(self) -> None:
        """Test case for get_bulk_playlists

        """
        pass

    def test_get_playlist(self) -> None:
        """Test case for get_playlist

        """
        pass

    def test_get_playlist_access_info(self) -> None:
        """Test case for get_playlist_access_info

        """
        pass

    def test_get_playlist_by_handle_and_slug(self) -> None:
        """Test case for get_playlist_by_handle_and_slug

        """
        pass

    def test_get_playlist_tracks(self) -> None:
        """Test case for get_playlist_tracks

        """
        pass

    def test_get_trending_playlists(self) -> None:
        """Test case for get_trending_playlists

        """
        pass

    def test_search_playlists(self) -> None:
        """Test case for search_playlists

        """
        pass


if __name__ == '__main__':
    unittest.main()
