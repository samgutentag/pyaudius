# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.models.user import User

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> User:
        """Test User
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `User`
        """
        model = User()
        if include_optional:
            return User(
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
                wallet = ''
            )
        else:
            return User(
                album_count = 56,
                followee_count = 56,
                follower_count = 56,
                handle = '',
                id = '',
                is_verified = True,
                verified_with_twitter = True,
                verified_with_instagram = True,
                verified_with_tiktok = True,
                name = '',
                playlist_count = 56,
                repost_count = 56,
                track_count = 56,
                is_deactivated = True,
                is_available = True,
                erc_wallet = '',
                spl_wallet = '',
                supporter_count = 56,
                supporting_count = 56,
                total_audio_balance = 56,
                wallet = '',
        )
        """

    def testUser(self):
        """Test User"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
