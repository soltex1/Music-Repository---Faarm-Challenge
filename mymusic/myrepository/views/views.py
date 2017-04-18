"""
Settings and all classes/functions for the Album

index - shows all albums
detail - show an album by id
create - create a new album
delete - delete an album by id
update - update an album by id

"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone

from myrepository.models import Album, AlbumSerializer, Genre, Lending
from myrepository.forms import AlbumForm

def index(request):
	all_albums = Album.objects.all()
	context = {'all_albums': all_albums}
	return render(request, 'myrepository/index.html', context)

def detail(request, album_id):
	album = Album.objects.get(id = album_id)
	context = {'album': album}
	return render(request, 'myrepository/album_detail.html', context)

def create(request): 
  if request.method == "POST": 
    form = AlbumForm(request.POST) 
    if form.is_valid(): 
      post = form.save(commit=False) 
      post.title = request.POST.get('title') # or form.cleaned_data['title'] 
      post.description = request.POST.get('description') 
      post.c_date = timezone.now() 
      post.n_songs = request.POST.get('n_songs')
      post.save()

      # if the request has the key 'teste' its means that we selected the field lending and it needs to be added
      if request.POST.get('teste') is not None:
      	lending = Lending(album=post, c_date=timezone.now(), l_date=timezone.now())
      	lending.save()

      # adding each genre selected to album
      for genre_id in form.cleaned_data['genres']:
      	post.genres.add(Genre.objects.get(name=genre_id))

      return redirect('detail', album_id=post.id) 
  else: 
    form = AlbumForm() 
    return render(request, 'myrepository/album_create.html', {'form':form})

def delete(request, album_id):
	album = Album.objects.get(id = album_id)
	context = {'album': album}

	if request.method == "POST":
		message = 'Album ' + str(album.id) + ' with title ['+str(album.title)+'] was removed successfully!'
		messages.add_message(request, messages.SUCCESS, message)
		album.delete()
		return redirect('albums_index')
	else:
		return render(request, 'myrepository/album_delete.html', context)

def update(request, album_id):
	album = Album.objects.get(id=album_id)
	form = AlbumForm(request.POST or None, instance=album)
	lent_number = Lending.objects.filter(album_id=album.id).count()

	# if album has been lent, then change the checkbox value to True
	if lent_number > 0:
		form.fields["teste"].initial = True

	if request.method == "POST":
		if form.is_valid():
			# delete all genres from album
			album.genres.clear()
			# delete lending value if exists
			if lent_number > 0:
				album.lending.delete()

			post = form.save(commit=False)
			post.title = request.POST.get('title') 
			post.description = request.POST.get('description')
			post.c_date = timezone.now()
			post.n_songs = request.POST.get('n_songs')

			# if the request has the key 'teste' its means that we selected the field lending and it needs to be added
			if request.POST.get('teste') is not None:
				lending = Lending(album=post, c_date=timezone.now(), l_date=timezone.now())
				lending.save()

			# adding each genre selected to album
			for genre_id in form.cleaned_data['genres']:
				post.genres.add(Genre.objects.get(name=genre_id))

			post.save()
			return redirect('album_detail', album_id=album.id)
	else:
		return render(request, 'myrepository/album_update.html',{'form': form})