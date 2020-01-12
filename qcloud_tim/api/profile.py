# -*- coding: utf-8 -*-


from . import BaseRESTAPI


class Profile(BaseRESTAPI):
    """资料管理

    """

    def portrait_get(self, to_account, tag_list=None):
        """拉取资料

        https://cloud.tencent.com/document/product/269/1639
        """
        data = {
            'To_Account': to_account,
            'TagList': tag_list or [
                "Tag_Profile_IM_Nick",
                "Tag_Profile_IM_Gender",
                "Tag_Profile_IM_BirthDay",
                "Tag_Profile_IM_AdminForbidType",
                "Tag_Profile_IM_AllowType",
                "Tag_Profile_IM_SelfSignature",
            ]

        }

        return self._post(
            'profile/portrait_get',
            data=data
        )

    def portrait_set(self, from_account, profile_item):
        """设置资料

        https://cloud.tencent.com/document/product/269/1640
        """
        data = {
            'From_Account': from_account,
            'ProfileItem': profile_item
        }

        return self._post(
            'profile/portrait_set',
            data=data
        )
