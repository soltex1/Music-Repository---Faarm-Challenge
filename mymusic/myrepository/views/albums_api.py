# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.utils import timezone

# rest api framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from myrepository.models import Album, AlbumSerializer, Lending

class AlbumList(APIView):
	''' get all albums '''
	def get(self, request, format=None):
		album = Album.objects.all()
		album_serializer = AlbumSerializer(album, many=True)
		return Response(album_serializer.data)

	def post(self, request, format=None):
		serializer = AlbumSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumListFavorites(APIView):
	''' get all favorite albums '''
	def get(self, request,format=None):
		album = Album.objects.filter(favorite=True)
		album_serializer = AlbumSerializer(album, many=True)
		return Response(album_serializer.data)

class AlbumListLent(APIView):
	''' get all albums that were lent '''
	def get(self, request,format=None):
		album = Album.objects.exclude(lending=None)
		album_serializer = AlbumSerializer(album, many=True)
		return Response(album_serializer.data)

class AlbumListAvailable(APIView):
	''' get all albums that were not lent '''
	def get(self, request,format=None):
		album = Album.objects.filter(lending=None)
		album_serializer = AlbumSerializer(album, many=True)
		return Response(album_serializer.data)

class AlbumDetail(APIView):
	''' get an album instance by id '''
	def get_object(self, album_id):
		try:
			return Album.objects.get(id=album_id)
		except:
			raise Http404

	def get(self, request, album_id, format=None):
		album = self.get_object(album_id)
		album_serializer = AlbumSerializer(album)
		return Response(album_serializer.data)

	''' update an album instance by given a dictionary with the fields '''
	def put(self, request, album_id, format=None):
		album = self.get_object(album_id)
		album_serializer = AlbumSerializer(album, data=request.data, partial=True)
				
		if 'lending' in request.data:
			if request.data['lending'] == album_id:
				lending = Lending(album=album, c_date=timezone.now(), l_date=timezone.now())
				lending.save()

		if album_serializer.is_valid():
			album_serializer.save()

			return Response(album_serializer.data)
		return Response(album_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	''' remove an album completely or only the lending value by giving a dictionary with key lending and value '''
	def delete(self, request, album_id, format=None):
		album = self.get_object(album_id)
		if 'lending' in request.data:
			if request.data['lending'] == 'false':
				Lending.objects.filter(album_id=album.id).delete()
		else:
			album.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)





