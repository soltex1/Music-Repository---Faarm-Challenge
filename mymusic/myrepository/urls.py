from django.conf.urls import url

from . import views

appname='myrepository'
urlpatterns = [
    url(r'^$', views.index, name='index'),
  	url(r'^album/(?P<album_id>\d+)/$', views.detail, name='detail'),
  	url(r'^album/delete/(?P<album_id>\d+)/$', views.delete, name='delete'),
  	url(r'^album/update/(?P<album_id>\d+)/$', views.update, name='update'),
  	url(r'^album/new/$', views.create, name='create'),
]