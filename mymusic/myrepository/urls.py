from django.conf.urls import url

from . import views

appname='myrepository'
urlpatterns = [
    url(r'^$', views.index, name='index'),
  	url(r'^(?P<album_id>\d+)/$', views.detail, name='detail'),
]