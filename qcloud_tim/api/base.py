# -*- coding: utf-8 -*-


class BaseRESTAPI(object):
    """ REST API base class """

    def __init__(self, client=None):
        self._client = client

    def _get(self, path, **kwargs):
        return self._client.get(path, **kwargs)

    def _post(self, path, **kwargs):
        return self._client.post(path, **kwargs)

    def get_client(self):
        return self._client

    def set_client(self, client):
        self._client = client
