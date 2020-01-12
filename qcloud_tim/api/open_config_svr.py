# -*- coding: utf-8 -*-


from . import BaseRESTAPI


class OpenConfigSVR(BaseRESTAPI):
    """运营管理/全局禁言管理

    """

    def set_no_speaking(self, to_account, c2c_msg_no_speaking_time=None, group_msg_no_speaking_time=None):
        """设置全局禁言

        https://cloud.tencent.com/document/product/269/4230
        """
        data = {
            'Set_Account': to_account
        }
        if c2c_msg_no_speaking_time:
            data['C2CmsgNospeakingTime'] = c2c_msg_no_speaking_time
        if group_msg_no_speaking_time:
            data['GroupmsgNospeakingTime'] = group_msg_no_speaking_time

        return self._post(
            'openconfigsvr/setnospeaking',
            data=data
        )

    def get_no_speaking(self, get_account):
        """查询全局禁言

        https://cloud.tencent.com/document/product/269/4229
        """
        data = {
            'Get_Account': get_account
        }

        return self._post(
            'openconfigsvr/getnospeaking',
            data=data
        )

    def get_app_info(self, request_field=None):
        """拉取运营数据

        https://cloud.tencent.com/document/product/269/4193
        """
        data = {
        }
        if request_field:
            data['RequestField'] = request_field

        return self._post(
            'openconfigsvr/getappinfo',
            data=data
        )
