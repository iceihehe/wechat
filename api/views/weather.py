# -*- coding=utf-8 -*-
# Created Time: Fri Jun 26 08:07:27 2015
# File Name: weather.py

from __future__ import print_function, unicode_literals

from django.views.generic import View
from django.shortcuts import render

from baidu_extend.basic import BaiduBasic
from const import ak


class IndexView(View):
    '''
    天气列表
    '''
    def get(self, request, *args, **kwargs):
        location = request.GET.get('location')
        baidu = BaiduBasic(ak=ak)
        results = baidu.get_weather(location)
        return render(request, 'weather.html', {'results': results})
