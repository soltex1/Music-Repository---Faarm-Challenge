# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from myrepository.models import Genre
from myrepository.forms import GenreForm

def index(request):
	all_genres = Genre.objects.all()
	context = {'all_genres': all_genres}
	return render(request, 'myrepository/genres_index.html', context)

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

def detail(request, genre_id):
	genre = Genre.objects.get(id=genre_id)
	context = {'genre': genre}
	return render(request, 'myrepository/genre_detail.html', context)

def update(request, genre_id):
	genre = Genre.objects.get(id=genre_id)
	form = GenreForm(request.POST or None, instance=genre)

	if request.method == "POST":
		if form.is_valid():
			post = form.save(commit=False)
			post.name = request.POST.get('name') # or form.cleaned_data['title']
			post.save()
			return redirect('genre_detail', genre_id=genre.id)
	else:
		return render(request, 'myrepository/genre_update.html',{'form': form})

def delete(request, genre_id):
	genre = Genre.objects.get(id = genre_id)
	context = {'genre': genre}

	if request.method == "POST":
		genre.delete()
		return redirect('genres_index')
	else:
		return render(request, 'myrepository/genre_delete.html', context)