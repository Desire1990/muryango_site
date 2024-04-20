from django.db import models
from io import BytesIO
from PIL import Image
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from datetime import datetime, date
from django.utils import timezone
from django.core.files import File
from django.db import models
from django.core.files import File
from PIL import Image
from django.db import transaction


class Objectif(models.Model):
	id=models.SmallAutoField(primary_key=True)
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to="objectif/")
	bref = models.TextField()
	objectif = models.TextField()

	def __str__(self):
		return f"{self.name}"

class Equipe(models.Model):
	id=models.SmallAutoField(primary_key=True)
	logo = models.ImageField(upload_to='equipe/')
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=50)
	titre = models.CharField(max_length=150)
	telephone = models.CharField(max_length=50, unique=True)
	email = models.EmailField(max_length=254,unique=True)

	thumbnail = models.ImageField(upload_to='logo/thumbnail/', null=True,  blank=True)

	def __str__(self):
		return f"{self.nom}"

	def get_absolute_url(self):
		return f'/{self.id}/'

	def get_logo(self):
		if self.logo:
			return self.logo.url
		return '' 

	def get_thumbnail(self):
		if self.thumbnail:
			return self.thumbnail.url
		else:
			if self.logo:
				self.thumbnail = (self.logo)
				self.save()

				return self.thumbnail.url
			else:
				return ''

	def make_thumbnail(self, logo, size=(200, 100)):
		""" make 300x200 px thumbnail from given image"""
		img = Image.open(logo, encoding='UTF-16')
		img.convert('RGB')
		img.thumbnail(size)
		
		thumb_io = BytesIO()
		img.save(thumb_io, 'JPEG', quality=85)

		thumbnail = File(thumb_io, name=logo.name)
		return thumbnail

class Logo(models.Model):
	id=models.SmallAutoField(primary_key=True)
	name = models.CharField(max_length=50)
	logo = models.ImageField(upload_to='logo/')
	thumbnail = models.ImageField(upload_to='logo/thumbnail/', null=True,  blank=True)

	def __str__(self):
		return f"{self.name}"

	def get_absolute_url(self):
		return f'/{self.id}/'

	def get_logo(self):
		if self.logo:
			return self.logo.url
		return '' 

	def get_thumbnail(self):
		if self.thumbnail:
			return self.thumbnail.url
		else:
			if self.logo:
				self.thumbnail = (self.logo)
				self.save()

				return self.thumbnail.url
			else:
				return ''

	def make_thumbnail(self, logo, size=(200, 100)):
		""" make 300x200 px thumbnail from given image"""
		img = Image.open(logo, encoding='UTF-16')
		img.convert('RGB')
		img.thumbnail(size)
		
		thumb_io = BytesIO()
		img.save(thumb_io, 'JPEG', quality=85)

		thumbnail = File(thumb_io, name=logo.name)
		return thumbnail
