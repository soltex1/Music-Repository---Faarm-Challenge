"""
Settings and all classes/functions for the Album

index - shows all genres
detail - show an genre by id
create - create a new genre
delete - delete a genre by id
update - update a genre by id

"""

# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from myrepository.models import Genre
from myrepository.forms import GenreForm

def index(request):
	all_genres = Genre.objects.all()
	context = {'all_genres': all_genres}
	return render(request, 'myrepository/genres_index.html', context)

def detail(request, genre_id):
	genre = Genre.objects.get(id=genre_id)
	context = {'genre': genre}
	return render(request, 'myrepository/genre_detail.html', context)

def create(request): 
  if request.method == "POST": 
    form = GenreForm(request.POST) 
    if form.is_valid(): 
      post = form.save(commit=False) 
      post.name = request.POST.get('name') # or form.cleaned_data['name'] 
      post.save()
      return redirect('genre_detail', genre_id=post.id) 
  else: 
    form = GenreForm() 
    return render(request, 'myrepository/genre_create.html', {'form':form})

def delete(request, genre_id):
	genre = Genre.objects.get(id = genre_id)
	context = {'genre': genre}

	if request.method == "POST":
		# prevent delete a genre that is associated with albums
		if genre.album_set.count() > 0:
			message = 'this genre is associated with albums, you cant delete'
			messages.add_message(request, messages.ERROR, message)
			return redirect('genre_delete', genre.id)
		else:
			genre.delete()
			message = 'genre deleted'
			messages.add_message(request, messages.SUCCESS, message)
			return redirect('genres_index')
	else:
		return render(request, 'myrepository/genre_delete.html', context)

def update(request, genre_id):
	genre = Genre.objects.get(id=genre_id)
	form = GenreForm(request.POST or None, instance=genre)

	if request.method == "POST":
		if form.is_valid():
			post = form.save(commit=False)
			post.name = request.POST.get('name')
			post.save()
			return redirect('genre_detail', genre_id=post.id)
	else:
		return render(request, 'myrepository/genre_update.html',{'form': form})