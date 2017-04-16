# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from myrepository.models import Album

from django.contrib import messages
def index(request):
	messages.add_message(request, messages.INFO, 'Hello world.')
	all_albums = Album.objects.all()
	context = {'all_albums': all_albums}
	return render(request, 'myrepository/index.html', context)
