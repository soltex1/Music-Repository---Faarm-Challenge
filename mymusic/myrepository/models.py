"""
Models setting for: Genre, Album, Lending, Artist and Lending

"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# rest api framework
from rest_framework import serializers

class Genre(models.Model):
	name = models.CharField(max_length = 200, unique=True)

	def __unicode__(self):
		return unicode(self.name)

class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = ['name']

class Album(models.Model):
	DIGITAL = 'dg'
	PHYSICAL = 'ps'
	TYPES_CHOICES = (
		(DIGITAL, 'Digital'),
		(PHYSICAL, 'Physical'),
	)
	types = models.CharField(max_length = 2, choices = TYPES_CHOICES, default = DIGITAL)
	title = models.CharField(max_length = 200)
	description = models.CharField(max_length = 400)
	favorite = models.BooleanField(default=False)
	n_songs = models.IntegerField()
	a_date = models.DateTimeField('album date')
	c_date = models.DateTimeField('date created')
	genres = models.ManyToManyField(Genre)

	def __unicode__(self):
		return unicode(self.title) 

class AlbumSerializer(serializers.ModelSerializer):
	class Meta:
		model = Album
		fields = ['id','lending','title','a_date','c_date','favorite','n_songs','description','genres','types'] 

class Lending(models.Model):
	album = models.OneToOneField(Album, on_delete=models.CASCADE, primary_key=True)
	l_date = models.DateTimeField('date lent')
	c_date = models.DateTimeField('date created')

	def __unicode__(self):
		return unicode('Yes')

class Artist(models.Model):
	album = models.ManyToManyField(Album)
	name = models.CharField(max_length = 100, unique=True)
	c_date = models.DateTimeField('date created')

	def __unicode__(self):
		return unicode(self.album)

class Track(models.Model):
	album = models.ManyToManyField(Album)
	name = models.CharField(max_length = 100)
	duration = models.TimeField()
	c_date = models.DateTimeField('date created')

	def __unicode__(self):
		return unicode(self.album)