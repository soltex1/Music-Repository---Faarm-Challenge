# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from myrepository.models import Album, Genre
from myrepository.forms import AlbumForm, GenreForm, LendingForm

from django.contrib import messages
from django.utils import timezone


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
      #post.a_date = timezone.now() 
      post.c_date = timezone.now() 
      post.n_songs = request.POST.get('n_songs')

      post.save()

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

		album.delete()
		messages.add_message(request, messages.ERROR, message)

		return redirect('index')
	else:
		return render(request, 'myrepository/album_delete.html', context)

def update(request, album_id):
	album = Album.objects.get(id=album_id)
	form = AlbumForm(request.POST or None, instance=album)

	if request.method == "POST":
		if form.is_valid():
			album.genres.clear()

			post = form.save(commit=False)
			post.title = request.POST.get('title') # or form.cleaned_data['title']
			post.description = request.POST.get('description')
			#print form['a_date']
			#post.a_date = form['a_date']
			post.c_date = timezone.now()
			post.n_songs = request.POST.get('n_songs')
			for genre_id in form.cleaned_data['genres']:
				post.genres.add(Genre.objects.get(name=genre_id))

			post.save()

			return redirect('detail', album_id=album.id)
	else:
		return render(request, 'myrepository/album_update.html',{'form': form})
