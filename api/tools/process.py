# -*- coding=utf-8 -*-
# Created Time: 2015年06月23日 星期二 19时52分38秒
# File Name: process.py

from __future__ import print_function, unicode_literals

from api.models.models import Follower, Location, Response


class TextProcessor(object):
    '''
    处理文本消息
    '''
    @classmethod
    def process(cls, wechat, message):
        print('hehe')
        response = Response.objects(keyword=message.content)
        if response:
            return wechat.response_text(response.first().res)
        return wechat.response_text('你在说什么')


class LocationProcessor(object):
    '''
    处理地理位置消息
    '''
    @classmethod
    def process(cls, wechat, message):
        source = message.source
        # 上报地理位置
        try:
            longitude = message.longitude
            latitude = message.latitude
            precision = message.precision
            Follower.objects(user_id=source).update_one(
                upsert=True,
                set__user_id=source,
                set__location__latitude=latitude,
                set__location__longitude=longitude,
                set__location__precision=precision,
            )
        # 地理位置消息
        except:
            latitude, longitude = message.location
            scale = message.scale
            label = message.label
            Follower.objects(user_id=source).update_one(
                upsert=True,
                set__user_id=source,
                set__location__label=label,
                set__location__scale=scale,
                set__location__latitude=latitude,
                set__location__longitude=longitude,
            )


class SubscribeProcessor(object):
    '''
    处理关注消息
    '''
    @classmethod
    def process(cls, wechat, message):
        Follower.objects(user_id=message.source).update_one(
            upsert=True,
            set__user_id=message.source
        )
        return wechat.response_text('欢迎加入， 你个逗比')
