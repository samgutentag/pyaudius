# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.models.remixed_track_aggregate import RemixedTrackAggregate

class TestRemixedTrackAggregate(unittest.TestCase):
    """RemixedTrackAggregate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemixedTrackAggregate:
        """Test RemixedTrackAggregate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemixedTrackAggregate`
        """
        model = RemixedTrackAggregate()
        if include_optional:
            return RemixedTrackAggregate(
                track_id = '',
                title = '',
                remix_count = 56
            )
        else:
            return RemixedTrackAggregate(
                track_id = '',
                title = '',
                remix_count = 56,
        )
        """

    def testRemixedTrackAggregate(self):
        """Test RemixedTrackAggregate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
