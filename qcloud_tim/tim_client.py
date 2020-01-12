# -*- coding: utf-8 -*-

# Author: Severus Well
# Contact: thinkweiwei@msn.com

"""A package for qcloud im(tim), Implement REST API."""

from . import HttpClient, TLSSig, api


class TimClient(object):

    def __init__(self, app_id, app_key, identifier='administrator'):
        self._app_id = app_id
        self._app_key = app_key
        self._identifier = identifier
        self._signature = TLSSig.gen_sig(identifier=identifier, app_id=app_id, app_key=app_key)

        client = HttpClient(self._app_id, self._identifier, self._signature)  # Default
        self.group_open_http_svc = api.GroupOpenHttpSVC(client=client)
        self.im_open_login_svc = api.IMOpenLoginSVC(client=client)
        self.open_im = api.OpenIM(client=client)
        self.profile = api.Profile(client=client)
        self.sns = api.SNS(client=client)
        self.open_config_svr = api.OpenConfigSVR(client=client)
        self.open_msg_svc = api.OpenMSGSVC(client=client)

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        if not isinstance(value, str):
            raise ValueError('identifier must be an str!')
        self._identifier = value

    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        if not isinstance(value, str):
            raise ValueError('signature must be an str!')
        self._signature = value
