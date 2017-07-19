from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User

class Artwork(models.Model):
	title = models.CharField(max_length=100)
	url = models.CharField(max_length=500)
	artist = models.ForeignKey(settings.AUTH_USER_MODEL)
	# artist = models.ForeignKey(User, related_name='artist')