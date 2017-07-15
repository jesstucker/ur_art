from django.db import models

class ArtWork(models.Model):
    title = models.CharField(max_length=30)

