# -*- coding=utf-8 -*-

from mongoengine import Document, StringField, FloatField


class Followers(Document):
    '''关注的人'''
    # 微信号
    user_id = StringField()
    # 经度
    longitude = FloatField()
    # 纬度
    latitude = FloatField()
