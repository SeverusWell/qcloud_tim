# -*- coding: utf-8 -*-
import os

from TLSSigAPIv2 import TLSSigAPIv2


class TLSSig(object):
    @staticmethod
    def gen_sig(identifier, app_id=None, app_key=None, expire=180 * 86400):
        app_id = app_id or os.environ.get('TENCENT_IM_app_id')
        app_key = app_key or os.environ.get('TENCENT_IM_SDK_APP_SECRET')

        api = TLSSigAPIv2(app_id, app_key)
        return api.gen_sig(identifier, expire)


if __name__ == "__main__":
    sig = TLSSig.gen_sig('xiaojun')
    print(sig)
