# -*- coding=utf-8 -*-

from __future__ import print_function, unicode_literals
from django.views.generic.base import View
from django.http import HttpResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_protect
# from wechat_sdk import WechatBasic
from wechat_extend import WechatExtend
from api.tools.process import LocationProcessor, SubscribeProcessor, TextProcessor


class WechatInterfaceView(View):
    '''微信交互'''
    def get(self, request, *args, **kwargs):
        '''微信平台修改服务器地址时用'''
        token = kwargs.get('token')
        data = request.GET
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')
        echostr = data.get('echostr')

        wechat = WechatExtend(token=token)

        # 验证是否来自微信服务器
        if not wechat.check_signature(
                signature=signature,
                timestamp=timestamp,
                nonce=nonce
                ):
            print('Not come from wechat')
            return HttpResponse('')

        return HttpResponse(echostr)

    def post(self, request, *args, **kwargs):
        '''微信平台向服务器发送消息'''
        token = kwargs.get('token')
        data = request.GET
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')

        wechat = WechatExtend(token=token)

        # 验证是否来自微信服务器
        if not wechat.check_signature(
                signature=signature,
                timestamp=timestamp,
                nonce=nonce
                ):
            print('Not come from wechat')
            return HttpResponse('')

        # 解析xml
        wechat.parse_data(request.body)
        message = wechat.get_message()

        print(request.body)
        print('type: ', message.type)

        res = ''

        # 地址消息
        if message.type == 'location':
            LocationProcessor.process(wechat, message)
        # 关注消息
        if message.type == 'subscribe':
            res = SubscribeProcessor.process(wechat, message)
        # 文本消息
        if message.type == 'text':
            res = TextProcessor.process(wechat, message)

        return HttpResponse(res)
