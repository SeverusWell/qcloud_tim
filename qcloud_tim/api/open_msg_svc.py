# -*- coding: utf-8 -*-
import time

from . import BaseRESTAPI


class OpenMSGSVC(BaseRESTAPI):
    """消息记录

    """
    CHAT_TYPE_C2C = 'C2C'
    CHAT_TYPE_GROUP = 'Group'

    def get_history(self, chat_type, msg_time=None):
        """下载消息记录

        https://cloud.tencent.com/document/product/269/1650
        """
        data = {
            'ChatType': chat_type,
            'MsgTime': msg_time or time.strftime('%Y%m%d%H', time.localtime(time.time() - 60 * 60 * 3))
        }

        return self._post(
            'open_msg_svc/get_history',
            data=data
        )
