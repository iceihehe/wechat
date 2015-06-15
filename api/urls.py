# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url
from views import views

urlpatterns = patterns(
    '',
    url(r'(?P<uid>\w+)/$', views.WechatInterfaceView.as_view()),

)
