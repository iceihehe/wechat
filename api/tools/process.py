# -*- coding=utf-8 -*-
# Created Time: 2015年06月23日 星期二 19时52分38秒
# File Name: process.py

from __future__ import print_function, unicode_literals

from api.models.models import Follower, Response
from baidu_extend.basic import BaiduBasic
from const import TEMPLATE_ID, AK


class TextProcessor(object):
    '''
    处理文本消息
    '''
    @classmethod
    def process(cls, wechat, message):
        # 如果关键词有重复的，取最新添加的
        response = Response.objects(keyword_list__in=[message.content])\
            .order_by('-id')
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


class ClickProcessor(object):
    '''
    处理点击事件
    '''
    @classmethod
    def process(cls, wechat, message):
        if message.key == 'weather':
            try:
                user = Follower.objects(user_id=message.source).first()
                location = user.location
            except:
                return wechat.response_text('先发送地理位置噻')
            # 来自百度天气的数据
            baidu = BaiduBasic(ak=AK)
            ll = "%s,%s" % (location.longitude, location.latitude)
            print("location: ", ll)
            try:
                results = baidu.get_weather(ll)
            except:
                return wechat.response_text('你跑火星去了说')

            data = {
                'city': {
                    'value': results['results'][0]['currentCity']
                    },
                'date': {
                    'value': results['results'][0]['weather_data'][0]['date'],
                    },
                'weather': {
                    'value': results['results'][0]['weather_data'][0]['weather'],
                    },
                'temp': {
                    'value': results['results'][0]['weather_data'][0]['temperature'],
                    },
                'wind': {
                    'value': results['results'][0]['weather_data'][0]['wind'],
                    },
                'pm25': {
                    'value': results['results'][0]['pm25'],
                    },
            }
            wechat.send_template_message(
                user_id=message.source,
                template_id=TEMPLATE_ID['weather'],
                data=data,
                url="http://104.236.136.36/weather?location=" + ll
            )
            return ''
        return wechat.response_text('tm的出错了')
