# -*- coding: utf-8 -*-

import random
from . import BaseRESTAPI


class GroupOpenHttpSVC(BaseRESTAPI):
    """群组管理

    """
    TYPE_PRIVATE = 'Private'
    TYPE_PUBLIC = 'Public'
    TYPE_CHAT_ROOM = 'ChatRoom'
    TYPE_AV_CHAT_ROOM = 'AVChatRoom'
    TYPE_B_CHAT_ROOM = 'BChatRoom'

    JOIN_OPTION_FREE_ACCESS = 'FreeAccess'
    JOIN_OPTION_NEED_PERMISSION = 'NeedPermission'
    JOIN_OPTION_DISABLE_APPLY = 'DisableApply'

    SHUT_UP_ALL_MEMBER_ON = 'On'
    SHUT_UP_ALL_MEMBER_OFF = 'Off'

    SILENCE_YES = 1
    SILENCE_NO = 0

    ROLE_ADMIN = 'Admin'
    ROLE_MEMBER = 'Member'

    MSG_FLAG_ACCEPT_AND_NOTIFY = 'AcceptAndNotify'
    MSG_FLAG_DISCARD = 'Discard'
    MSG_FLAG_ACCEPT_NOT_NOTIFY = 'AcceptNotNotify'

    WITH_HUGE_GROUPS_YES = 1
    WITH_HUGE_GROUPS_NO = 0

    WITH_NO_ACTIVE_GROUPS_YES = 1
    WITH_NO_ACTIVE_GROUPS_NO = 0

    ONLINE_ONLY_FLAG_YES = 1
    ONLINE_ONLY_FLAG_NO = 0

    def get_app_id_group_list(self):
        """获取 App 中的所有群组

        https://cloud.tencent.com/document/product/269/1614
        """
        return self._get(
            'group_open_http_svc/get_appid_group_list',
            params={
            }
        )

    def create_group(self, name, owner_account=None, member_list=None, group_type=TYPE_PUBLIC, introduction=None,
                     notification=None,
                     face_url=None, max_member_count=None, apply_join_option=JOIN_OPTION_NEED_PERMISSION):
        """创建群组

        https://cloud.tencent.com/document/product/269/1615
        """
        data = {
            'Name': name,
            'Type': group_type,
        }

        if member_list:
            data['MemberList'] = member_list

        if owner_account:
            data['Owner_Account'] = owner_account

        if introduction:
            data['Introduction'] = introduction

        if notification:
            data['Notification'] = notification

        if face_url:
            data['FaceUrl'] = face_url

        if max_member_count:
            data['MaxMemberCount'] = max_member_count

        if apply_join_option:
            data['ApplyJoinOption'] = apply_join_option

        return self._post(
            'group_open_http_svc/create_group',
            data=data
        )

    def get_group_info(self, group_id_list, response_filter=None):
        """获取群组详细资料

        https://cloud.tencent.com/document/product/269/1616
        """
        data = {
            'GroupIdList': group_id_list
        }
        if response_filter:
            data['ResponseFilter'] = response_filter

        return self._post(
            'group_open_http_svc/get_group_info',
            data=data
        )

    def get_group_member_info(self, group_id, limit=None, offset=None, member_info_filter=None):
        """获取群组成员详细资料

        https://cloud.tencent.com/document/product/269/1617
        """
        data = {
            'GroupId': group_id
        }
        if limit:
            data['Limit'] = limit

        if offset:
            data['Offset'] = offset

        if member_info_filter:
            data['MemberInfoFilter'] = member_info_filter

        return self._post(
            'group_open_http_svc/get_group_member_info',
            data=data
        )

    def modify_group_base_info(self, group_id, name=None, introduction=None, notification=None, face_url=None,
                               max_member_num=None, apply_join_option=None, shut_up_all_member=None,
                               app_defined_data=None):
        """修改群组基础资料

        https://cloud.tencent.com/document/product/269/1620
        """
        data = {
            'GroupId': group_id
        }
        if name:
            data['Name'] = name

        if introduction:
            data['Introduction'] = introduction

        if notification:
            data['Notification'] = notification

        if face_url:
            data['FaceUrl'] = face_url

        if max_member_num:
            data['MaxMemberNum'] = max_member_num

        if apply_join_option:
            data['ApplyJoinOption'] = apply_join_option

        if shut_up_all_member:
            data['ShutUpAllMember'] = shut_up_all_member

        if app_defined_data:
            data['AppDefinedData'] = app_defined_data

        return self._post(
            'group_open_http_svc/modify_group_base_info',
            data=data
        )

    def add_group_member(self, group_id, member_list, silence=SILENCE_YES):
        """增加群组成员

        https://cloud.tencent.com/document/product/269/1621
        """
        data = {
            'GroupId': group_id,
            'MemberList': member_list,
            'Silence': silence
        }
        return self._post(
            'group_open_http_svc/add_group_member',
            data=data
        )

    def delete_group_member(self, group_id, member_to_del_account, silence=SILENCE_YES, reason=None):
        """删除群组成员

        https://cloud.tencent.com/document/product/269/1622
        """
        data = {
            'GroupId': group_id,
            'MemberToDel_Account': member_to_del_account,
            'Silence': silence
        }
        if reason:
            data['Reason'] = reason

        return self._post(
            'group_open_http_svc/delete_group_member',
            data=data
        )

    def modify_group_member_info(self, group_id, member_account, role=None, msg_flag=None, name_card=None,
                                 app_member_defined_data=None, shut_up_time=None):
        """修改群成员资料

        https://cloud.tencent.com/document/product/269/1623
        """
        data = {
            'GroupId': group_id,
            'Member_Account': member_account,
        }

        if role:
            data['Role'] = role

        if msg_flag:
            data['MsgFlag'] = msg_flag

        if name_card:
            data['NameCard'] = name_card

        if app_member_defined_data:
            data['AppMemberDefinedData'] = app_member_defined_data

        if shut_up_time:
            data['ShutUpTime'] = shut_up_time

        return self._post(
            'group_open_http_svc/modify_group_member_info',
            data=data
        )

    def destroy_group(self, group_id):
        """解散群组

        https://cloud.tencent.com/document/product/269/1624
        """
        data = {
            'GroupId': group_id,
        }

        return self._post(
            'group_open_http_svc/destroy_group',
            data=data
        )

    def get_joined_group_list(self, member_account, limit=None, offset=None, group_type=None, with_huge_groups=None,
                              with_no_active_groups=None, response_filter=None):
        """获取用户所加入的群组

        https://cloud.tencent.com/document/product/269/1625
        """
        data = {
            'Member_Account': member_account,
        }

        if limit:
            data['Limit'] = limit

        if offset:
            data['Offset'] = offset

        if group_type:
            data['GroupType'] = group_type

        if with_huge_groups:
            data['WithHugeGroups'] = with_huge_groups

        if with_no_active_groups:
            data['WithNoActiveGroups'] = with_no_active_groups

        if response_filter:
            data['ResponseFilter'] = response_filter

        return self._post(
            'group_open_http_svc/get_joined_group_list',
            data=data
        )

    def get_role_in_group(self, group_id, user_account):
        """查询用户在群组中的身份

        https://cloud.tencent.com/document/product/269/1626
        """
        data = {
            'GroupId': group_id,
            'User_Account': user_account
        }

        return self._post(
            'group_open_http_svc/get_role_in_group',
            data=data
        )

    def forbid_send_msg(self, group_id, members_account, shut_up_time=0):
        """批量禁言和取消禁言

        https://cloud.tencent.com/document/product/269/1627
        """
        data = {
            'GroupId': group_id,
            'Members_Account': members_account,
            'ShutUpTime': shut_up_time
        }

        return self._post(
            'group_open_http_svc/forbid_send_msg',
            data=data
        )

    def get_group_shut_uin(self, group_id):
        """获取群组被禁言用户列表

        https://cloud.tencent.com/document/product/269/2925
        """
        data = {
            'GroupId': group_id,
        }

        return self._post(
            'group_open_http_svc/get_group_shutted_uin',
            data=data
        )

    def send_group_msg(self, group_id, msg_body, from_account=None, msg_random=random.randint(0, 4294967295),
                       msg_priority=None, forbid_callback_control=None, online_only_flag=ONLINE_ONLY_FLAG_NO,
                       offline_push_info=None):
        """在群组中发送普通消息

        https://cloud.tencent.com/document/product/269/1629
        """
        data = {
            'GroupId': group_id,
            'Random': msg_random,
            'MsgBody': msg_body
        }

        if from_account:
            data['From_Account']: from_account

        if msg_priority:
            data['MsgPriority']: msg_priority

        if forbid_callback_control:
            data['ForbidCallbackControl']: forbid_callback_control

        if online_only_flag:
            data['OnlineOnlyFlag']: online_only_flag

        if offline_push_info:
            data['OfflinePushInfo']: offline_push_info

        return self._post(
            'group_open_http_svc/send_group_msg',
            data=data
        )

    def send_group_system_notification(self, group_id, content, to_members_account=None):
        """在群组中发送系统通知

        https://cloud.tencent.com/document/product/269/1630
        """
        data = {
            'GroupId': group_id,
            'Content': content,
        }

        if to_members_account:
            data['ToMembers_Account']: to_members_account

        return self._post(
            'group_open_http_svc/send_group_system_notification',
            data=data
        )

    def group_msg_recall(self, group_id, msg_seq_list):
        """撤回群组消息

        https://cloud.tencent.com/document/product/269/12341
        """
        data = {
            'GroupId': group_id,
            'MsgSeqList': msg_seq_list,
        }

        return self._post(
            'group_open_http_svc/group_msg_recall',
            data=data
        )

    def change_group_owner(self, group_id, new_owner_account):
        """转让群组

        https://cloud.tencent.com/document/product/269/1633
        """
        data = {
            'GroupId': group_id,
            'NewOwner_Account': new_owner_account,
        }

        return self._post(
            'group_open_http_svc/change_group_owner',
            data=data
        )

    def import_group(self, name, owner_account=None, group_type=TYPE_PUBLIC, group_id=None, create_time=None,
                     introduction=None, notification=None, face_url=None, max_member_count=None,
                     apply_join_option=None, app_defined_data=None):
        """导入群基础资料

        https://cloud.tencent.com/document/product/269/1634
        """
        data = {
            'Name': name,
            'Type': group_type
        }

        if owner_account:
            data['Owner_Account'] = owner_account

        if create_time:
            data['CreateTime'] = create_time

        if group_id:
            data['GroupId'] = group_id

        if max_member_count:
            data['MaxMemberCount'] = max_member_count

        if introduction:
            data['Introduction'] = introduction

        if notification:
            data['Notification'] = notification

        if face_url:
            data['FaceUrl'] = face_url

        if apply_join_option:
            data['ApplyJoinOption'] = apply_join_option

        if app_defined_data:
            data['AppDefinedData'] = app_defined_data

        return self._post(
            'group_open_http_svc/import_group',
            data=data
        )

    def import_group_msg(self, group_id, msg_list):
        """导入群消息

        https://cloud.tencent.com/document/product/269/1635
        """
        data = {
            'GroupId': group_id,
            'MsgList': msg_list
        }

        return self._post(
            'group_open_http_svc/import_group_msg',
            data=data
        )

    def import_group_member(self, group_id, member_list, join_time=None, unread_msg_num=None):
        """导入群成员

        https://cloud.tencent.com/document/product/269/1636
        """
        data = {
            'GroupId': group_id,
            'MemberList': member_list
        }

        if join_time:
            data['JoinTime'] = join_time

        if unread_msg_num:
            data['UnreadMsgNum'] = unread_msg_num

        return self._post(
            'group_open_http_svc/import_group_member',
            data=data
        )

    def set_unread_msg_num(self, group_id, member_account, unread_msg_num):
        """设置成员未读消息计数

        https://cloud.tencent.com/document/product/269/1637
        """
        data = {
            'GroupId': group_id,
            'Member_Account': member_account,
            'UnreadMsgNum': unread_msg_num,
        }

        return self._post(
            'group_open_http_svc/set_unread_msg_num',
            data=data
        )

    def delete_group_msg_by_sender(self, group_id, sender_account):
        """删除指定用户发送的消息

        https://cloud.tencent.com/document/product/269/2359
        """
        data = {
            'GroupId': group_id,
            'Sender_Account': sender_account,
        }

        return self._post(
            'group_open_http_svc/delete_group_msg_by_sender',
            data=data
        )

    def group_msg_get_simple(self, group_id, req_msg_number, req_msg_seq=None):
        """拉取群漫游消息

        https://cloud.tencent.com/document/product/269/2738
        """
        data = {
            'GroupId': group_id,
            'ReqMsgNumber': req_msg_number,
        }
        if req_msg_seq:
            data['ReqMsgSeq'] = req_msg_seq

        return self._post(
            'group_open_http_svc/group_msg_get_simple',
            data=data
        )
