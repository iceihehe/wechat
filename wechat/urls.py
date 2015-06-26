from django.conf.urls import patterns, include, url

from api.views import weather

urlpatterns = patterns(
    '',
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^weather/$', weather.IndexView.as_view()),

)
