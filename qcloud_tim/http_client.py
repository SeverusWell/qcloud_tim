# -*- coding: utf-8 -*-

# Author: Severus Well
# Contact: thinkweiwei@msn.com

import json
import random
import requests


class HttpClient(object):

    def __init__(self, app_id, identifier, signature, timeout=10, auto_retry=True):
        self._app_id = app_id
        self._identifier = identifier
        self._signature = signature
        self.timeout = timeout
        self.auto_retry = auto_retry

        self._http = requests.Session()

    def get(self, path, **kwargs):
        return self._request(
            method='get',
            url=self.get_url(path),
            **kwargs
        )

    def post(self, path, **kwargs):
        return self._request(
            method='post',
            url=self.get_url(path),
            **kwargs
        )

    def get_url(self, path, random_id=random.randint(0, 4294967295)):
        protocol = 'https'
        host = 'console.tim.qq.com'
        ver = 'v4'
        url = '{protocol}://{host}/{ver}/{path}?sdkappid={app_id}&identifier={identifier}&usersig={signature}' \
              '&random={random_id}&contenttype=json'.format(
            protocol=protocol, host=host, ver=ver, path=path, app_id=self._app_id, identifier=self._identifier,
            signature=self._signature, random_id=random_id)
        return url

    def _request(self, method, url, **kwargs):
        if 'params' not in kwargs:
            kwargs['params'] = {}

        if isinstance(kwargs.get('data', ''), dict):
            body = (json.dumps(kwargs['data'], ensure_ascii=False)).encode('utf-8')
            kwargs['data'] = body

        kwargs['timeout'] = kwargs.get('timeout', self.timeout)
        result_processor = kwargs.pop('result_processor', None)
        res = self._http.request(method=method, url=url, **kwargs)

        try:
            res.raise_for_status()
        except Exception as e:
            raise Exception('TIM REST API request error!')

        return self._handle_result(res, method, url, result_processor, **kwargs)

    def _handle_result(self, res, method=None, url=None, result_processor=None, **kwargs):
        if not isinstance(res, dict):  # Dirty hack around asyncio based AsyncWeChatClient
            result = self._decode_result(res)
        else:
            result = res

        if not isinstance(result, dict):
            return result

        return result if not result_processor else result_processor(result)

    @staticmethod
    def _decode_result(res):
        try:
            result = json.loads(res.content.decode('utf-8', 'ignore'), strict=False)
        except (TypeError, ValueError):
            # Return origin response object if we can not decode it as JSON
            print('Can not decode response as JSON!')
            return res
        return result
