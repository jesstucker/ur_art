from django.db import models
from django.conf import settings

class Artwork(models.Model):
	title = models.CharField(max_length=100)
	url = models.CharField(max_length=500)
	artist = models.ForeignKey(settings.AUTH_USER_MODEL)