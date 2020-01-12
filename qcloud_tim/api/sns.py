# -*- coding: utf-8 -*-


from . import BaseRESTAPI


class SNS(BaseRESTAPI):
    """ 关系链管理

    """

    ADD_TYPE_BOTH = 'Add_Type_Both'
    ADD_TYPE_SINGLE = 'Add_Type_Single'

    FORCE_ADD_FLAGS_YES = 1
    FORCE_ADD_FLAGS_NO = 0

    DELETE_TYPE_SINGLE = 'Delete_Type_Single'
    DELETE_TYPE_BOTH = 'Delete_Type_Both'

    CHECK_RESULT_TYPE_SINGLE = 'CheckResult_Type_Single'
    CHECK_RESULT_TYPE_BOTH = 'CheckResult_Type_Both'
    BLACK_CHECK_RESULT_TYPE_SINGLE = 'BlackCheckResult_Type_Single'
    BLACK_CHECK_RESULT_TYPE_BOTH = 'BlackCheckResult_Type_Both'

    def friend_add(self, from_account, add_friend_item, add_type=ADD_TYPE_BOTH, force_add_flags=FORCE_ADD_FLAGS_YES):
        """添加好友

        https://cloud.tencent.com/document/product/269/1643
        """
        data = {
            'From_Account': from_account,
            'AddFriendItem': add_friend_item,
            'AddType': add_type,
            'ForceAddFlags': force_add_flags
        }

        return self._post(
            'sns/friend_add',
            data=data
        )

    def friend_import(self, from_account, add_friend_item):
        """导入好友

        https://cloud.tencent.com/document/product/269/8301
        """
        data = {
            'From_Account': from_account,
            'AddFriendItem': add_friend_item,
        }

        return self._post(
            'sns/friend_import',
            data=data
        )

    def friend_update(self, from_account, update_item):
        """更新好友

        https://cloud.tencent.com/document/product/269/12525
        """
        data = {
            'From_Account': from_account,
            'UpdateItem': update_item,
        }

        return self._post(
            'sns/friend_update',
            data=data
        )

    def friend_delete(self, from_account, to_account, delete_type=DELETE_TYPE_BOTH):
        """删除好友

        https://cloud.tencent.com/document/product/269/1644
        """
        data = {
            'From_Account': from_account,
            'To_Account': to_account,
            'DeleteType': delete_type,
        }

        return self._post(
            'sns/friend_delete',
            data=data
        )

    def friend_delete_all(self, from_account, delete_type=DELETE_TYPE_BOTH):
        """删除所有好友

        https://cloud.tencent.com/document/product/269/1645
        """
        data = {
            'From_Account': from_account,
            'DeleteType': delete_type,
        }

        return self._post(
            'sns/friend_delete_all',
            data=data
        )

    def friend_check(self, from_account, to_account, check_type=CHECK_RESULT_TYPE_BOTH):
        """校验好友

        https://cloud.tencent.com/document/product/269/1645
        """
        data = {
            'From_Account': from_account,
            'To_Account': to_account,
            'CheckType': check_type
        }

        return self._post(
            'sns/friend_check',
            data=data
        )

    def friend_get(self, from_account, start_index=0, standard_sequence=None, custom_sequence=None):
        """拉取好友

        https://cloud.tencent.com/document/product/269/1647
        """
        data = {
            'From_Account': from_account,
            'StartIndex': start_index,
        }
        if standard_sequence:
            data['StandardSequence']: standard_sequence
        if custom_sequence:
            data['StandardSequence']: custom_sequence

        return self._post(
            'sns/friend_get',
            data=data
        )

    def friend_get_list(self, from_account, to_account, tag_list=None):
        """拉取指定好友

        https://cloud.tencent.com/document/product/269/8609
        """
        data = {
            'From_Account': from_account,
            'To_Account': to_account,
            'TagList': tag_list or [
                "Tag_Profile_IM_Image",
                "Tag_Profile_IM_Nick",
                "Tag_SNS_IM_Remark",
                "Tag_SNS_IM_Group"
            ],
        }

        return self._post(
            'sns/friend_get_list',
            data=data
        )

    def black_list_add(self, from_account, to_account):
        """添加黑名单

        https://cloud.tencent.com/document/product/269/3718
        """
        data = {
            'From_Account': from_account,
            'To_Account': to_account,
        }

        return self._post(
            'sns/black_list_add',
            data=data
        )

    def black_list_delete(self, from_account, to_account):
        """删除黑名单

        https://cloud.tencent.com/document/product/269/3719
        """
        data = {
            'From_Account': from_account,
            'To_Account': to_account,
        }

        return self._post(
            'sns/black_list_delete',
            data=data
        )

    def black_list_get(self, from_account, start_index=0, max_limited=30, last_sequence=0):
        """拉取黑名单

        https://cloud.tencent.com/document/product/269/3719
        """
        data = {
            'From_Account': from_account,
            'StartIndex': start_index,
            'MaxLimited': max_limited,
            'LastSequence': last_sequence
        }

        return self._post(
            'sns/black_list_get',
            data=data
        )

    def black_list_check(self, from_account, to_account, check_type=BLACK_CHECK_RESULT_TYPE_BOTH):
        """校验黑名单

        https://cloud.tencent.com/document/product/269/3725
        """
        data = {
            'From_Account': from_account,
            'To_Account': to_account,
            'CheckType': check_type,
        }

        return self._post(
            'sns/black_list_check',
            data=data
        )

    def group_add(self, from_account, group_name, to_account=None):
        """添加分组

        https://cloud.tencent.com/document/product/269/10107
        """
        data = {
            'From_Account': from_account,
            'GroupName': group_name,
        }
        if to_account:
            data['To_Account'] = to_account

        return self._post(
            'sns/group_add',
            data=data
        )

    def group_delete(self, from_account, group_name):
        """删除分组

        https://cloud.tencent.com/document/product/269/10108
        """
        data = {
            'From_Account': from_account,
            'GroupName': group_name,
        }

        return self._post(
            'sns/group_delete',
            data=data
        )
