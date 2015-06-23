# -*- coding=utf-8 -*-

from mongoengine import Document, StringField, FloatField,\
    EmbededDocumentField, EmbededDocument


class Location(EmbededDocument):
    '''地理位置'''
    # 经度
    longitude = FloatField()
    # 纬度
    latitude = FloatField()
    # 精度
    precision = FloatField()


class Followers(Document):
    '''关注的人'''
    # 微信号
    user_id = StringField()
    # 地理位置
    location = EmbededDocumentField(Location)
