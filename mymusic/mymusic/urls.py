"""
URL's config for mymusic project.

"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('myrepository.urls')),
]
