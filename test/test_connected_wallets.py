# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.models.connected_wallets import ConnectedWallets

class TestConnectedWallets(unittest.TestCase):
    """ConnectedWallets unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectedWallets:
        """Test ConnectedWallets
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectedWallets`
        """
        model = ConnectedWallets()
        if include_optional:
            return ConnectedWallets(
                erc_wallets = [
                    ''
                    ],
                spl_wallets = [
                    ''
                    ]
            )
        else:
            return ConnectedWallets(
                erc_wallets = [
                    ''
                    ],
                spl_wallets = [
                    ''
                    ],
        )
        """

    def testConnectedWallets(self):
        """Test ConnectedWallets"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
