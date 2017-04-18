"""
URL's config for myrepository app.

"""
from django.conf.urls import url

from myrepository.views import views, genres
from myrepository.views import AlbumList, AlbumListFavorites, AlbumListLent, AlbumListAvailable, AlbumDetail, GenreList, GenreDetail

appname='myrepository'

urlpatterns = [
	
	# albums urls

	url(r'^$', views.index, name='albums_index'),
	url(r'^a1lbum/(?P<album_id>\d+)/$', views.detail, name='album_detail'),
	url(r'^album/delete/(?P<album_id>\d+)/$', views.delete, name='album_delete'),
	url(r'^album/update/(?P<album_id>\d+)/$', views.update, name='album_update'),
	url(r'^album/new/$', views.create, name='album_create'),

	# albums rest api urls

	url(r'^api/v1/albums$', AlbumList.as_view()),
	url(r'^api/v1/albums/favorites$', AlbumListFavorites.as_view()),
	url(r'^api/v1/albums/lent$', AlbumListLent.as_view()),
	url(r'^api/v1/albums/available$', AlbumListAvailable.as_view()),
	url(r'^api/v1/album/(?P<album_id>\d+)/$', AlbumDetail.as_view()),

	# genres urls
	
	url(r'^genres$', genres.index, name='genres_index'),
	url(r'^genres/new/$', genres.create, name='genre_create'),
	url(r'^genres/(?P<genre_id>\d+)/$', genres.detail, name='genre_detail'),
	url(r'^genres/update/(?P<genre_id>\d+)/$', genres.update, name='genre_update'),
	url(r'^genres/delete/(?P<genre_id>\d+)/$', genres.delete, name='genre_delete'),

  	# genres api urls
  	
  	url(r'^api/v1/genres$', GenreList.as_view()),
  	url(r'^api/v1/genre/(?P<genre_id>\d+)/$', GenreDetail.as_view()),
]