from django.conf.urls import url
from streamer import views

app_name = 'stream'

urlpatterns = [
    url(r'^start$', views.StartStream.as_view(), name='start_stream'),
    url(r'^stop$', views.StopStream.as_view(), name='stop_stream'),
    url(r'^live/(?P<username>\w+)/index.m3u8', views.fake_view, name='current_steam_url'),
    url(r'^$', views.HomePage.as_view(), name='home')
]
