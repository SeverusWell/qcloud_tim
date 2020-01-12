# -*- coding: utf-8 -*-

from . import BaseRESTAPI


class IMOpenLoginSVC(BaseRESTAPI):
    """帐号管理

    """

    def account_import(self, identifier, nick=None, face_url=None):
        """单个帐号导入接口

        https://cloud.tencent.com/document/product/269/1608
        """
        data = {
            'Identifier': identifier
        }
        if nick:
            data['Nick'] = nick
        if face_url:
            data['FaceUrl'] = face_url

        return self._post(
            'im_open_login_svc/account_import',
            data=data
        )

    def im_open_login_svc(self, accounts):
        """批量帐号导入接口

        https://cloud.tencent.com/document/product/269/4919
        """
        return self._post(
            'im_open_login_svc/multiaccount_import',
            data={
                'Accounts': accounts
            }
        )

    def account_delete(self, delete_item):
        """帐号删除接口

        https://cloud.tencent.com/document/product/269/36443
        """
        return self._post(
            'im_open_login_svc/account_delete',
            data={
                'DeleteItem': [{'UserID': user_id} for user_id in delete_item]
            }
        )

    def account_check(self, check_item):
        """帐号检查接口

        https://cloud.tencent.com/document/product/269/38417
        """
        return self._get(
            'im_open_login_svc/account_check',
            data={
                'CheckItem': [{'UserID': user_id} for user_id in check_item]
            }
        )

    def kick(self, identifier):
        """帐号登录态失效接口

        https://cloud.tencent.com/document/product/269/3853
        """
        return self._post(
            'im_open_login_svc/kick',
            data={
                'Identifier': identifier
            }
        )
