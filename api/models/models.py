# -*- coding=utf-8 -*-

from mongoengine import Document, StringField


class Followers(Document):
    '''关注的人'''
    # 微信号
    user_id = StringField()
    # 地理位置
    location = StringField()
