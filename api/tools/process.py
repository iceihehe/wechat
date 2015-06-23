# -*- coding=utf-8 -*-
# Created Time: 2015年06月23日 星期二 19时52分38秒
# File Name: process.py

from __future__ import print_function, unicode_literals

from api.models.models import Followers, Location


class TextProcessor(object):
    '''
    处理文本消息
    '''
    @staticmethod
    def process(wechat, message):
        pass


class LocationProcessor(object):
    '''
    处理地理位置消息
    '''
    @staticmethod
    def process(wechat, message):
        longitude = message.longitude
        latitude = message.latitude
        precision = message.precision

        location = Location(
            longitude=longitude,
            latitude=latitude,
            precision=precision
        )

        Followers.objects(user_id=message.source).update_one(
            upsert=True,
            set__location=location
        )
