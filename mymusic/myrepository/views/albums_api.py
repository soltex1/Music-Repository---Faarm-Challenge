# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404

# rest api framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from myrepository.models import Album, AlbumSerializer

class AlbumList(APIView):

	def get(self, request, format=None):
		album = Album.objects.all()
		album_serializer = AlbumSerializer(album, many=True)
		return Response(album_serializer.data)

class AlbumDetail(APIView):

	def get_object(self, album_id):
		try:
			return Album.objects.get(id=album_id)
		except:
			raise Http404

	def get(self, request, album_id, format=None):
		album = self.get_object(album_id)
		album_serializer = AlbumSerializer(album)
		return Response(album_serializer.data)
