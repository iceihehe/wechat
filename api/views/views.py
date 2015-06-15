# -*- coding=utf-8 -*-

from __future__ import print_function, unicode_literals
from django.views.generic.base import View
from django.http import HttpResponse
from wechat_sdk import WechatBasic


class WechatInterfaceView(View):
    '''微信交互'''
    def get(self, request, *args, **kwargs):
        '''微信平台修改服务器地址时用'''
        token = kwargs.get('token')
        data = request.GET
        print('token, ', token)
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')
        echostr = data.get('echostr')

        # 验证是否来自微信服务器
        wechat = WechatBasic(token=token)
        print('come from wechat')
        if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponse(echostr)
        print('not come from wechat')
        return HttpResponse()
