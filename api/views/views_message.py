# -*- coding=utf-8 -*-
# Created Time: 2015年06月23日 星期二 09时45分37秒
# File Name: views_message.py
'''
处理用户输入文字，图片等的数据
'''

from __future__ import print_function, unicode_literals
import abc


class MessageProcessor(object):
    __metaclass__ = abc.ABCMeta
