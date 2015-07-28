# -*- coding=utf-8 -*-
# Created Time: Fri Jun 26 08:07:27 2015
# File Name: weather.py

from __future__ import print_function, unicode_literals

import requests

from django.views.generic import View
from django.shortcuts import render

from baidu_extend.basic import BaiduBasic
from const import ak, appid, appsecret
from api.models.models import Follower


class IndexView(View):
    '''
    天气列表
    '''
    def get(self, request, *args, **kwargs):
        print('token', request.session.get('token'))
        location = request.GET.get('location')
        baidu = BaiduBasic(ak=ak)
        results = baidu.get_weather(location)
        # 获取code
        code = request.GET.get('code')
        if code:
            url = 'https://api.weixin.qq.com/sns/oauth2/access_token'
            r = requests.post(
                url=url,
                params={
                    'appid': appid,
                    'secret': appsecret,
                    'code': code,
                    'grant_type': 'authorization_code',
                }
            )
            url1 = 'https://api.weixin.qq.com/sns/userinfo'
            r1 = requests.get(
                url=url1,
                params={
                    'access_token': r.json()['access_token'],
                    'openid': r.json()['openid'],
                    'lang': 'zh_CN',
                }
            )
            Follower.objects(user_id=r1.json()['openid']).update_one(
                upsert=True,
            )
        return render(request, 'weather.html', {'results': results})
