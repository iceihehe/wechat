# -*- coding=utf-8 -*-
# Created Time: 2015年07月28日 星期二 10时57分22秒
# File Name: create_menu.py

from __future__ import print_function

from wechat_sdk.basic import WechatBasic
from const import appid, appsecret


button = {
    u'button': [
        {
            u'name': u'我的服务',
            u'sub_button': [
                {
                    u'type': u'click',
                    u'name': u'天气预报',
                    u'key': u'weather',
                    u'sub_button': []
                }
            ]
        },
        {
            u'name': u'公司测试',
            u'sub_button': [
                {
                    u'url': u'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx2102221b928b1121&redirect_uri=http%3A%2F%2Fgejin.eatornot.cn%2Fmall%2Fregister&response_type=code&scope=snsapi_base#wechat_redirect',
                    u'type': u'view',
                    u'name': u'个金注册',
                    u'sub_button': []
                }
            ]
        }
    ]
}

wechat = WechatBasic(appid=appid, appsecret=appsecret)

r = wechat.create_menu(button)
print(r)
