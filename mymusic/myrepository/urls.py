from django.conf.urls import url

from . import views

appname='mymusic'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]