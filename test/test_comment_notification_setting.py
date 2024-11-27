# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyaudius.models.comment_notification_setting import CommentNotificationSetting

class TestCommentNotificationSetting(unittest.TestCase):
    """CommentNotificationSetting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommentNotificationSetting:
        """Test CommentNotificationSetting
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommentNotificationSetting`
        """
        model = CommentNotificationSetting()
        if include_optional:
            return CommentNotificationSetting(
                is_muted = True
            )
        else:
            return CommentNotificationSetting(
                is_muted = True,
        )
        """

    def testCommentNotificationSetting(self):
        """Test CommentNotificationSetting"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()