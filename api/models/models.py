# -*- coding=utf-8 -*-

from mongoengine import Document, StringField, FloatField, IntField,\
    EmbeddedDocumentField, EmbeddedDocument


class Location(EmbeddedDocument):
    '''地理位置'''
    # 经度
    longitude = FloatField()
    # 纬度
    latitude = FloatField()
    # 精度
    precision = FloatField()
    # 缩放大小
    scale = IntField()
    # 地理位置信息
    label = StringField()


class Follower(Document):
    '''关注的人'''
    # 微信号
    user_id = StringField()
    # 地理位置
    location = EmbeddedDocumentField(Location)


class Response(Document):
    '''
    关键词回复
    暂时没有素材
    全是文字回复
    '''
    # 关键词
    keyword = StringField()
    # 回复
    res = StringField()
