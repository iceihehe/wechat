# -*- coding=utf-8 -*-
# Created Time: 2015年06月23日 星期二 19时52分38秒
# File Name: process.py

from __future__ import print_function, unicode_literals


class TextProcessor(object):
    '''
    处理文本消息
    '''
    @classmethod
    def process(wechat, message):
        pass


class LocationProcessor(object):
    '''
    处理地理位置消息
    '''
    @classmethod
    def process(wechat, message):
        print('wechat: ', wechat)
