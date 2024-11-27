# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.models.blob_info import BlobInfo

class TestBlobInfo(unittest.TestCase):
    """BlobInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BlobInfo:
        """Test BlobInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlobInfo`
        """
        model = BlobInfo()
        if include_optional:
            return BlobInfo(
                size = 56,
                content_type = ''
            )
        else:
            return BlobInfo(
                size = 56,
                content_type = '',
        )
        """

    def testBlobInfo(self):
        """Test BlobInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()