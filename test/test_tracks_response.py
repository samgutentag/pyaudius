# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.models.tracks_response import TracksResponse

class TestTracksResponse(unittest.TestCase):
    """TracksResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TracksResponse:
        """Test TracksResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TracksResponse`
        """
        model = TracksResponse()
        if include_optional:
            return TracksResponse(
                data = [
                    pyaudius.models.track.Track(
                        artwork = pyaudius.models.track_artwork.track_artwork(
                            150x150 = '', 
                            480x480 = '', 
                            1000x1000 = '', ), 
                        description = '', 
                        genre = '', 
                        id = '', 
                        track_cid = '', 
                        preview_cid = '', 
                        orig_file_cid = '', 
                        orig_filename = '', 
                        is_original_available = True, 
                        mood = '', 
                        release_date = '', 
                        remix_of = pyaudius.models.remix_parent.remix_parent(
                            tracks = [
                                pyaudius.models.track_element.track_element(
                                    parent_track_id = '', )
                                ], ), 
                        repost_count = 56, 
                        favorite_count = 56, 
                        comment_count = 56, 
                        tags = '', 
                        title = '', 
                        user = pyaudius.models.user.user(
                            album_count = 56, 
                            artist_pick_track_id = '', 
                            bio = '', 
                            cover_photo = pyaudius.models.cover_photo.cover_photo(
                                640x = '', 
                                2000x = '', ), 
                            followee_count = 56, 
                            follower_count = 56, 
                            handle = '', 
                            id = '', 
                            is_verified = True, 
                            twitter_handle = '', 
                            instagram_handle = '', 
                            tiktok_handle = '', 
                            verified_with_twitter = True, 
                            verified_with_instagram = True, 
                            verified_with_tiktok = True, 
                            website = '', 
                            donation = '', 
                            location = '', 
                            name = '', 
                            playlist_count = 56, 
                            profile_picture = pyaudius.models.profile_picture.profile_picture(
                                150x150 = '', 
                                480x480 = '', 
                                1000x1000 = '', ), 
                            repost_count = 56, 
                            track_count = 56, 
                            is_deactivated = True, 
                            is_available = True, 
                            erc_wallet = '', 
                            spl_wallet = '', 
                            spl_usdc_payout_wallet = '', 
                            supporter_count = 56, 
                            supporting_count = 56, 
                            total_audio_balance = 56, 
                            wallet = '', ), 
                        duration = 56, 
                        is_downloadable = True, 
                        play_count = 56, 
                        permalink = '', 
                        is_streamable = True, 
                        ddex_app = '', 
                        playlists_containing_track = [
                            56
                            ], 
                        pinned_comment_id = 56, )
                    ]
            )
        else:
            return TracksResponse(
        )
        """

    def testTracksResponse(self):
        """Test TracksResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
