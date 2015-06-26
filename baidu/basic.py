# -*- coding=utf-8 -*-
# Created Time: 2015年06月26日 星期五 15时04分19秒
# File Name: basic.py

from __future__ import print_function, unicode_literals

import requests
import json


class BaiduBasic(object):
    """
    百度基本功能类

    其实现在我只用了天气接口
    """
    def __init__(self, ak=None):
        self.__ak = ak

    def get_weather(self, location):
        """
        获取天气
        location="x,y"  x是经度，y是维度
        或者
        location="北京"
        """
        self._check_ak()

        return self._post(
            url="http://api.map.baidu.com/telematics/v3/weather",
            params={
                'ak': self.__ak,
                'location': location,
            }
        )

    def _check_ak(self):
        if not self.__ak:
            raise EOFError(
                'Please provide ak parameter in the construction of class.'
            )

    def _post(self, url, **kwargs):
        """
        使用POST方法发请求
        """
        return self._request(
            method="post",
            url=url,
            **kwargs
        )

    def _request(self, method, url, **kwargs):
        """
        发送请求
        """
        if "params" not in kwargs:
            kwargs["params"] = {
                "ak": self.__ak,
            }
        if isinstance(kwargs.get("data", ""), dict):
            body = json.dumps(kwargs["data"], ensure_ascii=False)
            body = body.encode('utf8')
            kwargs["data"] = body

        r = requests.request(
            method=method,
            url=url,
            **kwargs
        )
        r.raise_for_status()
        response_json = r.json()
        self._check_official_error(response_json)
        return response_json

    def _check_official_error(self, json_data):
        """
        检测官方错误
        """
        if "error" in json_data and json_data["error"] != 0:
            raise EOFError(
                "{}: {}".format(json_data["error"], json_data["status"])
            )
