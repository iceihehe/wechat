# -*- coding=utf-8 -*-

from __future__ import print_function, unicode_literals
from django.views.generic.base import View
from django.http import HttpResponse


class WechatInterfaceView(View):
    '''微信交互'''
    def get(self, request, *args, **kwargs):
        '''微信平台修改服务器地址时用'''
        uid = kwargs.get('uid')
        data = request.GET
        print('uid, ', uid)
        print('data, ', data)
        return HttpResponse(uid)
