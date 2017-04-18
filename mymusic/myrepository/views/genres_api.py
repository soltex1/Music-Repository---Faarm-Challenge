"""
Settings and all classes/functions for the Genre Rest API

"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.utils import timezone

# rest api framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from myrepository.models import Genre, GenreSerializer

class GenreList(APIView):
	''' get all albums '''
	def get(self, request, format=None):
		genres = Genre.objects.all()
		genres_serializer = GenreSerializer(genres, many=True)
		return Response(genres_serializer.data)
	''' post a new album '''
	def post(self, request, format=None):
		serializer = GenreSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
	''' get an genre instance by id '''
	def get_object(self, genre_id):
		try:
			return Genre.objects.get(id=genre_id)
		except:
			raise Http404

	''' get an genre instance by id '''
	def get(self, request, genre_id, format=None):
		genre = self.get_object(genre_id)
		genres_serializer = GenreSerializer(genre)
		return Response(genres_serializer.data)

	''' update an album instance by given a dictionary with the fields (can be partial) '''
	def put(self, request, genre_id, format=None):
		genre = self.get_object(genre_id)
		genres_serializer = GenreSerializer(genre, data=request.data, partial=True)

		if genres_serializer.is_valid():
			genres_serializer.save()
			return Response(genres_serializer.data)
		return Response(genres_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, genre_id, format=None):
		genre = self.get_object(genre_id)
		genre.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)