from django.conf.urls import url

from . import views

appname='myrepository'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]