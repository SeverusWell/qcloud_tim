# -*- coding: utf-8 -*-
import random
import time

from . import BaseRESTAPI


class OpenIM(BaseRESTAPI):
    """单聊消息

    """
    SYNC_OTHER_MACHINE_YES = 1
    SYNC_OTHER_MACHINE_NO = 2

    SYNC_FROM_OLD_SYSTEM_REAL_TIME = 1
    SYNC_FROM_OLD_SYSTEM_HISTORY = 2

    def send_text_msg(self, to_account, content, from_account=None, sync_other_machine=SYNC_OTHER_MACHINE_YES,
                      msg_life_time=604800):
        """单发单聊文本消息

        https://cloud.tencent.com/document/product/269/2282
        """
        data = {
            'SyncOtherMachine': sync_other_machine,
            'To_Account': to_account,
            'MsgLifeTime': msg_life_time,
            'MsgRandom': random.randint(0, 4294967295),
            'MsgTimeStamp': int(time.time()),
            "MsgBody": [
                {
                    "MsgType": "TIMTextElem",
                    "MsgContent": {
                        "Text": content
                    }
                }
            ]
        }
        if from_account:
            data['From_Account'] = from_account

        return self._post(
            'openim/sendmsg',
            data=data
        )

    def batch_send_text_msg(self, to_account, content, from_account=None, sync_other_machine=SYNC_OTHER_MACHINE_YES):
        """批量发单聊消息

        https://cloud.tencent.com/document/product/269/1612
        """
        data = {
            'SyncOtherMachine': sync_other_machine,
            'To_Account': to_account,
            'MsgRandom': random.randint(0, 4294967295),
            "MsgBody": [
                {
                    "MsgType": "TIMTextElem",
                    "MsgContent": {
                        "Text": content
                    }
                }
            ]
        }
        if from_account:
            data['From_Account'] = from_account

        return self._post(
            'openim/batchsendmsg',
            data=data
        )

    def import_text_msg(self, to_account, from_account, content, msg_time_stamp=random.randint(0, 4294967295),
                        sync_from_old_system=SYNC_FROM_OLD_SYSTEM_REAL_TIME):
        """导入单聊消息

        https://cloud.tencent.com/document/product/269/2568
        """
        data = {
            'SyncFromOldSystem': sync_from_old_system,
            'From_Account': from_account,
            'To_Account': to_account,
            'MsgRandom': msg_time_stamp,
            'MsgTimeStamp': int(time.time()),
            "MsgBody": [
                {
                    "MsgType": "TIMTextElem",
                    "MsgContent": {
                        "Text": content
                    }
                }
            ]
        }

        return self._post(
            'openim/importmsg',
            data=data
        )

    def admin_msg_withdraw(self, to_account, from_account, msg_key):
        """撤回单聊消息

        https://cloud.tencent.com/document/product/269/38980
        """
        data = {
            'From_Account': from_account,
            'To_Account': to_account,
            'MsgKey': msg_key,
        }

        return self._post(
            'openim/admin_msgwithdraw',
            data=data
        )

    def query_state(self, to_account):
        """获取用户在线状态

        https://cloud.tencent.com/document/product/269/2566
        """
        data = {
            'To_Account': to_account,
        }

        return self._post(
            'openim/querystate',
            data=data
        )
