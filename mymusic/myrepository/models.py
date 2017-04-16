# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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

	def __str__(self):
		return self.title

class Genre(models.Model):
	name = models.CharField(max_length = 200, unique=True)
	albums = models.ManyToManyField(Album)

	def __str__(self):
		return self.name
	
class Lending(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE, unique=True)
	l_date = models.DateTimeField('date lent')
	c_date = models.DateTimeField('date created')

	def __str__(self):
		return self.album

	def __unicode__(self):
		return unicode(self.album)