# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.models.undisbursed_challenges import UndisbursedChallenges

class TestUndisbursedChallenges(unittest.TestCase):
    """UndisbursedChallenges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UndisbursedChallenges:
        """Test UndisbursedChallenges
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UndisbursedChallenges`
        """
        model = UndisbursedChallenges()
        if include_optional:
            return UndisbursedChallenges(
                data = [
                    pyaudius.models.undisbursed_challenge.undisbursed_challenge(
                        challenge_id = '', 
                        user_id = '', 
                        specifier = '', 
                        amount = '', 
                        completed_blocknumber = 56, 
                        handle = '', 
                        wallet = '', 
                        created_at = '', 
                        completed_at = '', 
                        cooldown_days = 56, )
                    ]
            )
        else:
            return UndisbursedChallenges(
        )
        """

    def testUndisbursedChallenges(self):
        """Test UndisbursedChallenges"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
