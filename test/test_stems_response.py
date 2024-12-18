# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.models.stems_response import StemsResponse

class TestStemsResponse(unittest.TestCase):
    """StemsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StemsResponse:
        """Test StemsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StemsResponse`
        """
        model = StemsResponse()
        if include_optional:
            return StemsResponse(
                data = [
                    pyaudius.models.stem.stem(
                        id = '', 
                        parent_id = '', 
                        category = '', 
                        cid = '', 
                        user_id = '', 
                        blocknumber = 56, 
                        orig_filename = '', )
                    ]
            )
        else:
            return StemsResponse(
        )
        """

    def testStemsResponse(self):
        """Test StemsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
