# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.models.extended_usdc_gate import ExtendedUsdcGate

class TestExtendedUsdcGate(unittest.TestCase):
    """ExtendedUsdcGate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtendedUsdcGate:
        """Test ExtendedUsdcGate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtendedUsdcGate`
        """
        model = ExtendedUsdcGate()
        if include_optional:
            return ExtendedUsdcGate(
                price = 56,
                splits = [
                    pyaudius.models.extended_payment_split.extended_payment_split(
                        user_id = 56, 
                        percentage = 1.337, 
                        eth_wallet = '', 
                        payout_wallet = '', 
                        amount = 56, )
                    ]
            )
        else:
            return ExtendedUsdcGate(
                price = 56,
                splits = [
                    pyaudius.models.extended_payment_split.extended_payment_split(
                        user_id = 56, 
                        percentage = 1.337, 
                        eth_wallet = '', 
                        payout_wallet = '', 
                        amount = 56, )
                    ],
        )
        """

    def testExtendedUsdcGate(self):
        """Test ExtendedUsdcGate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
