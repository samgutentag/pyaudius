# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.models.favorites_response import FavoritesResponse

class TestFavoritesResponse(unittest.TestCase):
    """FavoritesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FavoritesResponse:
        """Test FavoritesResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FavoritesResponse`
        """
        model = FavoritesResponse()
        if include_optional:
            return FavoritesResponse(
                data = [
                    pyaudius.models.favorite.favorite(
                        favorite_item_id = '', 
                        favorite_type = '', 
                        user_id = '', 
                        created_at = '', )
                    ]
            )
        else:
            return FavoritesResponse(
        )
        """

    def testFavoritesResponse(self):
        """Test FavoritesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
