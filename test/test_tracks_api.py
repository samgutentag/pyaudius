# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.api.tracks_api import TracksApi


class TestTracksApi(unittest.TestCase):
    """TracksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TracksApi()

    def tearDown(self) -> None:
        pass

    def test_download_track(self) -> None:
        """Test case for download_track

        Download the original or MP3 file of a track
        """
        pass

    def test_get_bulk_tracks(self) -> None:
        """Test case for get_bulk_tracks

        """
        pass

    def test_get_track(self) -> None:
        """Test case for get_track

        """
        pass

    def test_get_track_access_info(self) -> None:
        """Test case for get_track_access_info

        """
        pass

    def test_get_track_stems(self) -> None:
        """Test case for get_track_stems

        """
        pass

    def test_get_track_top_listeners(self) -> None:
        """Test case for get_track_top_listeners

        """
        pass

    def test_get_trending_tracks(self) -> None:
        """Test case for get_trending_tracks

        """
        pass

    def test_get_underground_trending_tracks(self) -> None:
        """Test case for get_underground_trending_tracks

        """
        pass

    def test_inspect_track(self) -> None:
        """Test case for inspect_track

        Inspects the details of the file for a track
        """
        pass

    def test_search_tracks(self) -> None:
        """Test case for search_tracks

        """
        pass

    def test_stream_track(self) -> None:
        """Test case for stream_track

        Get the streamable MP3 file of a track
        """
        pass

    def test_track_comment_count(self) -> None:
        """Test case for track_comment_count

        """
        pass

    def test_track_comment_notification_setting(self) -> None:
        """Test case for track_comment_notification_setting

        """
        pass

    def test_track_comments(self) -> None:
        """Test case for track_comments

        """
        pass


if __name__ == '__main__':
    unittest.main()
